# -*- coding: utf-8 -*-

import os
BOT_NAME = 'wb'

SPIDER_MODULES = ['wb.spiders']
NEWSPIDER_MODULE = 'wb.spiders'


# USER_AGENT = 'wb (+http://www.google.com)'
USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10',
    'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
]

#DOWNLOADER_CLIENTCONTEXTFACTORY  =  'wb.sslcontexttest.CustomContextFactory'
#DOWNLOADER_CLIENT_TLS_METHOD = 'TLS'

DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'wb.middlewares.RandomUserAgentMiddleware': 400,

}
TELNETCONSOLE_ENABLED = False

CONCURRENT_REQUESTS=32
CONCURRENT_REQUESTS_PER_IP=16


DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
}
EXTENSIONS = {
   'scrapy.telnet.TelnetConsole': None
}



ITEM_PIPELINES = {
    'wb.pipelines.WbPipeline': 300,
}


# config
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARSER_CONFIG_FILE = os.path.join(BASE_DIR, 'parse_config.cfg')

# DOWNLOADER_CLIENT_TLS_METHOD='TLSv1.0'
LOG_URLS_FILE = '/home/scrapy-logs'

def settings():
    return None