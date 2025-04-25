# -*- coding: utf-8 -*-

__author__ = 'VuongNM'

import os, time, scrapy, mysql.connector, logging, re, hashlib, redis, requests, configparser

from .helper import Helper
from scrapy.utils.project import get_project_settings
from .dispatcherLib import DispatcherLibrary
from pydispatch import dispatcher
from scrapy.http import Request
from scrapy.selector import Selector
from urllib.parse import urlparse
from scrapy import signals
from datetime import datetime
from unidecode import unidecode
from dotenv import load_dotenv

load_dotenv()

class BaseSpider(scrapy.Spider):
    group = None
    visited_urls = []
    visited_datetimes = []
    visiting_urls = []
    to_update_urls = []
    empty_cates = [] # return  no urls
    deleted_cates = [] # 404 error
    empty_contents = []
    visiting_cates = []
    media_urls = []
    media_url_inserts = []
    media_datetime_inserts = []
    seen_urls = []
    item_count = 0
    url_count = 0
    handle_httpstatus_list = [403, 404]
    name = "base"
    service_id = 0
    allowed_domains = ["example.com"]
    url_get_like = "http://api.facebook.com/restserver.php?method=links.getStats&urls={article_url}"
    custom_settings = {
        "CLOSESPIDER_TIMEOUT": 120,
    }

    def __init__(self, service_id=None,group=None, url= None, cate = None, debug=None, debug_scrape=None, debug_filtered=None, debug_again=None, *args, **kwargs):

        settings = get_project_settings()

        parse_cfg = configparser.ConfigParser()
        parse_cfg.read(settings.get('PARSER_CONFIG_FILE'))
        self.parse_cfg = parse_cfg

        if(group == None):
            self.group = "GR1"
        else:
            self.group = group

        self.crawl_one_url = url
        self.crawl_one_cate = cate
        self.debug= debug
        self.is_debug_scrape = debug_scrape
        self.is_debug_filtered = debug_filtered
        self.is_debug_again = debug_again

        logging.info( '[INFO] Init connection mysql' )
        print ('[INFO] Init connection mysql')
        self.monitaz_conn = mysql.connector.connect(user=os.getenv('MYSQL_USERNAME'),
                                    passwd=os.getenv('MYSQL_PASSWD'),
                                    db=os.getenv('MYSQL_MONITAZ_DB'),
                                    host=os.getenv('MYSQL_HOST'),
                                    charset="utf8", use_unicode=True)
        self.monitaz_cursor= self.monitaz_conn.cursor()

        self.core_conn = mysql.connector.connect(user=os.getenv('MYSQL_USERNAME'),
                                    passwd=os.getenv('MYSQL_PASSWD'),
                                    db=os.getenv('MYSQL_DB'),
                                    host=os.getenv('MYSQL_HOST'),
                                    charset="utf8", use_unicode=True)
        self.core_cursor= self.core_conn.cursor()

        self.filterdb_conn = mysql.connector.connect(user=os.getenv('MYSQL_USERNAME'),
                                    passwd=os.getenv('MYSQL_PASSWD'),
                                    db=os.getenv('MYSQL_TOFILTER_DB'),
                                    host=os.getenv('MYSQL_HOST'),
                                    charset="utf8", use_unicode=True)
        self.filter_cursor = self.filterdb_conn.cursor()

        self.mediadb_conn = mysql.connector.connect(user=os.getenv('MYSQL_USERNAME'),
                                    passwd=os.getenv('MYSQL_PASSWD'),
                                    db=os.getenv('MYSQL_FILTER_MEDIA_DB'),
                                    host=os.getenv('MYSQL_HOST'),
                                    charset="utf8", use_unicode=True)
        self.mediadb_cursor = self.mediadb_conn.cursor()

        self.init_filterdb()

        self.init_mediadb()

        self.redis_db = redis.Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'), db=os.getenv('REDIS_DB_ID'))

        self.url_category_first = ''
        
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        dispatcher.connect(self.spider_opened, signals.spider_opened)

    def start_requests(self):

        print ("===")
        print ("BEGIN CRAWLER WEBSITE " + self.allowed_domains[0])
        print ("===")

        page = 1
        cf_domain = self.allowed_domains[0]
        parser_xpath = self.get_xpaths()
        # parser_xpath = self.get_xpaths_mysql()
        # if parser_xpath:
        #     print "[INFO] GET XPATH IN DB"
        # else:
        #     print "[INFO] GET XPATH IN FILE CFG"
        #     parser_xpath = self.get_xpaths()

        if parser_xpath:
            if self.crawl_one_url == None and self.crawl_one_cate == None :

                list_data = DispatcherLibrary(self.service_id, self.group).getCateUrls(cf_domain)
                if len(list_data) > 0:
                    i = 1
                    for row in list_data:
                        id, domain_url, category_name, domain_name, domain_group, status, created, pay_category = row
                        if i == 1:
                            self.url_category_first = domain_url
                            if self.url_category_first != "":
                                i += 1

                        meta = {"domain": cf_domain, "xpath_config": parser_xpath, "domain_id": id, "category_name": category_name, "category_url": domain_url, "pay": pay_category}
                        print (domain_url)
                        yield Request(domain_url,meta=meta,callback=self.parse)
                else:
                    #LOG SPIDER NOT CATEGORY
                    print ("[INFO] LOG SPIDER NOT CATEGORY")
                    filename = "logs-no-category.txt"
                    log_text = "Domain: "+ cf_domain+" --- Spider Name: "+self.name+"\n"
                    open(filename, 'a+').write(log_text)

            elif self.crawl_one_url != None and self.crawl_one_cate == None :
                meta = {
                    'post_url': self.crawl_one_url,
                    "xpath_config": parser_xpath,
                    "domain": self.allowed_domains[0],
                    "domain_id": 1,
                    "category_name": self.name,
                    "category_url": self.allowed_domains[0],
                    "pay":0
                }
                if self.crawl_one_url in self.visited_urls:
                    print ("[INFO] url exists in pre-request filter")
                else:
                    print ("[INFO] url NOT exists in pre-request filter")

                if self.is_debug_scrape != None:
                    yield Request(self.crawl_one_url, callback = self.parse_full_post_for_debug, meta=meta)
                    print (self.is_debug_scrape)
                else:
                    if self.is_debug_again != None:
                        string = str(self.crawl_one_url.encode('utf-8')) + "_" + str(self.allowed_domains[0])
                        key_insert = hashlib.md5(str(string).encode('utf-8')).hexdigest()
                        duplicate = self.redis_exists(key_insert)
                        if duplicate == True:
                            print ("[INFO][DEBUG] ITEM ALREADY EXISTS DON'T REQUEST AGAIN")
                            print ("[INFO][DEBUG] THE KEY: " + key_insert)
                            self.delete_key_to_redis(key_insert)
                    yield Request(self.crawl_one_url, callback = self.parse_full_post , meta=meta)

            elif self.crawl_one_url == None and self.crawl_one_cate != None :
                while True:
                    list_data = DispatcherLibrary(self.service_id, self.group).getUrlLeech(cf_domain, self.group, page)
                    if len(list_data) > 0:
                        for row in list_data:
                            id, domain_url, category_name, domain_name, domain_group, status, created, pay_category = row
                            meta = {"domain": cf_domain, "xpath_config": parser_xpath, "domain_id": id, "category_name": category_name, "category_url": domain_url, "pay": pay_category}
                            if domain_url == self.crawl_one_cate:

                                print ("===")
                                print (domain_url)
                                print ("===")

                                yield Request(domain_url,meta=meta,callback=self.parse)
                    else:
                        break
                    page = page + 1
            else:
                print ("[ERROR] pass url OR cate, not both of them ")
        else:
            print ("[ERROR] GET XPATH IN DB ERROR!!! ")

    def parse(self, response):
        # if response.meta["domain"] == "sbv.gov.vn":
        #     print "===="
        #     print "HEHE"
        #     print "===="
        #     filename = "response_debug1.html"
        #     open(filename, 'wb').write(response.body)

        post_urls = response.selector.xpath(response.meta['xpath_config']['post_url']).extract()
        # COUNT URL
        self.url_count += len(post_urls)
        print ("[INFO] COUNT URL: "+str(self.url_count))
        if len(post_urls) == 0 and response.status == 200:
            self.empty_cates.append( (self.allowed_domains[0], response.meta['category_url']))
        if response.status == 404:
            print ("[ERROR] 404 cate : " + response.url)
            self.deleted_cates.append( (self.allowed_domains[0],response.meta['category_url']))

        self.visiting_cates.append((self.allowed_domains[0], response.meta['domain_id'],response.meta['category_url'], str(datetime.now())))

        cate_seen_urls = []
        domain = self.getDomainFromURL(response.url)

        # CUSTOM URL
        info_domain = urlparse(response.url)
        scheme = info_domain.scheme

        for post_url in post_urls:
            # info_post_url  = urlparse(post_url)
            # scheme = info_post_url.scheme
            meta_req = response.meta
            if (not post_url.startswith("http://") ) and (not post_url.startswith("https://")):
                if not post_url.startswith("/"):
                    post_url = "/" + post_url
                # post_url = "http://"+domain+post_url
                post_url = scheme + "://" + domain + post_url

            meta_req['post_url'] = post_url

            if post_url not in self.visited_urls:
                if post_url not in self.media_urls:
                    # if meta_req["domain"] == "nongnghiep.vn":
                    #     meta_req['domain'] = meta_req['domain'].replace("‘", "")

                    string = str(post_url.encode('utf-8')) + "_" + str(meta_req['domain'])
                    key_insert = hashlib.md5(str(string).encode('utf-8')).hexdigest()
                    # print "==================================="
                    # print post_url
                    # print key_insert
                    # print "==================================="

                    duplicate = self.redis_exists(key_insert)

                    # IF NGÀY ĐĂNG LÀ 2021-05-03 or 2021-05-04 
                    # duplicate = False

                    if duplicate == True:
                        print ("[INFO] ITEM ALREADY EXISTS DON'T REQUEST AGAIN")
                        print ("[INFO] THE KEY: " + key_insert)
                        print ("[INFO] THE WEB LINK : " + str(post_url.encode("utf-8")))
                    else:
                        # print "============= REQUEST TRUE ============="
                        # print post_url
                        # print "=========================================="
                        yield Request(post_url, callback=self.parse_full_post, meta=meta_req)
                else:
                    # print "============== FILTER MEDIA =============="
                    # print post_url
                    # print "=========================================="
                    logging.info( "[FILTER MEDIA] request filtered " + post_url)
            else:
                # print "============== FILTER REQUEST =============="
                # print post_url
                # print "============================================"
                logging.info( "[FILTER] request filtered " + post_url)
                self.to_update_urls.append(post_url)

            cate_seen_urls.append(post_url)
        self.seen_urls.append((response.meta['domain_id'],response.meta['category_name'],cate_seen_urls))

    def get_like(self, url):
        return {"total_like": 0, "total_comment": 0, "total_share": 0}

    def parse_full_post(self, response):

        print ("============== PARSE REQUEST ==============")
        print (str(response.url))
        print ("============================================")

        if response.status != 200:
            print ("SERVER ERROR ON THIS URL: "+ str(response.url) )
            return

        # if response.meta["domain"] == "baomoi.com":
        #     print "===="
        #     print "HEHE"
        #     print "===="
        #     filename = "response_debug_baomoi.html"
        #     open(filename, 'wb').write(response.body)

        # filename = "response_debug1.html"
        # open(filename, 'wb').write(response.body)

        item = Helper().getItem()
        article_url = str(response.meta['post_url'].strip().encode('utf-8'))
        url = self.url_get_like.format(article_url=article_url)
        data_shares = self.get_like(url)
        item['web_parent_id'] = 0
        item['web_grand_parent_id'] = 0
        item['web_cid'] = 0
        item['web_id'] = 0
        try:
            web_title = ''
            for i in response.selector.xpath(response.meta['xpath_config']['post_title']).extract():
                web_title  = web_title + i.strip()
            item['web_title'] = web_title.encode('utf-8')
        except Exception:
            item['web_title']    = ""

        extracted_desc = response.selector.xpath(response.meta['xpath_config']['post_intro']).extract()
        if len(extracted_desc) > 0:
            item['web_lead'] = extracted_desc[0].strip().encode('utf-8')
        else:
            item['web_lead'] = item['web_title']

        # print response.meta['xpath_config']['post_content']
        # item['web_content'] = Helper()._join_data(" ", response.selector.xpath(response.meta['xpath_config']['post_content']).extract()).replace(r" +", " ").strip().encode('utf-8').replace(" "," ")
        # item['web_author'] = Helper()._join_data(",", response.selector.xpath(response.meta['xpath_config']['post_author']).extract()).strip().encode('utf-8')
        raw_content = Helper()._join_data(" ", response.selector.xpath(response.meta['xpath_config']['post_content']).extract())
        cleaned_content = re.sub(r" +", " ", raw_content).replace(" ", " ").strip()
        item['web_content'] = cleaned_content.encode('utf-8')
        raw_author = Helper()._join_data(",", response.selector.xpath(response.meta['xpath_config']['post_author']).extract())
        item['web_author'] = raw_author.replace(" ", " ").strip().encode('utf-8')
        item['web_author_link'] = ""
        img_link = response.selector.xpath(response.meta['xpath_config']['post_content_image']).extract()
        if len(img_link) > 0:
            item['web_image'] = img_link[0].strip().encode('utf-8')
        else:
            item['web_image'] = ""
        item['web_category_name'] = response.meta['category_name'].strip().encode("utf-8")
        item['web_category_url'] = response.meta['category_url'].strip().encode('utf-8')
        # get like count
        item['web_like_count'] = data_shares["total_like"]
        item['web_share_count'] = data_shares["total_share"]
        item['web_child_count'] = data_shares["total_comment"]
        item['web_url_comment'] = ""

        item['web_link'] = response.meta['post_url'].strip().encode('utf-8')
        item['web_domain_id'] = response.meta['domain_id']
        item['web_domain_name'] = response.meta['domain']
        #web_post_type: 0 is post, 1 is comment, 2 is reply
        item['web_post_type'] = 0
        item['web_branch'] = ""
        item['web_sub_branch'] = ""
        item['web_is_crawled'] = 0
        item['web_crawler_time'] = int(time.time())
        extracted_datetime = response.selector.xpath(response.meta['xpath_config']['post_created_at']).extract()
        print (extracted_datetime)
        if len(extracted_datetime) > 0:
            if len(extracted_datetime) > 1:
                joined = Helper()._join_data("",extracted_datetime)
                item['web_created'] = self.format_datetime(joined)
            elif len(extracted_datetime) ==1: 
                item['web_created'] = self.format_datetime(extracted_datetime[0])
        else:
            item['web_created'] = self.format_datetime("")

        item['web_tag'] = Helper()._join_data(",", response.selector.xpath(response.meta['xpath_config']['post_tags']).extract()).strip().encode('utf-8')
        item['web_group'] = self.group
        item['web_type'] = 0
        item['web_price'] = self.article_price(item,response.meta["pay"])

        print ("[PARSED DATETIME]: ", item['web_created'])
        print ('[PARSED WEBTITLE]: ', item['web_title'] )
        if self.crawl_one_url != None:
            print ("[PARSED CONTENT] ---------------------------------------")
            print (item['web_content'])
            print ("---------------------------------------")
        if (item['web_content'] == ""):
            if ('video' in response.url):
                self.media_url_inserts.append(response.meta['post_url'])
                self.media_datetime_inserts.append(str(datetime.now()))
            elif(len(response.xpath('.//iframe[(contains(@src,"youtube") or contains(@src,"vimeo")) and (not(contains(@src,"subscribe_embed")))]')) > 0):
                self.media_url_inserts.append(response.meta['post_url'])
                self.media_datetime_inserts.append(str(datetime.now()))
            elif(len(response.xpath('.//video')) > 0):
                self.media_url_inserts.append(response.meta['post_url'])
                self.media_datetime_inserts.append(str(datetime.now()))
        yield item

    def crawl_log_run_spider_count(self):
        now = datetime.now()
        now_format = now.strftime('%Y/%m/%d %H:%M:%S')
        print (now_format)
        print ("[INFO] UPDATE LOG RUN CRAWLER")
        sql = """ INSERT INTO crawl_logs (spider_name, domain_name, count_crawler, last_time_crawler, first_time_crawler) VALUES ("%s", "%s", %s, "%s", "%s") ON DUPLICATE KEY UPDATE count_crawler=count_crawler+1"""
        sql = sql % (self.name, self.allowed_domains[0], 1, now_format, now_format)
        self.core_cursor.execute(sql)
        self.core_conn.commit()

    def parse_full_post_for_debug(self, response):
        filename = "response_debug.html"
        open(filename, 'wb').write(response.body)

        if response.status != 200:
            print ("SERVER ERROR ON THIS URL: "+ str(response.url))
            return

        item = Helper().getItem()
        article_url = str(response.meta['post_url'].strip().encode('utf-8'))
        url = self.url_get_like.format(article_url=article_url)
        data_shares = self.get_like(url)
        item['web_parent_id'] = 0
        item['web_grand_parent_id'] = 0
        item['web_cid'] = 0
        item['web_id'] = 0
        try:
            web_title = ''
            for i in response.selector.xpath(response.meta['xpath_config']['post_title']).extract():
                web_title  = web_title + i.strip()
            item['web_title'] = web_title.encode('utf-8')
        except Exception:
            item['web_title']    = ""
        extracted_desc = response.selector.xpath(response.meta['xpath_config']['post_intro']).extract()
        if len(extracted_desc) > 0:
            item['web_lead'] = extracted_desc[0].strip().encode('utf-8')
        else:
            item['web_lead'] = item['web_title']

        # print "==============================="
        # print response.selector.xpath(response.meta['xpath_config']['post_content']).extract()
        # print "==============================="
        # item['web_content'] = Helper()._join_data(" ", response.selector.xpath(response.meta['xpath_config']['post_content']).extract()).replace(r" +", " ").strip().encode('utf-8').replace(" "," ")
        raw_content = Helper()._join_data(" ", response.selector.xpath(response.meta['xpath_config']['post_content']).extract())
        cleaned_content = re.sub(r" +", " ", raw_content).replace(" ", " ").strip()
        item['web_content'] = cleaned_content.encode('utf-8')
        raw_author = Helper()._join_data(",", response.selector.xpath(response.meta['xpath_config']['post_author']).extract())
        item['web_author'] = raw_author.replace(" ", " ").strip().encode('utf-8')
        item['web_author_link'] = ""
        img_link = response.selector.xpath(response.meta['xpath_config']['post_content_image']).extract()
        if len(img_link) > 0:
            item['web_image'] = img_link[0].strip().encode('utf-8')
        else:
            item['web_image'] = ""
        item['web_category_name'] = response.meta['category_name'].strip().encode("utf-8")
        item['web_category_url'] = response.meta['category_url'].strip().encode('utf-8')
        # get like count
        item['web_like_count'] = data_shares["total_like"]
        item['web_share_count'] = data_shares["total_share"]
        item['web_child_count'] = data_shares["total_comment"]
        if self.is_debug_filtered != None:
            item['web_url_comment'] = "DEBUG"
        else:
            item['web_url_comment'] = ""

        item['web_link'] = response.meta['post_url'].strip().encode('utf-8')
        item['web_domain_id'] = response.meta['domain_id']
        item['web_domain_name'] = response.meta['domain']
        #web_post_type: 0 is post, 1 is comment, 2 is reply
        item['web_post_type'] = 0
        item['web_branch'] = ""
        item['web_sub_branch'] = ""
        item['web_is_crawled'] = 0
        item['web_crawler_time'] = int(time.time())
        extracted_datetime = response.selector.xpath(response.meta['xpath_config']['post_created_at']).extract()
        print (extracted_datetime)
        if len(extracted_datetime) > 0:
            if len(extracted_datetime) > 1:
                joined = Helper()._join_data("",extracted_datetime)
                item['web_created'] = self.format_datetime(joined)
            elif len(extracted_datetime) ==1:
                item['web_created'] = self.format_datetime(extracted_datetime[0])
        else:
            item['web_created'] = self.format_datetime("")

        item['web_tag'] = Helper()._join_data(",", response.selector.xpath(response.meta['xpath_config']['post_tags']).extract()).strip().encode('utf-8')
        item['web_group'] = self.group
        item['web_type'] = 0
        item['web_price'] = self.article_price(item,response.meta["pay"])

        print ("[PARSED DATETIME]: ", item['web_created'])
        print('[PARSED WEBTITLE]:', item['web_title'])

        print ("[PARSED CONTENT] ---------------------------------------")
        print (item['web_content'])
        print (item['web_url_comment'])
        print ("===")
        print (self.is_debug_filtered)
        print ("===")
        print ("---------------------------------------")

        if self.is_debug_filtered != None:
            yield item

        # if (item['web_content'] == ""):
        #     if ('video' in response.url):
        #         self.media_url_inserts.append(response.meta['post_url'])
        #         self.media_datetime_inserts.append(str(datetime.now()))
        #     elif(len(response.xpath('.//iframe[(contains(@src,"youtube") or contains(@src,"vimeo")) and (not(contains(@src,"subscribe_embed")))]')) > 0):
        #         self.media_url_inserts.append(response.meta['post_url'])
        #         self.media_datetime_inserts.append(str(datetime.now()))
        #     elif(len(response.xpath('.//video')) > 0):
        #         self.media_url_inserts.append(response.meta['post_url'])
        #         self.media_datetime_inserts.append(str(datetime.now()))

    def get_xpaths(self):
        cf_domain = self.allowed_domains[0]
        xpaths = {
            "post_title": self.parse_cfg.get(cf_domain, 'post_title_select'),
            "post_content": self.parse_cfg.get(cf_domain, 'post_content_select'),
            "post_created_at": self.parse_cfg.get(cf_domain, 'post_created_at_select'),
            "post_tags": self.parse_cfg.get(cf_domain, 'post_tags_select'),
            "post_author": self.parse_cfg.get(cf_domain, 'post_author_select'),
            "post_category_id": self.parse_cfg.get(cf_domain, 'post_category_id_select'),
            "post_id": self.parse_cfg.get(cf_domain, 'post_id_select'),
            "post_url": self.parse_cfg.get(cf_domain, 'post_url_select'),
            "next_page": self.parse_cfg.get(cf_domain, 'next_page_select'),
            "post_intro": self.parse_cfg.get(cf_domain, 'post_intro_select'),
            "post_content_image": self.parse_cfg.get(cf_domain, 'post_content_image_select'),
            "post_category_name": self.parse_cfg.get(cf_domain, 'post_category_name')
        }

        ret = {}
        for key, value in xpaths.items():
            if ( value == "" or value == None):
                ret[key] = "./just-a-nonsense-xpath"
            else:
                ret[key] = value

        return ret

    def insert_visiting_urls(self):
        now = datetime.now()

        for row in self.visiting_urls:
            string = row + "_" + str(self.allowed_domains[0])
            web_key = hashlib.md5(str(string).encode('utf-8')).hexdigest()
            sql = "INSERT INTO " + self.name +  """(url,crawled_time, web_key) VALUES  ('%s','%s','%s')""" % (row,str(now), web_key)
            self.filter_cursor.execute(sql)
        self.filterdb_conn.commit()

    def update_visited_urls(self):
        print ("[FILTER] update filter to database of size " + str(len(self.to_update_urls)))
        if len(self.to_update_urls)  > 0 :
            sql = "TRUNCATE TABLE " + self.name
            self.filter_cursor.execute(sql)
            self.filterdb_conn.commit()
        new_datetime = str(datetime.now())
        # print len(self.to_update_urls)
        self.to_update_urls = list(set(self.to_update_urls))
        for row in self.to_update_urls:
            row_str = row.decode("utf-8") if isinstance(row, bytes) else row
            domain = self.allowed_domains[0]
            string = row_str + "_" + domain

            if isinstance(string, str):
                string = string.encode("utf8")
            web_key = hashlib.md5(string).hexdigest()

            if row in self.visited_urls:
                old_datetime = self.visited_datetimes[self.visited_urls.index(row)]
                sql = "INSERT INTO " + self.name + """(url,crawled_time, web_key) VALUES  ('%s','%s','%s')""" % (
                    row_str, old_datetime, web_key)
            else:
                sql = "INSERT INTO " + self.name + """(url,crawled_time, web_key) VALUES  ('%s','%s','%s')""" % (
                    row_str, new_datetime, web_key)

            try:
                self.filter_cursor.execute(sql)
            except Exception as e:
                print("[FILTER EXCEPTION] got error executing sql: " + sql)
                print("[ERROR DETAILS]", e)

        self.filterdb_conn.commit()
    
    def update_media_urls(self):
        if len(self.media_url_inserts)  > 0 :
            for key, row in enumerate(self.media_url_inserts):
                date_time = self.media_datetime_inserts[key]
                sql = "INSERT INTO " + self.name +  """(url,crawled_time) VALUES  ('%s','%s')""" % (row,date_time)
                try:
                    self.mediadb_cursor.execute(sql)
                except Exception:
                    print ("[MEDIA FILTER EXCEPTION] got error executing sql: " + sql)
            self.mediadb_conn.commit()

    def update_empty_cates(self):
        
        get_all = """SELECT domain_url FROM web_empty_cates ;"""
        self.core_cursor.execute(get_all)
        exists = map(lambda x: x[0], self.core_cursor.fetchall())

        #delete it and update latest
        del_sql = "DELETE FROM web_empty_cates WHERE domain  = \'"+ self.allowed_domains[0] +"\'"
        self.core_cursor.execute(del_sql)
        self.core_conn.commit()
        sql = """INSERT INTO web_empty_cates  (domain, domain_url) VALUES ('%s','%s') """
        for i in self.empty_cates:
            if i[1] not in exists:
                self.core_cursor.execute(sql % i)
        self.core_conn.commit()

    def stat_empty_content_ratio(self):
        print ("[STATS] Empty content count: " + str(len(self.empty_contents)))
        ratio = len(self.empty_contents) * 1.0 / (len(self.to_update_urls)+ 1)
        print ("[STATS] Empty content ratio " + str(ratio))
        sql = """ INSERT INTO web_empty_content_ratio (domain,ratio) VALUES ('%s', %s) ON DUPLICATE KEY UPDATE ratio=%s"""
        sql = sql % (self.allowed_domains[0], ratio, ratio) 
        self.core_cursor.execute(sql)
        self.core_conn.commit()

    def stat_last_crawled_time(self):
        now = datetime.now()
        sql = """ INSERT INTO web_crawling_stat (domain,last_crawled_time) VALUES ('%s', '%s') ON DUPLICATE KEY UPDATE last_crawled_time='%s'"""
        sql = sql % (self.allowed_domains[0],str(now),str(now))
        self.core_cursor.execute(sql)
        self.core_conn.commit()

    def stat_cate_last_crawled_time(self):
        print ("[INFO] UDPATE CATEGORY CRAWLED TIME")
        # sql = """INSERT INTO cate_crawling_stat (domain,domain_id, domain_url,last_crawled_time) VALUES ('%s', %s,'%s','%s') ON DUPLICATE KEY UPDATE last_crawled_time='%s' ;"""
        sql = """INSERT INTO cate_crawling_stat (domain,domain_id, domain_url,last_crawled_time) VALUES ('%s', %s,'%s','%s') ;"""
        for row in self.visiting_cates:
            to_exec = sql % (row[0],row[1],row[2],row[3])
            self.core_cursor.execute(to_exec)
        self.core_conn.commit()

    def update_404_cates(self):
        print ("[INFO] UPDATE DELETED CATES")
        get_all = """SELECT domain_url FROM web_404_cates ;"""
        self.core_cursor.execute(get_all)
        exists = map(lambda x: x[0], self.core_cursor.fetchall())
        del_sql = "DELETE FROM web_404_cates WHERE domain  = \'"+ self.allowed_domains[0] +"\'"
        self.core_cursor.execute(del_sql)
        self.core_conn.commit()

        sql = """INSERT INTO web_404_cates  (domain, domain_url) VALUES ('%s','%s') """
        for i in self.deleted_cates:
            if i[1] not in exists:
                self.core_cursor.execute(sql % i)
        self.core_conn.commit()
    
    def getDomainFromURL(self, url):
        domain_name = url.split("/")[2].strip()
        if "www" in domain_name:
            domain_name = domain_name.split('www')[1][1:];
        return domain_name

    def update_seen_urls_to_file(self):
        settings = get_project_settings()

        urls_log_dir = settings['LOG_URLS_FILE']
        for i in self.seen_urls:
            cate_id = i[0]
            cate_name =i[1]
            urls = i[2]
            now = datetime.now()
            date_str = now.strftime("%Y_%m_%d")
            today_folder = urls_log_dir +"/"+date_str
            if os.path.exists(today_folder) == False:
                os.makedirs(today_folder)

            domain_folder = today_folder + "/" + self.allowed_domains[0]
            if os.path.exists(domain_folder) == False:
                os.makedirs(domain_folder)


            run_folder = domain_folder + "/" + now.strftime("%H_%M_%S")
            if os.path.exists(run_folder) == False:
                os.makedirs(run_folder)

            filename = run_folder + "/" + str(cate_id) + "_"  + unidecode(cate_name).replace("/","_") +".txt"
            import codecs
            f = codecs.open(filename,encoding='utf-8',mode="w")
            for line in urls:
                f.write(line+"\n")
        print ("[INFO] WRITE URLS TO FILE " + urls_log_dir)
    
    def format_datetime(self,datetime_str):
        #Helper().format_bnews()
        funcName = "format_"+self.name
        datetime_formater = getattr(Helper(),funcName)
        return datetime_formater(datetime_str)

    def article_price(self, item,default_price):
        func_name = "article_price_" + self.name
        func = getattr(Helper(), func_name,None)
        if func is not None:
            price = func(item,default_price)
            return price
        else:
            return default_price
    
    def init_filterdb(self):
        sql = "SELECT * FROM  " + self.name+ " ;" 
        try:
            self.filter_cursor.execute(sql)
            rows = self.filter_cursor.fetchall()
            for row in rows:
                self.visited_urls.append(row[0])
                self.visited_datetimes.append(row[1])
        except Exception as e:
            sql = "CREATE TABLE " + self.name + "(url varchar(500), crawled_time datetime, web_key varchar(100) );"
            self.filter_cursor.execute(sql)
            self.filterdb_conn.commit()

        logging.info( "[INFO] done initing filter")
        print ("[INFO] done initing filter")
        print ("[INFO] filter size " + str(len(self.visited_datetimes)))

    def init_mediadb(self):
        sql = "SELECT url FROM  " + self.name+ " ;" 
        try:
            self.mediadb_cursor.execute(sql)
            rows = self.mediadb_cursor.fetchall()
            for row in rows:
                self.media_urls.append(row[0])
        except Exception:
            sql = "CREATE TABLE " + self.name + "(url varchar(500), crawled_time datetime);"
            self.mediadb_cursor.execute(sql)
            self.mediadb_conn.commit()

        logging.info( "[INFO] done initing filter media")
        print ("[INFO] done initing filter media")
        print ("[INFO] filter media size " + str(len(self.media_urls)))

    def spider_opened(self,spider):
        DispatcherLibrary(self.service_id, self.group).spider_open()

    def spider_closed(self, spider, reason):
        print ("[INFO] Close Spider")
        # INSERT LOG CRAWLER TO DB
        # self.crawl_log_run_spider_count()
        # INSERT XPATH TO DB
        # parser_xpath = self.get_xpaths()
        # print "URL: "+self.url_category_first
        # if self.url_category_first != '':
        #     domain_url = self.get_domain_from_URL(self.url_category_first)
        # else:
        #     domain_url = ''
        # print "DOMAIN URL: "+domain_url
        # print "[INFO] SAVE TO DB"
        # self.save_xpath_to_db(parser_xpath, domain_url)
        # INSERT XPATH TO DB

        if self.crawl_one_url == None and self.crawl_one_cate == None:
            self.update_visited_urls()
            self.update_empty_cates()
            self.update_404_cates()
            self.stat_empty_content_ratio()
            self.stat_last_crawled_time()
            self.stat_cate_last_crawled_time()
            self.update_media_urls()
            ratio = len(self.empty_contents) * 1.0 / (len(self.to_update_urls)+ 1)
            # self.sendTelegram(len(self.empty_contents), self.item_count, ratio, self.allowed_domains[0])
            # self.update_seen_urls_to_file()
        elif self.crawl_one_url == None and self.crawl_one_cate != None:
            self.update_empty_cates()
            self.update_404_cates()
            self.stat_cate_last_crawled_time()
            self.update_media_urls()
            # self.update_seen_urls_to_file()

        else:
            self.insert_visiting_urls()
            
        self.core_conn.close()
        self.filterdb_conn.close()
        DispatcherLibrary(self.service_id, self.group).spider_close(reason)
        # if(self.url_count == 0):
        #     filename = "/debug/category_debug.txt"
        #     text_line = "NAME: "+self.name+" --  URL: "+self.allowed_domains[0] + "  --  SERVER: 221 \n"
        #     open(filename, 'a+').write(text_line)
            # self.sendTelegramMessage(text_line, "-563670055")
        print ("NUMBER OF URLS: "+ str(self.url_count))
        print ("NUMBER OF NEW ITEMS: "+ str(self.item_count))
        print ("DONE!")

    def redis_exists(self,key):
        val = self.redis_db.get(key)
        if val == "exist":
            return True
        return False

    def _join_data_content(self, separator=None, data=None):
        # import requests
        # import urllib

        if(separator != None and data != None):
            if len(data) > 0:
                s = ""
                for i in range(0, len(data)):
                    document = Selector(text=data[i])

                    image = document.xpath(".//img/@src").extract()
                    # print "======="
                    # print image
                    # print "======="
                    if len(image) > 0:
                        image_src = image[0].strip()
                        try:
                            if image_src != "":
                                # GET EXTENSION
                                # extension = os.path.splitext(image_src)[1]
                                # new_image = hashlib.md5(str(title).decode('utf-8').encode('utf-8')).hexdigest()+extension

                                # print "================="
                                # print image_src
                                # print "================="

                                # DOWNLOAD IMAGE
                                # now = datetime.now()
                                # directory = '/home/data/dogspaper.com/img.news/uploads/images/' + now.strftime("%Y/%m/%d")

                                # if not os.path.exists(directory):
                                #     os.makedirs(directory)
                                # urllib.urlretrieve(image_src, directory + "/" + new_image)

                                # NEW IMAGE
                                # image_src = "https://img.dogspaper.com/images/" + now.strftime("%Y/%m/%d") + "/" +new_image

                                # print "==============="
                                # print image_src
                                # print "==============="

                                # s += u"<p style=\"text-align:center\"><img src=\"" +image_src+ u"\" class=\"img-responsive\"></p> "
                                pass
                        except Exception as f:
                            s += ""
                            print ("==================")
                            print (f)
                            print ("==================")

                    # s += u"<p>" +self._join_node(" ", document.xpath(".//text()").extract()).strip()+ u"</p> "
                    s += u"" +self._join_node(" ", document.xpath(".//text()").extract()).strip()+ u"<br> "
                return s
        return ''

    def robust_decode(self, bs):
        '''Takes a byte string as param and convert it into a unicode one.
    First tries UTF8, and fallback to Latin1 if it fails'''
        cr = None
        try:
            cr = bs.decode('utf8')
        except UnicodeDecodeError:
            cr = bs.decode('latin1')
        return cr

    def _join_node(self, separator=None, data=None):
        if(separator != None and data != None):
            if len(data) > 0:
                s = ""
                for i in range(0, len(data)):
                    s = s + separator + data[i].strip()
                s = s.replace(r" +", " ").strip()
                return s
        return ''

    def stripUnicode(self, input_str):
        input_str = str(unidecode.unidecode(input_str)).strip().replace("/"," ")
        input_str = input_str.replace("--", "-").strip()
        return input_str

    def format_image(self, title, image):
        funcName = "format_"+self.name
        image_formater = getattr(Image(),funcName)
        return image_formater(title, image)

    def sendTelegram(self, empty_item_count, new_item_count, empty_ratio, domain):
        bot_token = '1373128266:AAGLzdOlNKAx8TK31XfKzW6Od2mgemsc0Yc'
        bot_chatID = '-410137550'
        bot_message = " \n Date: "+str(datetime.now())+" \n Website: "+domain+" \n Empty item count: "+str(empty_item_count)+" \n New item count: "+str(new_item_count)+" \n Empty Ratio: "+str(empty_ratio)+" \n --------------------------------------------------------------------"
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)

        print ('[Website Notification] --------- Send Telegram Success!')

    def sendTelegramMessage(self, message, bot_chatID = "-410137550"):
        bot_token = '1373128266:AAGLzdOlNKAx8TK31XfKzW6Od2mgemsc0Yc'
        bot_message = " \n "+message+" \n --------------------------------------------------------------------"
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)

    def save_xpath_to_db(self, xpath_config, domain_url):
        print ("[INFO] SAVE XPATH TO DB ")
        
        try:
            sql = """ INSERT INTO xpaths (domain, name, type, status, xpath_title, xpath_content, xpath_post_intro, xpath_post_image, xpath_post_created_at, xpath_post_url, scrapy_name, url_test) 
                VALUES ('%s', '%s', '%s', %s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') 
                ON DUPLICATE KEY 
                UPDATE xpath_title='%s', xpath_content='%s', xpath_post_intro='%s', xpath_post_image='%s', xpath_post_created_at='%s', xpath_post_url='%s'"""
            sql = sql % (self.allowed_domains[0], domain_url, 'website', 1, xpath_config['post_title'], xpath_config['post_content'], xpath_config['post_intro'], xpath_config['post_content_image'], xpath_config['post_created_at'], xpath_config['post_url'], self.name, self.url_category_first, xpath_config['post_title'], xpath_config['post_content'], xpath_config['post_intro'], xpath_config['post_content_image'], xpath_config['post_created_at'], xpath_config['post_url'])
            # print sql
            self.monitaz_cursor.execute(sql)
            self.monitaz_conn.commit()
        except Exception as f:
            print ("[ERROR]"+str(f))
            #LOG SPIDER NOT CATEGORY
            print ("[INFO] LOG SAVE")
            filename = "logs-xpath-save-error.txt"
            log_text = "Domain: "+ self.allowed_domains[0] +" --- Spider Name: "+self.name+"--- Error: "+str(f)+ "\n" 
            open(filename, 'a+').write(log_text)
        
    def get_domain_from_URL(self, url):
        # CUSTOM URL
        info_domain = urlparse(url)
        scheme = info_domain.scheme
        if (not url.startswith("http://") ) and (not url.startswith("https://")):
            if not url.startswith("www."):
                domain_url = scheme + "://" + self.allowed_domains[0]
            else:
                domain_url = scheme + "://www." + self.allowed_domains[0]
        else:
            domain_url  = "http://"+self.allowed_domains[0]
        
        return domain_url

    def delete_key_to_redis(self, key):
        try:
            self.redis_db.delete(key)
            print ("[INFO][DEBUG] Remove Key Success")
        except Exception as e:
            print ("[INFO][ERROR] Remove Key Error: "+str(e))
