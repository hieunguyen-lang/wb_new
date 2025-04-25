# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import configparser
from scrapy import settings
# import MySQLdb
import mysql.connector
from elasticsearch import Elasticsearch
import hashlib
import json
import os
from dotenv import load_dotenv

load_dotenv()

class WbPipeline(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(settings.get('EXTRA_CONFIG_FILE'))
        self.extra_config = config
        self.update_fields = {
            'web_content': 'web_content',
            'web_like_count': 'web_like_count',
            'web_crawler_time': 'web_crawler_time'
        }
        self.es_doc_type = config.get('elasticsearch', 'doc_type')
        self.es_index = config.get('elasticsearch', 'index')
        self.es = Elasticsearch([config.get('elasticsearch', 'dns')])

        self.es_doc_type_v2 = config.get('elasticsearch_v2', 'doc_type')
        self.es_index_v2 = config.get('elasticsearch_v2', 'index')
        self.es_v2 = Elasticsearch([config.get('elasticsearch_v2', 'dns')])

    def mysqConnect(self):
        self.conn = mysql.connector.connect(user="replicate",
                                    passwd="muathuhanoi2014",
                                    db="monitaz_core",
                                    host="192.168.1.230",
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
        item['web_content'] = item['web_content'].strip()
        if item['web_content'] == "":
            self._set_raw_null(str(item["web_link"]), str(item["web_domain_name"]))
            print ("===========================")
            print ("NULL F.U.C.K THE XPATHHHHH!")
            print ("===========================")
            return False
        else:
            string = str(item["web_link"]) + "_" + str(item['web_domain_name'])
            key_insert = hashlib.md5(str(string).encode('utf-8')).hexdigest()

            duplicate = self.es_v2.exists(index=self.es_index_v2, doc_type=self.es_doc_type_v2, id=key_insert)
            if(duplicate is True):
                update_data_es = {}
                update_data_es['doc'] = self.get_update_data(item)
                #self.es.update(index=self.es_index, doc_type=self.es_doc_type, id=key_insert, body=dict(update_data_es))
                return key_insert
            else:
                # SAVE RAW TO MYSQL
                try:
                    self._set_raw(key_insert, item)
                except Exception:
                    pass
                self.es.index(index=self.es_index, doc_type=self.es_doc_type, id=key_insert, body=dict(item))

                # insert_query = """INSERT INTO web_data (web_parent_id,web_grand_parent_id,web_cid,web_id,web_title,web_lead,web_content,web_image,web_category_name,web_category_url,web_author,web_author_link,web_like_count,web_share_count,web_url_comment,web_child_count,web_link,web_domain_id,web_domain_name,web_post_type,web_branch,web_sub_branch,web_is_crawled,web_crawler_time,web_created,web_tag,web_group,web_type,is_filter_banking,is_filter_education,is_filter_tele,is_filter_leisure,is_filter_media,is_filter_cele,is_filter_service,is_filter_property,is_filter_clothing,is_filter_transport,is_filter_tourism,is_filter_building,is_filter_charity,is_filter_argi,is_filter_pharma,is_filter_fina,is_filter_food,is_filter_drink,is_filter_visual,is_filter_it,is_filter_furniture,is_filter_household,is_filter_other_1,is_filter_other_2,is_filter_other_3,is_filter_other_4,is_filter_other_5,is_filter_updated) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE web_content = %s, web_like_count = %s, web_crawler_time = %s"""
                # id = self.insertDatabase(insert_query, (item['web_parent_id'], item['web_grand_parent_id'], item['web_cid'], item['web_id'], item['web_title'], item['web_lead'], item['web_content'], item['web_image'], item['web_category_name'], item['web_category_url'], item['web_author'], item['web_author_link'], item['web_like_count'], item['web_share_count'], item['web_url_comment'], item['web_child_count'], item['web_link'], item['web_domain_id'], item['web_domain_name'], item['web_post_type'], item['web_branch'], item['web_sub_branch'], item['web_is_crawled'], item['web_crawler_time'], item['web_created'], item['web_tag'], item['web_group'], item['web_type'], item['is_filter_banking'], item['is_filter_education'], item['is_filter_tele'], item['is_filter_leisure'], item['is_filter_media'], item['is_filter_cele'], item['is_filter_service'], item['is_filter_property'], item['is_filter_clothing'], item['is_filter_transport'], item['is_filter_tourism'], item['is_filter_building'], item['is_filter_charity'], item['is_filter_argi'], item['is_filter_pharma'], item['is_filter_fina'], item['is_filter_food'], item['is_filter_drink'], item['is_filter_visual'], item['is_filter_it'], item['is_filter_furniture'], item['is_filter_household'], item['is_filter_other_1'], item['is_filter_other_2'], item['is_filter_other_3'], item['is_filter_other_4'], item['is_filter_other_5'], item['is_filter_updated'], item['web_content'], item['web_like_count'], item['web_crawler_time']))
                return key_insert

            # OLD INSERT MYSQL GET KEY AFTER THAT INSERT ES
            # insert_query = """INSERT INTO web_data (web_parent_id,web_grand_parent_id,web_cid,web_id,web_title,web_lead,web_content,web_image,web_category_name,web_category_url,web_author,web_author_link,web_like_count,web_share_count,web_url_comment,web_child_count,web_link,web_domain_id,web_domain_name,web_post_type,web_branch,web_sub_branch,web_is_crawled,web_crawler_time,web_created,web_tag,web_group,web_type,is_filter_banking,is_filter_education,is_filter_tele,is_filter_leisure,is_filter_media,is_filter_cele,is_filter_service,is_filter_property,is_filter_clothing,is_filter_transport,is_filter_tourism,is_filter_building,is_filter_charity,is_filter_argi,is_filter_pharma,is_filter_fina,is_filter_food,is_filter_drink,is_filter_visual,is_filter_it,is_filter_furniture,is_filter_household,is_filter_other_1,is_filter_other_2,is_filter_other_3,is_filter_other_4,is_filter_other_5,is_filter_updated) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE web_content = %s, web_like_count = %s, web_crawler_time = %s"""
            # id = self.insertDatabase(insert_query, (item['web_parent_id'], item['web_grand_parent_id'], item['web_cid'], item['web_id'], item['web_title'], item['web_lead'], item['web_content'], item['web_image'], item['web_category_name'], item['web_category_url'], item['web_author'], item['web_author_link'], item['web_like_count'], item['web_share_count'], item['web_url_comment'], item['web_child_count'], item['web_link'], item['web_domain_id'], item['web_domain_name'], item['web_post_type'], item['web_branch'], item['web_sub_branch'], item['web_is_crawled'], item['web_crawler_time'], item['web_created'], item['web_tag'], item['web_group'], item['web_type'], item['is_filter_banking'], item['is_filter_education'], item['is_filter_tele'], item['is_filter_leisure'], item['is_filter_media'], item['is_filter_cele'], item['is_filter_service'], item['is_filter_property'], item['is_filter_clothing'], item['is_filter_transport'], item['is_filter_tourism'], item['is_filter_building'], item['is_filter_charity'], item['is_filter_argi'], item['is_filter_pharma'], item['is_filter_fina'], item['is_filter_food'], item['is_filter_drink'], item['is_filter_visual'], item['is_filter_it'], item['is_filter_furniture'], item['is_filter_household'], item['is_filter_other_1'], item['is_filter_other_2'], item['is_filter_other_3'], item['is_filter_other_4'], item['is_filter_other_5'], item['is_filter_updated'], item['web_content'], item['web_like_count'], item['web_crawler_time']))
            #
            # duplicate = self.es.exists(index=self.es_index, doc_type=self.es_doc_type, id=id)
            # if(duplicate is True):
            #     update_data_es = {}
            #     update_data_es['doc'] = self.get_update_data(item)
            #     self.es.update(index=self.es_index, doc_type=self.es_doc_type, id=id, body=dict(update_data_es))
            #     return id
            # else:
            #     self.es.index(index=self.es_index, doc_type=self.es_doc_type, id=id, body=dict(item))
            #     return id

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
        sql = """INSERT INTO web_raw(web_key, web_data, web_link) VALUE (%s, %s, %s)"""
        curr = self.insertDatabase(sql,(web_key, json.dumps(data.__dict__), data["web_link"]))

    def _set_raw_null(self, web_link, web_domain):
        sql = """INSERT INTO web_null(web_link, web_domain) VALUE (%s, %s)"""
        curr = self.insertDatabase(sql,(web_link, web_domain))