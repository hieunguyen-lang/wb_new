import random

from scrapy.utils.project import get_project_settings
from proxy import *

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

class RandomProxyBuyingTEST(object):
    def __init__(self):
        self.proxies = PROXIES_LIST_BUYING_TEST
        print ("[PROXY] random proxy list " + str(self.proxies))
    def process_request(self,request,spider):
        pick = random.choice(self.proxies)
        print ("[PROXY] picked proxy "  + pick + " for request "  + request.url)

        request.meta['proxy'] = pick