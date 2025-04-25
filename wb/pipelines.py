# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector, hashlib, json, urllib.request, requests, pika, redis, os

from wb.spiders.base_spider import BaseSpider
from datetime import datetime
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

load_dotenv()

class WbPipeline(object):
    def __init__(self):

        self.update_fields = {
            'web_content': 'web_content',
            'web_like_count': 'web_like_count',
            'web_crawler_time': 'web_crawler_time'
        }
        self.es = Elasticsearch([{'host': os.getenv('ES_HOST'), 'port': int(os.getenv('ES_PORT')), 'scheme': 'http'}])
        self.now  = datetime.now()

        self.conn = mysql.connector.connect(user=os.getenv('MYSQL_USERNAME'),
                                    passwd=os.getenv('MYSQL_PASSWD'),
                                    db=os.getenv('MYSQL_DB'),
                                    host=os.getenv('MYSQL_HOST'),
                                    charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        

        credentials = pika.PlainCredentials(username=os.getenv('RABBIT_USERNAME'), password=os.getenv('RABBIT_PASSWORD'))
        params = pika.ConnectionParameters(os.getenv('RABBIT_HOST'),credentials=credentials)
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=os.getenv('RABBIT_QUEUE'))
        self.channel.exchange_declare(exchange='the_famous_fanout', exchange_type='fanout')
        self.channel.queue_declare(queue="monitaz_ifollow_tele", durable=True)
        self.channel.queue_declare(queue="monitaz_ifollow_banking", durable=True)
        self.channel.queue_declare(queue='monitaz_ifollow_check', durable=True)
        
        self.channel.queue_bind(exchange='the_famous_fanout', queue="monitaz_ifollow_tele")
        self.channel.queue_bind(exchange='the_famous_fanout', queue="monitaz_ifollow_banking")



        self.filter_host = os.getenv('FILTER_HOST')
        self.filter_port = os.getenv('FILTER_PORT')
        self.filter_url = "http://"+self.filter_host+":"+ str(self.filter_port) 

        self.redis_db = redis.Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'), db=os.getenv('REDIS_DB_ID'))


    def mysqConnect(self):
        self.conn = mysql.connector.connect(user=os.getenv('MYSQL_USERNAME'),
                                    passwd=os.getenv('MYSQL_PASSWD'),
                                    db=os.getenv('MYSQL_DB'),
                                    host=os.getenv('MYSQL_HOST'),
                                    charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def insertDatabase(self, sql, params=()):
        try:
            self.mysqConnect()
            cursor = self.conn.cursor()
            cursor.execute(sql, params)
            self.conn.commit()
        except (AttributeError, mysql.connector.OperationalError) as e:
            print ('exception generated during sql connection: ', e)
            self.mysqConnect()
            cursor = self.conn.cursor()
            cursor.execute(sql, params)
        return cursor.lastrowid

        def process_item(self, item, spider):
        print("==== DEBUG PIPELINE ====")

        web_link = item.get("web_link", "")
        if isinstance(web_link, bytes):
            web_link = web_link.decode("utf-8")

        web_domain_name = item.get("web_domain_name", "")
        if isinstance(web_domain_name, bytes):
            web_domain_name = web_domain_name.decode("utf-8")

        web_title = item.get("web_title", "")
        if isinstance(web_title, bytes):
            web_title = web_title.decode("utf-8")

        if item.get('web_url_comment') == "DEBUG":
            string = f"{web_link}_{web_domain_name}"
            print(string)
            key_insert = hashlib.md5(string.encode('utf-8')).hexdigest()
            print(key_insert)

            item_dict = dict(item)
            item_dict['web_key'] = key_insert

            # FIX: convert bytes to string
            for k, v in item_dict.items():
                if isinstance(v, bytes):
                    try:
                        item_dict[k] = v.decode('utf-8')
                    except Exception:
                        item_dict[k] = str(v)

            try:
                json_string = json.dumps(item_dict)
                self.channel.basic_publish(exchange='',
                                           routing_key='monitaz_ifollow_check',
                                           body=json_string)
                print("DEBUG message sent to RabbitMQ.")
            except Exception as e:
                print("[DEBUG ERROR] Unable to publish DEBUG item to RabbitMQ:", e)

            print("====== SUCCESSFUL DEBUG PROCESS ======")

        print("========================")

        # Strip content
        item['web_content'] = item.get('web_content', '').strip()
        if item['web_content'] == "":
            self._set_raw_null(web_link, web_domain_name, str(item.get("web_category_url", "")), str(self.now))
            print("===========================")
            print("[XPATHS EXCEPTION] EMPTY CONTENT")
            print(web_link)
            print("===========================")
            if issubclass(spider.__class__, BaseSpider):
                spider.empty_contents.append(web_link)
            return None

        to_return = False
        string = f"{web_link}_{web_domain_name}"
        key_insert = hashlib.md5(string.encode('utf-8')).hexdigest()
        print("[INFO] KEY 1:", key_insert)

        string_http = web_link.replace("www.", "").replace("http://", "https://") + "_" + web_domain_name
        key_hash_http = hashlib.md5(string_http.encode('utf-8')).hexdigest()
        print("[INFO] KEY 2:", key_hash_http)

        string_https = web_link.replace("www.", "").replace("http://", "https://") + "_" + web_domain_name
        key_hash_https = hashlib.md5(string_https.encode('utf-8')).hexdigest()
        print("[INFO] KEY 3:", key_hash_https)

        string_www = web_link.replace("https://", "https://www.").replace("http://","http://www.") + "_" + web_domain_name
        key_hash_www = hashlib.md5(string_www.encode('utf-8')).hexdigest()
        print("[INFO] KEY 4:", key_hash_www)

        duplicate = self.redis_exists(key_insert)
        duplicate_http = self.redis_exists(key_hash_http)
        duplicate_https = self.redis_exists(key_hash_https)
        duplicate_www = self.redis_exists(key_hash_www)
        print("[DEBUG] Redis is using DB:", self.redis_db.connection_pool.connection_kwargs.get("db"))

        if duplicate or duplicate_http or duplicate_https or duplicate_www:
            print("[INFO] ITEM ALREADY EXISTS")
            print("[INFO] THE KEY:", key_insert)
            print("[INFO] THE WEB LINK:", web_link)
            print("[INFO] STRING KEY:", string)
        else:
            to_return = True
            try:
                item_dict = dict(item)
                item_dict['web_key'] = key_insert

                # FIX: convert bytes to string
                for k, v in item_dict.items():
                    if isinstance(v, bytes):
                        try:
                            item_dict[k] = v.decode('utf-8')
                        except Exception:
                            item_dict[k] = str(v)

                res = self.es.index(index=os.getenv('ES_INDEX'), id=key_insert, body=item_dict)

                try:
                    json_string = json.dumps(item_dict)
                    self.channel.basic_publish(exchange='the_famous_fanout', routing_key='', body=json_string)
                    print("Message sent to RabbitMQ successfully.")
                except Exception as e:
                    print("[RABBITMQ ERROR] Failed to publish to RabbitMQ:", e)

                self.insert_key_to_redis(key_insert)
                print("Key inserted into Redis.")

            except Exception as e:
                print("[EXCEPTION] ERROR INSERTING TO DBS")
                print("[EXCEPTION DETAIL]", str(e))

        if issubclass(spider.__class__, BaseSpider):
            spider.visiting_urls.append(web_link)
            spider.to_update_urls.append(web_link)
            spider.item_count += 1

        if to_return:
            return item

    def get_update_data(self, item):
        update_data = {}
        update_fields = self._get_base_update_field()

        if item['web_post_type'] == 0:
            update_fields['web_is_crawled'] = 'web_is_crawled'
        elif item['web_post_type'] == 1:
            update_fields['web_is_crawled'] = 'web_is_crawled'

        for field in update_fields.itervalues():
            update_data[field] = item[field]

        return update_data

    def _get_base_update_field(self):
        return self.update_fields

    def _set_raw(self, web_key, data):
        sql = """INSERT INTO web_raw(web_key, web_data, web_link, web_domain, web_domain_id, crawled_time) VALUE (%s, %s, %s, %s, %s,%s)"""
        try:
            curr = self.cursor.execute(sql,(web_key, json.dumps(data.__dict__), data["web_link"].encode("utf-8"), data["web_domain_name"], data["web_domain_id"],str(self.now)))
            self.conn.commit()
        except Exception as e:
            print ("[EXCEPTION] exception in set raw")
            print (e)

    def _set_raw_null(self, web_link, web_domain, category_url, time):
        sql = """INSERT INTO web_null(web_link, web_domain, category_url, crawled_at) VALUE (%s, %s, %s, %s)"""
        # print sql
        try:
            self.cursor.execute(sql,(web_link, web_domain,category_url,time))
        except Exception as e:
            print ("[EXCEPTION] exception in insert raw null")
            print('err: ', e)
        self.conn.commit()

    def close_spider(self,spider):
        print ("COMMIT LAST BATCH!")
        try:
            # self.batch.commit()
            self.conn.close()
        except Exception as e:
            print('err: ', e)
            pass            


    def redis_exists(self,key):
        # check_duplicate = self.es.exists(index=settings['ES_INDEX'], doc_type=settings['ES_TYPE'], id=key)
        # return check_duplicate
        val = self.redis_db.get(key)
        if val == "exist":
            return True
        return False

    def insert_key_to_redis(self, key):
        self.redis_db.set(key,"exist")


    def exists(self,key):
        #return true if record exists in hbase
        #return false if record is not 
        ret = urllib.request.urlopen(self.filter_url+ "/key/"+str(key)).read()
        if "True" in ret:
            print ("Key exists in filter: " + key)
            return True
        return False

    def insert_key_to_filter(self, key):
        #insert the key into the filter
        try:
            r = requests.post(self.filter_url + "/key/"+str(key))
            print ("Key inserted into filter: " + key)
        except Exception:
            print ("CANT CONNECT TO FILTER HOSTS AT "+ self.filter_url)

    def sendTelegram(self, web_category_name, web_category_url, web_link):
        bot_token = '1660557788:AAFgvelfDIIac1LRA4h7wsyuj4OVOgSmp9w'
        bot_chatID = '-595233542'
        bot_message = " \n DateNow: "+str(datetime.now())+" \n Cate Name: "+str(web_category_name)+" \n Cate Url: "+str(web_category_url)+" \n Link: "+str(web_link)+" \n --------------------------------------------------------------------"
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&text=' + bot_message
        response = requests.get(send_text)

        print ('[Website Notification] --------- Send Telegram Success!')
