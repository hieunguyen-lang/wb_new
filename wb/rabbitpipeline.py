# -*- coding: utf-8 -*-
__author__="VuongNM"

import pika
import configparser
from scrapy import settings
import json
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()

class RabbitPipeline(object):
    ##  ##     
    ##  ##
    ##########  
    ######  ##  
    ##########

    def __init__(self):
        # credentials = pika.PlainCredentials(username='monitaz', password='monitaz2016')

        credentials = pika.PlainCredentials(username=os.getenv('RABBIT_USERNAME'), password=os.getenv('RABBIT_PASSWORD'))
        params = pika.ConnectionParameters(os.getenv('RABBIT_HOST'),credentials=credentials)
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=os.getenv('RABBIT_QUEUE'))
        self.channel.exchange_declare(exchange='the_famous_fanout', type='fanout')
        self.channel.queue_bind(exchange='the_famous_fanout', queue="monitaz_ifollow_banking")
        self.channel.queue_bind(exchange='the_famous_fanout', queue="monitaz_ifollow_tele")

    def process_item(self,item,spider):
        if item is not None :
            string = str(item["web_link"]) + "_" + str(item['web_domain_name'])
            key_insert = hashlib.md5(str(string).decode('utf-8').encode('utf-8')).hexdigest()

            item_dict = dict(item)
            item_dict['web_key'] = key_insert
            json_string = json.dumps(item_dict)
            self.channel.basic_publish(exchange='the_famous_fanout',
                          routing_key='',
                          body=json_string)
            print(" [x] message sent!")
            return item
