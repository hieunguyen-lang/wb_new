import os
import random

# from scrapy import settings
from scrapy.utils.project import get_project_settings
from proxy import *
from proxy_https import *
from proxy_https_v2 import *
#from scrapy import log
settings = get_project_settings()
class RandomUserAgentMiddleware(object):
    def process_request(self, request,spider):
        userAgent = random.choice(settings['USER_AGENT_LIST'])
        if userAgent:
            request.headers.setdefault("User-Agent", userAgent)
            request.headers['User-Agent']=userAgent
        else:
            request.headers.setdefault("User-Agent",settings['USER_AGENT_LIST'][0])
            request.headers['User-Agent']=settings['USER_AGENT_LIST'][0]
            

# class ProxyMiddleware(object):
#     def process_request(self, request, spider):
#         request.meta['proxy'] = settings.get("HTTP_PROXY")
#
# class TorMiddleware(object):
#     def process_request(self, request, spider):
#         print ("[TOR] request forwarded to tor " + request.url)
#         request.meta['proxy'] = settings.get("POLIPO_PROXY")
#
# class RandomProxyMiddleware(object):
#     def __init__(self):
#         self.proxies = settings['PROXIES_LIST']
#         print ("[PROXY] random proxy list " + str(self.proxies))
#     def process_request(self,request,spider):
#         pick = random.choice(self.proxies)
#         print ("[PROXY] picked proxy "  + pick + " for request "  + request.url)
#
#         request.meta['proxy'] = pick
#
#
# class RandomProxyBuying(object):
#     def __init__(self):
#         self.proxies = settings['PROXIES_LIST_BUYING']
#         print ("[PROXY] random proxy list " + str(self.proxies))
#     def process_request(self,request,spider):
#         pick = random.choice(self.proxies)
#         print ("[PROXY] picked proxy "  + pick + " for request "  + request.url)
#
#         request.meta['proxy'] = pick
#
# class RandomProxyBuying_V2(object):
#     def __init__(self):
#         self.proxies = settings['PROXIES_LIST_BUYING_V2']
#         print ("[PROXY] random proxy list " + str(self.proxies))
#     def process_request(self,request,spider):
#         pick = random.choice(self.proxies)
#         print ("[PROXY] picked proxy "  + pick + " for request "  + request.url)
#
#         request.meta['proxy'] = pick
#
# class RandomProxyBuying_V3(object):
#     def __init__(self):
#         self.proxies = settings['PROXIES_LIST_BUYING_V3']
#         print ("[PROXY] random proxy list " + str(self.proxies))
#     def process_request(self,request,spider):
#         pick = random.choice(self.proxies)
#         print ("[PROXY] picked proxy "  + pick + " for request "  + request.url)
#
#         request.meta['proxy'] = pick
#
# class RandomProxyBuyingVnex(object):
#     def __init__(self):
#         self.proxies = settings['PROXIES_LIST_BUYING_VNEX']
#         print ("[PROXY] random proxy list " + str(self.proxies))
#     def process_request(self,request,spider):
#         pick = random.choice(self.proxies)
#         print ("[PROXY] picked proxy "  + pick + " for request "  + request.url)
#
#         request.meta['proxy'] = pick

class RandomProxyBuyingTEST(object):
    def __init__(self):
        self.proxies = PROXIES_LIST_BUYING_TEST
        print ("[PROXY] random proxy list " + str(self.proxies))
    def process_request(self,request,spider):
        pick = random.choice(self.proxies)
        print ("[PROXY] picked proxy "  + pick + " for request "  + request.url)

        request.meta['proxy'] = pick

# class RandomProxyBuyingDev(object):
#     def __init__(self):
#         self.proxies = settings['PROXIES_LIST_BUYING_DEV']
#         print ("[PROXY] random proxy list " + str(self.proxies))
#         print ("==============")
#         print ("WTH")
#         print ("==============")
#
#     def process_request(self,request,spider):
#         pick = random.choice(self.proxies)
#         print ("[PROXY] picked proxy "  + pick + " for request "  + request.url)
#
#         request.meta['proxy'] = pick
#
# class RandomProxyBuyingHTTPS(object):
#     def __init__(self):
#         self.proxies = PROXIES_LIST_BUYING_HTTPS_V2
#         print ("[PROXY] random proxy list " + str(self.proxies))
#     def process_request(self,request,spider):
#         pick = random.choice(self.proxies)
#         print ("[PROXY] picked proxy "  + pick + " for request "  + request.url)
#
#         request.meta['proxy'] = pick
#
# class RandomProxyBuyingHTTPSREAL(object):
#     def __init__(self):
#         self.proxies = PROXIES_LIST_BUYING_HTTPS
#         print ("[PROXY] random proxy list " + str(self.proxies))
#     def process_request(self,request,spider):
#         pick = random.choice(self.proxies)
#         print ("[PROXY] picked proxy "  + pick + " for request "  + request.url)
#
#         request.meta['proxy'] = pick