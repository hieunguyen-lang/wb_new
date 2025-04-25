# -*- coding: utf-8 -*-

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

# POLIPO_PROXY = "http://localhost:8118"
#
# PROXIES_LIST = [
#     'https://headoop.monitaz:9044',
#     'https://bodoop2.monitaz:9044',
#     'https://bodoop1.monitaz:9044'
# ]
#
# PROXIES_LIST_BUYING2 = [
#     # 'http://lum-customer-splus_jsc-zone-static:g79psmcp525t@zproxy.lum-superproxy.io:22225'
#     'http://127.0.0.1:24000'
#     # 'http://127.0.0.1:22225'
# ]
#
# PROXIES_LIST_BUYING = [
#     "http://lum-customer-hl_8088d7d6-zone-zone1:iq5kgfv7tnp8@zproxy.lum-superproxy.io:22225"
# ]
# PROXIES_LIST_BUYING_V2 = [
#     "http://lum-customer-hl_8088d7d6-zone-zone2:won6ft395ynk@zproxy.lum-superproxy.io:22225"
# ]
#
# PROXIES_LIST_BUYING_V3 = [
#     "https://tvplusbd1:QLIYKU@135.148.36.59:7548",
#     "https://tvplusbd1:QLIYKU@135.148.36.50:10860",
#     "https://tvplusbd1:QLIYKU@135.148.36.47:13114",
#     "https://tvplusbd1:QLIYKU@135.148.62.174:6541",
#     "https://tvplusbd1:QLIYKU@135.148.62.163:8411"
# ]
#
# PROXIES_LIST_BUYING_VNEX = [
#     # 'http://lum-customer-hl_aa3bca6c-zone-static:g79psmcp525t@zproxy.luminati.io:22225'
#     'http://lum-customer-hl_8088d7d6-zone-zone1:iq5kgfv7tnp8@zproxy.lum-superproxy.io:22225'
# ]
#
# PROXIES_LIST_BUYING_DEV = [
#     # 'http://lum-customer-hl_aa3bca6c-zone-static:g79psmcp525t@zproxy.luminati.io:22225'
#     # 'http://138.68.154.243:8118/',
#     # 'http://45.33.86.60:80/',
#     # 'http://138.68.154.243:8118/'
#     'https://bodoop2.monitaz:9044'
# ]

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
    # 'wb.rabbitpipeline.RabbitPipeline':400, #must after the Wbpipeline

    # 'wb.pipelines.DummyPipeline': 300,
}

import os
# config
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARSER_CONFIG_FILE = os.path.join(BASE_DIR, 'parse_config.cfg')
PARSER_CONFIG_COMMENT_FILE = os.path.join(BASE_DIR, 'parse_comment_config.cfg')
PARSER_CONFIG_FILE_HOMEPAGE = os.path.join(BASE_DIR, 'parse_config_homepage.cfg')
PARSER_CONFIG_URL_FILE = os.path.join(BASE_DIR, 'parse_url_config.cfg')
EXTRA_CONFIG_FILE = os.path.join(BASE_DIR, 'extra_config.cfg')

# DOWNLOADER_CLIENT_TLS_METHOD='TLSv1.0'
LOG_URLS_FILE = '/home/scrapy-logs'

def settings():
    return None