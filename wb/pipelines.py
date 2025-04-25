# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import configparser
# from scrapy import settings
from scrapy.utils.project import get_project_settings
# import MySQLdb
import mysql.connector
from elasticsearch import Elasticsearch
import hashlib
import json
from datetime import datetime 
from wb.spiders.base_spider import BaseSpider
import urllib.request
import requests
import pika
import redis
import os
from dotenv import load_dotenv

load_dotenv()


class BloomFilterPipeline(object):
    def __init__(self):

        self.filter_host = os.getenv('FILTER_HOST')
        self.filter_port = os.getenv('FILTER_PORT')
        self.filter_url = "http://"+self.filter_host+":"+ str(self.filter_port)

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


    def process_item(self, item,spider):
        key_insert = item['fb_post_id']
        duplicate = self.exists(key_insert)
        if duplicate == True:
            print ("ITEM EXISTED " + item['fb_post_id'])
        else:
            return item


class WbPipeline(object):
    def __init__(self):
        settings = get_project_settings()

        config = configparser.ConfigParser()
        config.read(settings.get('EXTRA_CONFIG_FILE'))
        self.extra_config = config
        self.update_fields = {
            'web_content': 'web_content',
            'web_like_count': 'web_like_count',
            'web_crawler_time': 'web_crawler_time'
        }
        # c = Connection(host=settings['HBASE_MASTER'],port=settings['HBASE_PORT'])
        # self.table = c.table(settings['HBASE_TABLE'])
        self.es = Elasticsearch([{'host': os.getenv('ES_HOST'), 'port': int(os.getenv('ES_PORT')), 'scheme': 'http'}])
        # self.batch = self.table.batch(fail_silently=False)
        # self.batch_count = 0
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

    def safe_decode(val):
        return val.decode("utf-8") if isinstance(val, bytes) else val

    # def process_item(self, item, spider):
    #     print ("==== DEBUG PIPELINE ====")
    #     if item['web_url_comment'] == "DEBUG":
    #         string = str(item["web_link"]) + "_" + str(item['web_domain_name'])
    #         print (string)
    #         key_insert = hashlib.md5(str(string).decode('utf-8').encode('utf-8')).hexdigest()
    #         print (key_insert)
    #         item_dict = dict(item)
    #         item_dict['web_key'] = key_insert
    #         json_string = json.dumps(item_dict)
    #         self.channel.basic_publish(exchange='',
    #                           routing_key='monitaz_ifollow_check',
    #                           body=json_string)
    #
    #         print ("====== SUCCESSED PY======")
    #     print ("========================")
    #
    #     item['web_content'] = item['web_content'].strip()
    #     if item['web_content'] == "":
    #         self._set_raw_null(str(item["web_link"]), str(item["web_domain_name"]), str(item["web_category_url"]), str(self.now) )
    #         print ("===========================")
    #         print ("[XPATHS EXCEPTION] EMPTY CONTENT")
    #         print  (item['web_link'])
    #         print ("===========================")
    #         if issubclass(spider.__class__, BaseSpider ):
    #             spider.empty_contents.append(item['web_link'])
    #         return None
    #     else:
    #         to_return = False
    #         string = str(item["web_link"]) + "_" + str(item['web_domain_name'])
    #         key_insert = hashlib.md5(str(string).encode('utf-8')).hexdigest()
    #         print ("[INFO] KEY 1: "+ key_insert)
    #         #Key Hash
    #         # string_http = str(item["web_link"].replace("www.","").replace("https://","http://")) + "_" + str(item['web_domain_name'])
    #         web_link = item["web_link"].decode("utf-8") if isinstance(item["web_link"], bytes) else item["web_link"]
    #         web_domain_name = item["web_domain_name"].decode("utf-8") if isinstance(item["web_domain_name"], bytes) else item["web_domain_name"]
    #
    #         string_http = web_link.replace("www.", "").replace("http://", "https://") + "_" + web_domain_name
    #         key_hash_http = hashlib.md5(str(string_http).encode('utf-8')).hexdigest()
    #         print ("[INFO] KEY 2: "+ key_hash_http)
    #
    #         # string_https = str(item["web_link"].replace("www.","").replace("http://","https://")) + "_" + str(item['web_domain_name'])
    #         string_https = web_link.replace("www.", "").replace("http://", "https://") + "_" + web_domain_name
    #         key_hash_https = hashlib.md5(str(string_https).encode('utf-8')).hexdigest()
    #         print ("[INFO] KEY 3: "+ key_hash_https)
    #
    #         string_www = web_link.replace("https://","https://www.").replace("http://","http://www.") + "_" + web_domain_name
    #         key_hash_www = hashlib.md5(str(string_www).encode('utf-8')).hexdigest()
    #         print ("[INFO] KEY 4: "+ key_hash_www)
    #
    #         # Check Duplicate
    #         duplicate = self.redis_exists(key_insert)
    #         duplicate_http = self.redis_exists(key_hash_http)
    #         duplicate_https = self.redis_exists(key_hash_https)
    #         duplicate_www = self.redis_exists(key_hash_www)
    #
    #         # duplicate_http = False
    #         # duplicate_https = False
    #         # duplicate_www = False
    #
    #         # if spider.debug == 'True':
    #         #    print "\n\n\nINSERT THE DEBUG URL INTO QUEUE AND QUEUE ONLY \n\n" + item['web_link'] + "\n\n"
    #         #    temp = dict(item)
    #         #    temp['web_key'] = key_insert
    #         #    self.channel.basic_publish(exchange='',routing_key='monitaz_ifollow_debug',body=json.dumps(dict(temp)))
    #         # IF NGÀY ĐĂNG LÀ 2021-05-03 or 2021-05-04
    #         # if '2021-05-04' in item['web_created'] or '2021-05-03' in item['web_created']:
    #         #     duplicate = False
    #         #     print "INFO =======================* 2021-05-03 or 2021-05-04 *======================="
    #
    #         # IF TRONG KHOẢNG THỜI GIAN 2021-05-11 09:00:00 ĐẾN 2021-05-11 10:30:00
    #         # dateStartAgain = '2021-05-11 09:00:00'
    #         # dateStartAgain = datetime.strptime(dateStartAgain, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
    #         # dateEndAgain = '2021-05-11 12:00:00'
    #         # dateEndAgain = datetime.strptime(dateEndAgain, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
    #         # if item['web_created'] > dateStartAgain and item['web_created'] < dateEndAgain:
    #         #     duplicate = False
    #
    #         timeWebCreate = item['web_created']
    #         timeWebCreate = datetime.strptime(timeWebCreate, "%Y-%m-%d %H:%M:%S")
    #         if timeWebCreate.year == 2022 or timeWebCreate.year == 2023 or timeWebCreate.year == 2024 or timeWebCreate.year == 2025:
    #             duplicate = False
    #         else:
    #             duplicate = True
    #
    #         if duplicate == True or duplicate_http == True or duplicate_https == True or duplicate_www == True:
    #             print ("[INFO] ITEM ALREADY EXISTS")
    #             print ("[INFO] THE KEY: " + key_insert)
    #             print ("[INFO] THE WEB LINK : " + item['web_link'])
    #             string = str(item["web_link"]) + "_" + str(item['web_domain_name'])
    #             print ("[INFO] STRING KEY: " + string)
    #         else:
    #             to_return = True
    #             try:
    #                 # if self.batch:
    #                 #     self.batch.insert(key_insert, {"ifollow": dict(item)})
    #                 #     self.batch_count +=1
    #                 #     if (self.batch_count) == 100:
    #
    #                 #         self.batch.commit(finalize=True)
    #                 #         self.batch_count  = 0
    #                 #         self.batch = self.table.batch(fail_silently=False)
    #
    #                 # else:
    #                 #     self.batch = self.table.batch(fail_silently=False)
    #                 item_dict = dict(item)
    #                 # self.table.insert(key_insert, {"ifollow": item_dict})
    #                 res = self.es.index(index=os.getenv('ES_INDEX'), doc_type=os.getenv('ES_TYPE'), id=key_insert, body=item_dict)
    #                 # self._set_raw(key_insert, item)
    #
    #                 item_dict['web_key'] = key_insert
    #                 json_string = json.dumps(item_dict)
    #                 self.channel.basic_publish(exchange='the_famous_fanout',
    #                               routing_key='',
    #                               body=json_string)
    #                 # self.channel2.basic_publish(exchange='the_famous_fanout',
    #                 #               routing_key='',
    #                 #               body=json_string)
    #                 self.insert_key_to_redis(key_insert)
    #                 print ("bước 3.1==================================================================")
    #                 # CHECK DATETIME
    #                 web_crawl_v2 = datetime.fromtimestamp(item_dict['web_crawler_time']).strftime('%Y-%m-%d %H:%M:%S')
    #                 arrDomainSkip = ["baonhanh247.com"]
    #                 if (str(web_crawl_v2) == str(item_dict['web_created'])) and item_dict['web_domain_name'] not in arrDomainSkip :
    #                     # self.sendTelegram(item_dict['web_category_name'], item_dict['web_category_url'], item_dict['web_link'])
    #                     filename = "datetime_debug.txt"
    #                     text_line = "URL: "+item_dict['web_domain_name'] + "  --  SERVER: 221 \n"
    #                     open(filename, 'a+').write(text_line)
    #             except Exception as e:
    #                 print ("[EXCEPTION] ERROR INSERTING TO DBS")
    #                 print (e)
    #
    #
    #
    #         if issubclass(spider.__class__, BaseSpider ):
    #             spider.visiting_urls.append(item['web_link'])
    #             spider.to_update_urls.append(item['web_link'])
    #             spider.item_count = spider.item_count +1
    #         if to_return == True:
    #             return item

    def process_item(self, item, spider):
        print("==== DEBUG PIPELINE ====")

        if item['web_url_comment'] == "DEBUG":
            string = str(item["web_link"]) + "_" + str(item['web_domain_name'])
            print(string)
            key_insert = hashlib.md5(string.encode('utf-8')).hexdigest()
            print(key_insert)

            item_dict = dict(item)
            item_dict['web_key'] = key_insert
            try:
                json_string = json.dumps(item_dict)
                self.channel.basic_publish(exchange='',
                                           routing_key='monitaz_ifollow_check',
                                           body=json_string)
            except Exception as e:
                print("[DEBUG ERROR] Unable to publish DEBUG item to RabbitMQ:", e)

            print("====== SUCCESSED PY======")

        print("========================")

        item['web_content'] = item['web_content'].strip()
        if item['web_content'] == "":
            self._set_raw_null(str(item["web_link"]), str(item["web_domain_name"]), str(item["web_category_url"]),
                               str(self.now))
            print("===========================")
            print("[XPATHS EXCEPTION] EMPTY CONTENT")
            print(item['web_link'])
            print("===========================")
            if issubclass(spider.__class__, BaseSpider):
                spider.empty_contents.append(item['web_link'])
            return None

        to_return = False
        string = str(item["web_link"]) + "_" + str(item['web_domain_name'])
        key_insert = hashlib.md5(string.encode('utf-8')).hexdigest()
        print("[INFO] KEY 1:", key_insert)

        web_link = item["web_link"].decode("utf-8") if isinstance(item["web_link"], bytes) else item["web_link"]
        web_domain_name = item["web_domain_name"].decode("utf-8") if isinstance(item["web_domain_name"], bytes) else \
        item["web_domain_name"]

        string_http = web_link.replace("www.", "").replace("http://", "https://") + "_" + web_domain_name
        key_hash_http = hashlib.md5(string_http.encode('utf-8')).hexdigest()
        print("[INFO] KEY 2:", key_hash_http)

        string_https = web_link.replace("www.", "").replace("http://", "https://") + "_" + web_domain_name
        key_hash_https = hashlib.md5(string_https.encode('utf-8')).hexdigest()
        print("[INFO] KEY 3:", key_hash_https)

        string_www = web_link.replace("https://", "https://www.").replace("http://",
                                                                          "http://www.") + "_" + web_domain_name
        key_hash_www = hashlib.md5(string_www.encode('utf-8')).hexdigest()
        print("[INFO] KEY 4:", key_hash_www)

        duplicate = self.redis_exists(key_insert)
        duplicate_http = self.redis_exists(key_hash_http)
        duplicate_https = self.redis_exists(key_hash_https)
        duplicate_www = self.redis_exists(key_hash_www)

        timeWebCreate = datetime.strptime(item['web_created'], "%Y-%m-%d %H:%M:%S")
        if timeWebCreate.year in [2022, 2023, 2024, 2025]:
            duplicate = False
        else:
            duplicate = True

        if duplicate or duplicate_http or duplicate_https or duplicate_www:
            print("[INFO] ITEM ALREADY EXISTS")
            print("[INFO] THE KEY:", key_insert)
            print("[INFO] THE WEB LINK:", item['web_link'])
            print("[INFO] STRING KEY:", string)
        else:
            to_return = True
            try:
                item_dict = dict(item)
                # Bỏ doc_type (Elasticsearch 7+ không dùng nữa)
                res = self.es.index(index=os.getenv('ES_INDEX'), id=key_insert, body=item_dict)

                item_dict['web_key'] = key_insert
                try:
                    json_string = json.dumps(item_dict)
                    self.channel.basic_publish(exchange='the_famous_fanout', routing_key='', body=json_string)
                except Exception as e:
                    print("[RABBITMQ ERROR] Failed to publish to RabbitMQ:", e)

                self.insert_key_to_redis(key_insert)
                print("bước 3.1==================================================================")

                web_crawl_v2 = datetime.fromtimestamp(item_dict['web_crawler_time']).strftime('%Y-%m-%d %H:%M:%S')
                arrDomainSkip = ["baonhanh247.com"]
                if (web_crawl_v2 == item_dict['web_created']) and item_dict['web_domain_name'] not in arrDomainSkip:
                    filename = "datetime_debug.txt"
                    text_line = "URL: " + item_dict['web_domain_name'] + "  --  SERVER: 221 \n"
                    open(filename, 'a+').write(text_line)
            except Exception as e:
                print("[EXCEPTION] ERROR INSERTING TO DBS")
                print(str(e))

        if issubclass(spider.__class__, BaseSpider):
            spider.visiting_urls.append(item['web_link'])
            spider.to_update_urls.append(item['web_link'])
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