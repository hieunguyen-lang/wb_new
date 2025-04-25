# -*- coding: utf-8 -*-
__author__ = 'VuongNM'

import os
import sys
import time
import re
import subprocess
import datetime
from termcolor import colored


SPIDER_NAMES = [ 'bnews','24h','2sao','afamily','alobacsi','baobaohiemxahoi','baobariavungtau','baocantho','baochinhphu','baocongthuong','baodatviet','baodautu','baogiaothong','baohaiquan','baohiemxahoi','baotainguyenmoitruong','baotintuc','baovanhoa','baoxaydung','bariavungtau','bizlive','bnews','bongda360','bongdaplus','cadn','cafebiz','cafef','cafeland','camnangmuasam','congluan','congly','daibieunhandan','daidoanket','daikynguyen','daikynguyenvn','dangcongsan','dantri','danviet','dep','dientutieudung','doanhnhanonline','doanhnhansaigon','doisongphapluat','dothi','dulichvn','emdep','englishthesaigontimes','enternews','eva','giadinh','giadinhvatreem','giadinhvietnam','giaoduc','giaoducthoidai','gioitre','healthplus','ictnews','infonet','kenh14','khoahocdoisong','khoahocvacongnghevietnam','kienthuc','kinhtenongthon','landtoday','laodong','micgov','motthegioi','ndh','ngoisao','nguoiduatin','nhandan','nhandancom','nhandanorg','nld','nss','phununet','phunuonline','qdnd','saigondautu','saoonline','seatimes','soha','songkhoe','suckhoedoisong','taichinhplus','tamnhin','tapchibcvt','tapchitaichinh','tbck','tbdn','thanhnien','thethao247','thitruongtaichinh','thoibaokinhdoanh','thoibaonganhang','thoibaotaichinhvietnam','tienphong','tiin','tinmoi','tinnhanhchungkhoan','trithuccongluan','ttdn','ttvn','tuoitre','vcci','vccinews','vef','ven','vietbao','vietnamnet','vietnamplus','vietq','vietstock','viettimes','vinacorp','vir','vnba','vneconomictimes','vneconomy','vnex','vnmedia','vov','vtc','vtv','xahoithongtin','xalo','xaluan','zing' ] 
NUM_CONCURENT_SPIDER = 2
NEXT_SPIDER = 0




def get_running_spiders():
    ret = []
    ps_cmd  = """ ps -ef | grep -e "/usr/local/bin/scrapy"  | grep -v "post|comment|reply" | grep -e "GR1" """
    procs  = os.popen(ps_cmd).read().split("\n")
    for line in procs:
        if "python" in line:
            regex = r"crawl \w+ "
            parts  = re.findall(regex,line)
            if len (parts)  > 0:
                spider_name= parts[0].strip("").split(" ")[1]
                if spider_name in SPIDER_NAMES:
                    ret.append(spider_name)
    return ret




def spawn_spider(running_spiders):
    global SPIDER_NAMES
    global NUM_CONCURENT_SPIDER
    global NEXT_SPIDER
 
    indexes = map( lambda x: SPIDER_NAMES.index(x), running_spiders)
    while(True):
        if NEXT_SPIDER in indexes:
            NEXT_SPIDER = NEXT_SPIDER +1
        else:
            break;
    if (NEXT_SPIDER >= len(SPIDER_NAMES)):
        NEXT_SPIDER  = 0
        print (colored("[CRAWLING DAEMON] finish crawling cycle at " + str(datetime.datetime.now()),"red"))
    next_spider_name = SPIDER_NAMES[NEXT_SPIDER]
    print (str(datetime.datetime.now()) + " [CRAWLING DAEMON] spawning spider " + next_spider_name)
    NEXT_SPIDER = NEXT_SPIDER +1 
    cmd = "scrapy crawl " + next_spider_name + " -a group=GR1 "
    subprocess.Popen(cmd,shell=True,stdin=None, stdout=open("/dev/null","w"), stderr=open("/dev/null","w"),close_fds=True)           
    # cmd = "scrapy crawl " + next_spider_name + " -a group=GR1 "
    # os.popen(cmd)



def main(num_conn_proc=10,running_dir="/home/web_crawl/wb/"):
    global SPIDER_NAMES
    global NUM_CONCURENT_SPIDER
    global NEXT_SPIDER

    #run the service
    #if the number of spider is smaller than number of allowed concurrent spider, spawn some spider 
    os.chdir(running_dir)
    print (colored("[CRAWLING DAEMON] running_dir " + running_dir,"red"))
    print ("[CRAWLING DAEMON] start crawling with "+ str(num_conn_proc)+" concurrent spiders ")
    while (True):
        running_spiders = get_running_spiders()
        print (colored("[CRAWLING DAEMON] "+ str(len(running_spiders)) +" running_spiders " + str(running_spiders),"green"))
        count  = num_conn_proc - len(running_spiders)
        while (count > 0):
            spawn_spider(running_spiders)
            count = count - 1
        time.sleep(3)



if __name__=="__main__":

    if len(sys.argv) ==3: 
        print ("[CRAWLING DAEMON] daemon start with passed params")
        print (sys.argv[1:])
        main(num_conn_proc = int(sys.argv[1]), running_dir = sys.argv[2])

    elif len(sys.argv) ==1 :
        print ("[CRAWLING DAEMON] use defalut params")
        main()