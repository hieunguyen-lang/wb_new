# -*- coding: utf-8 -*-

__author__ = 'DucHung'


# //
# //                            _
# //                         _ooOoo_
# //                        o8888888o
# //                        88" . "88
# //                        (| -_- |)
# //                        O\  =  /O
# //                     ____/`---'\____
# //                   .'  \\|     |//  `.
# //                  /  \\|||  :  |||//  \
# //                 /  _||||| -:- |||||_  \
# //                 |   | \\\  -  /'| |   |
# //                 | \_|  `\`---'//  |_/ |
# //                 \  .-\__ `-. -'__/-.  /
# //               ___`. .'  /--.--\  `. .'___
# //            ."" '<  `.___\_<|>_/___.' _> \"".
# //           | | :  `- \`. ;`. _/; .'/ /  .' ; |
# //           \  \ `-.   \_\_`. _.'_/_/  -' _.' /
# // ===========`-.`___`-.__\ \___  /__.-'_.'_.-'================



from datetime import datetime,date
import time
from datetime import timedelta
from  dateutil import parser
import calendar
import unidecode
import re
import json
from wb.items import WbItem
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

class Helper:
    def __init__(self, *args, **kwargs):
        self.DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
        self.DATE_REGEX =   '\d+/\d+/\d+'
        self.TIME_REGEX = '\d+:\d+'

    def getServerVersion(self):
        return "SV01"

    def _join_data(self, separator=None, data=None):
        if(separator != None and data != None):
            if len(data) > 0:
                s = data[0]
                for i in range(1, len(data)):
                    if(data[i]):
                        words = data[i].strip().split(" ")
                        if len(words) > 15:
                            s = s + " <br><br> " + data[i] 
                        else:
                            s = s + separator + data[i].strip()
                s=re.sub(r"(<br>){2,}", " <br><br> ",s)
                s=re.sub(r"\s{2,}", " ",s)
                return s
        return ''

    def _join_data_no_strip(self, separator=None, data=None):
        if(separator != None and data != None):
            if len(data) > 0:
                s = data[0]
                for i in range(1, len(data)):
                    if(data[i]):
                        words = data[i].split(" ")
                        if len(words) > 15:
                            s = s + " <br><br> " + data[i] 
                        else:
                            s = s + separator + data[i]
                s=re.sub(r"(<br>){2,}", " <br><br> ",s)
                s=re.sub(r"\s{2,}", " ",s)
                return s
        return ''

    def _to_dict(self, data):
        d = {}
        if(len(data) > 0):
            for i in range(0, len(data)):
                d[i] = data[i]
        return d

    def createdHeader(self, domain):
        headers = {
            "Host": ""+domain+"",
            "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
            "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "vi-VN,vi;q=0.8,fr-FR;q=0.6,fr;q=0.4,en-US;q=0.2,en;q=0.2,zh-CN;q=0.2,zh;q=0.2,mt;q=0.2,zh-TW;q=0.2",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": ""
        }
        return headers

    def createdHeaderTruongton(self, session_id):
        headers = {}
        headers['Host'] = "truongton.net"
        headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36"
        headers['Accept'] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        headers['Accept-Language'] = "vi-VN,vi;q=0.8,fr-FR;q=0.6,fr;q=0.4,en-US;q=0.2,en;q=0.2,zh-CN;q=0.2,zh;q=0.2,mt;q=0.2,zh-TW;q=0.2"
        headers['Content-Type'] = "application/x-www-form-urlencoded"
        headers['Connection'] = "keep-alive"
        headers['Cookie'] = "ttsessionhash=" + session_id+ "; ttimloggedin=yes"
        return headers

    def getItem(self):
        item = WbItem()
        item['web_parent_id'] = '0'
        item['web_grand_parent_id'] = 0
        item['web_cid'] = ""
        item['web_id'] = ""
        item['web_title'] = ""
        item['web_lead'] = ""
        item['web_content'] = ""
        item['web_author'] = ""
        item['web_author_link'] = ""
        item['web_image'] = ""
        item['web_category_name'] = ""

        item['web_like_count'] = 0
        item['web_share_count'] = 0
        item['web_child_count'] = 0
        item['web_url_comment'] = ""

        item['web_link'] = ""
        item['web_domain_id'] = ""
        item['web_domain_name'] = ""
        #web_post_type: 0 is post, 1 is comment, 2 is reply
        item['web_post_type'] = 0
        item['web_branch'] = ""
        item['web_sub_branch'] = ""
        item['web_is_crawled'] = 0
        item['web_crawler_time'] = 0
        item['web_created'] = ""
        item['web_tag'] = ""
        item['web_group'] = ""
        #web_type: 0 is website, 1 is forum
        item['web_type'] = 0
        item['is_filter_banking'] = 0
        item['is_filter_education'] = 0
        item['is_filter_tele'] = 0
        item['is_filter_leisure'] = 0
        item['is_filter_media'] = 0
        item['is_filter_cele'] = 0
        item['is_filter_service'] = 0
        item['is_filter_property'] = 0
        item['is_filter_clothing'] = 0
        item['is_filter_transport'] = 0
        item['is_filter_tourism'] = 0
        item['is_filter_building'] = 0
        item['is_filter_charity'] = 0
        item['is_filter_argi'] = 0
        item['is_filter_pharma'] = 0
        item['is_filter_fina'] = 0
        item['is_filter_food'] = 0
        item['is_filter_drink'] = 0
        item['is_filter_visual'] = 0
        item['is_filter_it'] = 0
        item['is_filter_furniture'] = 0
        item['is_filter_household'] = 0
        item['is_filter_other_1'] = 0
        item['is_filter_other_2'] = 0
        item['is_filter_other_3'] = 0
        item['is_filter_other_4'] = 0
        item['is_filter_other_5'] = 0
        item['is_filter_updated'] = 0
        return item


    def format_classic1(self,input_str):
        """
        dateformat example: 20/11/2016
        time format: 15:00
        """
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, classic1 prototype datetime parsing")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_baodanang(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, baodanang.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_khuyennongvn_gov(self, input_str):
        input_str = input_str.strip()
        try:
            if "AM" in input_str:
                    hours = 0
                    input_str = input_str.replace(" AM", "")

            if "PM" in input_str:
                hours = 12
                input_str = input_str.replace(" PM", "")

            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]

            stripped = time_str + " " + date_str
            stripped = stripped.strip()

            temp = datetime.strptime(stripped, "%H:%M:%S %m/%d/%Y")
            if (hours == 12):
                timeFormat = (temp + timedelta(hours=12)).strftime(self.DATETIME_FORMAT)

            if (hours == 0):
                timeFormat = temp.strftime(self.DATETIME_FORMAT)
            return timeFormat
        except Exception:
            print ("[EXCEPTION] datetime converting exception, khuyennongvn.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_dubaotiente(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, dubaotiente.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_thongtinbank(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, thongtinbank.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tapchicaosu(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tapchicaosu.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_hotronghiencuu(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hotronghiencuu.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_lamchutaichinh(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, lamchutaichinh.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_nganhangaz(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, nganhangaz.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tapchikientruc(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tapchikientruc.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_chinhsachdautu(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, chinhsachdautu.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tamnhindoanhnhan(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tamnhindoanhnhan.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_diendandothi_kinhtedothi(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, diendandothi.kinhtedothi.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tintuctienao(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tintuctienao.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_vannghequandoi(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, vannghequandoi.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_chongbanphagia(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, chongbanphagia.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_kinhtevadautu(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, kinhtevadautu.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_trituemoi(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, trituemoi.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_chuongtrinhmuctieuquocgia_baodantoc(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, chuongtrinhmuctieuquocgia.baodantoc.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_uytinthuonghieu(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, uytinthuonghieu.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_thegioidisan(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, thegioidisan.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_cgvdt(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, cgvdt.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_quanlynhanuoc(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, quanlynhanuoc.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_taichinhcoban(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, taichinhcoban.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_khuyennongkiengiang(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, khuyennongkiengiang.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_kienthuckinhte(self, input_str):
        input_str = input_str.replace("tháng"," ").strip()
        input_str = input_str.replace("   "," ").strip()
        try:
            time = datetime.now()
            nam=time.strftime("%Y")
            input_str = input_str.strip()
            date_rex = "\d+ \d+"
            date_str = re.findall(date_rex, input_str)[0]
            date_str1 = date_str+" "+nam
            stripped = date_str1
            return datetime.strptime(stripped, "%d %m %Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, kienthuckinhte.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_blognganhang(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, blognganhang.org")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tapchilaodongxahoi(self, input_str):
        input_str = input_str.strip()
        try:
            if "AM" in input_str:
                hours = 0
                input_str = input_str.replace(" AM", "")

            if "PM" in input_str:
                hours = 12
                input_str = input_str.replace(" PM", "")

            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]

            stripped = time_str + " " + date_str
            stripped = stripped.strip()

            temp = datetime.strptime(stripped, "%H:%M %d/%m/%Y")
            if (hours == 12):
                timeFormat = (temp + timedelta(hours=12)).strftime(self.DATETIME_FORMAT)

            if (hours == 0):
                timeFormat = temp.strftime(self.DATETIME_FORMAT)
            return timeFormat
        except Exception:
            try:
                date_rex = "\d+-\d+-\d+"
                time_rex = "\d+:\d+"
                date_str = re.findall(date_rex, input_str)[0]
                time_str = re.findall(time_rex, input_str)[0]

                stripped = time_str + " " + date_str
                stripped = stripped.strip()

                temp = datetime.strptime(stripped, "%H:%M %Y-%m-%d")
                if (hours == 12):
                    timeFormat = (temp + timedelta(hours=12)).strftime(self.DATETIME_FORMAT)

                if (hours == 0):
                    timeFormat = temp.strftime(self.DATETIME_FORMAT)
                return timeFormat
            except Exception:
                print ("[EXCEPTION] datetime converting exception, tapchilaodongxahoi.vn")
                return datetime.today().strftime(self.DATETIME_FORMAT)
            
    def format_phapluatphattrien(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception,phapluatphattrien.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_nganhangnongthon(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, nganhangnongthon.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_vntre(self, input_str):
        input_str = input_str.replace("T"," ").replace(".000000+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, vntre.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_lapphap(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped = date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, lapphap.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_gocnhinphaply_nguoiduatin(self, input_str):
        input_str = input_str.replace("T"," ").replace(".000000+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, gocnhinphaply.nguoiduatin.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_ssc_gov(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, ssc.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_doanhnhanvatieudungV2(self, input_str):
        input_str = input_str.replace("T"," ").replace(".000000+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, doanhnhanvatieudung.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_saigoneconomynet(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception,saigoneconomynet.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_thoibaovietnamnet(self, input_str):
        input_str = input_str.replace("T"," ").replace(".000000+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, thoibaovietnam.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_thegioitiepthivietnam(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception,thegioitiepthivietnam.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_doithoaiphattrien(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, doithoaiphattrien.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_thebusiness(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, thebusiness.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_kinhdoanhplus(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, kinhdoanhplus.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_vnewstoday(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, vnewstoday.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_baobackan(self, input_str):
        input_str = input_str.replace("T"," ").replace("+0700"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, baobackan.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_newsliver_site(self, input_str):
        input_str = input_str.replace("-"," ").strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, newsliver.site")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_dbndhanoi_gov(self, input_str):
        input_str = str(unidecode.unidecode(input_str)).strip()
        if "Thang Muoi Hai" in input_str:
            month = 12
            input_str = input_str.replace("Thang Muoi Hai", str(month))

        if "Thang Muoi Mot" in input_str:
            month = 11
            input_str = input_str.replace("Thang Muoi Mot", str(month))

        if "Thang Muoi" in input_str:
            month = 10
            input_str = input_str.replace("Thang Muoi", str(month))

        if "Thang Chin" in input_str:
            month = 9
            input_str = input_str.replace("Thang Chin", str(month))

        if "Thang Tam" in input_str:
            month = 8
            input_str = input_str.replace("Thang Tam", str(month))

        if "Thang Bay" in input_str:
            month = 7
            input_str = input_str.replace("Thang Bay", str(month))

        if "Thang Sau" in input_str:
            month = 6
            input_str = input_str.replace("Thang Sau", str(month))

        if "Thang Nam" in input_str:
            month = 5
            input_str = input_str.replace("Thang Nam", str(month))

        if "Thang Tu" in input_str:
            month = 4
            input_str = input_str.replace("Thang Tu", str(month))

        if "Thang Ba" in input_str:
            month = 3
            input_str = input_str.replace("Thang Ba", str(month))

        if "Thang Hai" in input_str:
            month = 2
            input_str = input_str.replace("Thang Hai", str(month))

        if "Thang Mot" in input_str:
            month = 1
            input_str = input_str.replace("Thang Mot", str(month))

        input_str = input_str.replace(" - ", " ")
        input_str = input_str.strip()
        try:
            date_rex = "\d+ \d+ \d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %d %m %Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, dbndhanoi.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_xetv(self, input_str):
        input_str = input_str.replace("T"," ").replace("+0700"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, xetv.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_canhco(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, canhco.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_autotv(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, autotv.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_infofinance(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, infofinance.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_dbkcqdnbacninh(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, dbkcqdnbacninh.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_bankviet(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, bankviet.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_69invest(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, 69invest.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tranggame(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tranggame.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_doanhnhanngaynay(self, input_str):
        input_str = input_str.replace("T"," ").replace(".000000+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, doanhnhanngaynay.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_bloghuuich(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, bloghuuich.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_ithethao(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, ithethao.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_hanoitoplist(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hanoitoplist.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_bankcuatoi(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, bankcuatoi.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_useful(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, useful.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_vncash24h(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, vncash24h.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_dongthap_gov(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, dongthap.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_tuyengiao_phuyen_gov(self, input_str):
        input_str = input_str.replace("+07"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tuyengiao.phuyen.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_hoinhabao(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d-%m-%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hoinhabao.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_doisongdoanhnhan(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, doisongdoanhnhan.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_kimson_ninhbinh_gov(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, kimson.ninhbinh.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_c4cvn(self, input_str):
        input_str = input_str.replace("T"," ").replace(".000Z"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, c4c.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_yenthanh_nghean_gov(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, yenthanh.nghean.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_snnptnt_laocai_gov(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, snnptnt.laocai.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_cafekinhte(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, cafekinhte.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_hochiminhcity_gov(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hochiminhcity.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_hungha_thaibinh_gov(self, input_str):
        input_str = input_str.replace("T"," ").replace("+0700"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hungha.thaibinh.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_laodongvaphapluat_laodongthudo(self, input_str):
        try:
            data = json.loads(input_str)
            input_str = data['datePublished']
            input_str = input_str.replace("T", " ").replace("+07:00", " ").strip()
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            try:
                date_rex = "\d+-\d+-\d+"
                time_rex = "\d+:\d+:\d+"
                date_str = re.findall(date_rex, input_str)[0]
                time_str = re.findall(time_rex, input_str)[0]
                datetime_str = time_str + " " + date_str
                return datetime.strptime(datetime_str, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
            except Exception:
                try:
                    date_rex = "\d+/\d+/\d+"
                    time_rex = "\d+:\d+"
                    date_str = re.findall(date_rex, input_str)[0]
                    time_str = re.findall(time_rex, input_str)[0]
                    datetime_str = time_str + " " + date_str
                    return datetime.strptime(datetime_str, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
                except Exception:
                    print ("[EXCEPTION] datetime converting exception, laodongvaphapluat.laodongthudo.vn")
                    return datetime.today().strftime(self.DATETIME_FORMAT)
                
    def format_hoabinhtv(self,input_str):
        input_str = input_str.strip()
        try:
            time = datetime.now()
            nam=time.strftime("%Y")
            input_str = input_str.strip()
            date_rex = "\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            date_str1 = date_str+"/"+nam
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str1
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hoabinhtv.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_qrt(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            try:
                date_rex = "\d+/\d+/\d+"
                time_rex = "\d+:\d+"
                date_str = re.findall(date_rex,input_str)[0]
                time_str = re.findall(time_rex,input_str)[0]
                stripped = time_str + " " + date_str
                return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
            except Exception:
                print ("[EXCEPTION] datetime converting exception, qrt.vn")
                return datetime.today().strftime(self.DATETIME_FORMAT)
            
    def format_hatinhtv(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hatinhtv.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_sputniknews(self,input_str):
        input_str = input_str.replace(".", "/").strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, sputniknews.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_thieuhoa_thanhhoa_gov(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+ - \d+ - \d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d - %m - %Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, snnptnt.laocai.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_thanhgiong(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, thanhgiong.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tapchigiaoduc_edu(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tapchigiaoduc.edu.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
    
    def format_danang_gov(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d-%m-%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, danang.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_cema_gov(self, input_str):
        input_str = input_str.strip()
        try:
            if "AM" in input_str:
                    hours = 0
                    input_str = input_str.replace(" AM", "")

            if "PM" in input_str:
                hours = 12
                input_str = input_str.replace(" PM", "")

            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]

            stripped = time_str + " " + date_str
            stripped = stripped.strip()

            temp = datetime.strptime(stripped, "%H:%M %d/%m/%Y")
            if (hours == 12):
                timeFormat = (temp + timedelta(hours=12)).strftime(self.DATETIME_FORMAT)

            if (hours == 0):
                timeFormat = temp.strftime(self.DATETIME_FORMAT)
            return timeFormat
        except Exception:
            try:
                input_str = str(unidecode.unidecode(input_str)).strip()
                # input_str = input_str.split(" ")
                print (input_str)
                if "thang" in input_str:
                    diff = timedelta(days=int(input_str[0]) * 30)
                    passed = str(passed).split(' ')[0]
                    now = datetime.now()
                    passed = now - diff
                    return passed.strftime(self.DATETIME_FORMAT)
                elif "tuan" in input_str:
                    diff = timedelta(days=int(input_str[0]) * 7)
                    passed = str(passed).split(' ')[0]
                    now = datetime.now()
                    passed = now - diff
                    return passed.strftime(self.DATETIME_FORMAT)
                elif "ngay" in input_str:
                    diff = timedelta(days=int(input_str[0]))
                    now = datetime.now()
                    passed = now - diff
                    return passed.strftime(self.DATETIME_FORMAT)
                elif "gio truoc" in input_str:
                    diff = timedelta(hours=int(input_str[0]))
                    now = datetime.now()
                    passed = now - diff
                    return passed.strftime(self.DATETIME_FORMAT)
                elif "phut truoc" in input_str:
                    diff = timedelta(minutes=int(input_str[0]))
                    now = datetime.now()
                    passed = now - diff
                    return passed.strftime(self.DATETIME_FORMAT)
                else:
                    str_date = input_str[2] + " " + input_str[3]
                    return datetime.strptime(str_date, "%d-%m-%Y %H:%M:%S").strftime(self.DATETIME_FORMAT)
            except Exception:
                print ("[EXCEPTION] datetime converting exception, cema.gov.vn")
                return datetime.today().strftime(self.DATETIME_FORMAT)
            
    def format_gdsr_gov(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, gdsr.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_etv_quochoi(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, etv.quochoi.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_vimc(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, vimc.co")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_hoangquan(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hoangquan.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_congdoantttt(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, congdoantttt.org.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_stockvn247(self, input_str):
        data = json.loads(input_str)
        input_str = data['datePublished']
        input_str = input_str.replace("T"," ").replace("-07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, stockvn247.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_atmbanking_edu(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, atmbanking.edu.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tcnn(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tcnn.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_ntdvn(self, input_str):
        data = json.loads(input_str)
        input_str = data['datePublished']
        input_str = input_str.strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, ntdvn.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_haiphong24h(self, input_str):
        input_str = input_str.replace("T"," ").replace(".000000+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, haiphong24h.org")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_vqh_hanoi_gov(self, input_str):
        input_str = input_str.replace("+07"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, vqh.hanoi.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tintucxedien(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tintucxedien.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_danvanhaiphong(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+-\d+-\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d-%m-%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, danvanhaiphong.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_bodephatquoc(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, bodephatquoc.org")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_conganquangninh_gov(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, conganquangninh.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_hoichuthapdoquangbinh_gov(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d-%m-%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hoichuthapdoquangbinh.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_kinhnghiemopt(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, kinhnghiemopt.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_chungta(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, chungta.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_vnask(self, input_str):
        data = json.loads(input_str)
        input_str = data['datePublished']
        input_str = input_str.strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, vnask.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_cachvaytiennganhang(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, cachvaytiennganhang.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_vdca_org(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, vdca.org.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_vinanet(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, vinanet.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_vn_stockproxx(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, vn.stockproxx.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tuangiao_gov(self, input_str):
        input_str = input_str.replace("+07"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tuangiao.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_backan_gov(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, backan.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_bantindoanhnghiep24h(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, bantindoanhnghiep24h.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_businesstoday(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, businesstoday.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_nhipsongsaigonV2(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, nhipsongsaigon.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tiepthiinfo(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tiepthiinfo.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_hoanghoa_thanhhoa_gov(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hoanghoa.thanhhoa.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_dbndthanhhoa_gov(self, input_str):
        input_str = str(unidecode.unidecode(input_str)).strip()
        print(input_str)
        if "Thang Muoi Hai" in input_str:
            month = 12
            input_str = input_str.replace("Thang Muoi Hai", str(month))

        if "Thang Muoi Mot" in input_str:
            month = 11
            input_str = input_str.replace("Thang Muoi Mot", str(month))

        if "Thang Muoi" in input_str:
            month = 10
            input_str = input_str.replace("Thang Muoi", str(month))

        if "Thang Chin" in input_str:
            month = 9
            input_str = input_str.replace("Thang Chin", str(month))

        if "Thang Tam" in input_str:
            month = 8
            input_str = input_str.replace("Thang Tam", str(month))

        if "Thang Bay" in input_str:
            month = 7
            input_str = input_str.replace("Thang Bay", str(month))

        if "Thang Sau" in input_str:
            month = 6
            input_str = input_str.replace("Thang Sau", str(month))

        if "Thang Nam" in input_str:
            month = 5
            input_str = input_str.replace("Thang Nam", str(month))

        if "Thang Tu" in input_str:
            month = 4
            input_str = input_str.replace("Thang Tu", str(month))

        if "Thang Ba" in input_str:
            month = 3
            input_str = input_str.replace("Thang Ba", str(month))

        if "Thang Hai" in input_str:
            month = 2
            input_str = input_str.replace("Thang Hai", str(month))

        if "Thang Mot" in input_str:
            month = 1
            input_str = input_str.replace("Thang Mot", str(month))

        input_str = input_str.replace(" - ", " ")
        input_str = input_str.strip()
        try:
            date_rex = "\d+ \d+ \d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %d %m %Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, dbndthanhhoa.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_vanvn(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, vanvn.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_baotangtuoitre(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, baotangtuoitre.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_dbndnghean(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, dbndnghean.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_thv(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, thv.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
    
    def format_danchuphapluat(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, danchuphapluat.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_vietnamdefence(self, input_str):
        input_str = input_str.strip()
        try:
            if "AM" in input_str:
                hours = 0
                input_str = input_str.replace(" AM", "")

            if "PM" in input_str:
                hours = 12
                input_str = input_str.replace(" PM", "")

            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]

            stripped = time_str + " " + date_str
            stripped = stripped.strip()

            temp = datetime.strptime(stripped, "%H:%M %d/%m/%Y")
            if (hours == 12):
                timeFormat = (temp + timedelta(hours=12)).strftime(self.DATETIME_FORMAT)

            if (hours == 0):
                timeFormat = temp.strftime(self.DATETIME_FORMAT)
            return timeFormat
        except Exception:
            print ("[EXCEPTION] datetime converting exception, vietnamdefence.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_hoinongdanninhbinh(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hoinongdanninhbinh.org.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_hagiang_gov(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hagiang.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tapchinongnghiep(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tapchinongnghiep.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_suckhoeso(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, suckhoeso.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_nghiencuuquocte(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, nghiencuuquocte.org")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_quydautuphattrien_hanoi_gov(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, quydautuphattrien.hanoi.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_ubkttw(self, input_str):
        input_str = input_str.replace("+07"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, ubkttw.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_hoahaudoanhnhanvietnam(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hoahaudoanhnhanvietnam.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_truyenthongkhoahoc(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, truyenthongkhoahoc.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_baohaiphongV2(self,input_str):
        try:
            input_str = input_str.strip()
            if "thang" in input_str:
                diff = timedelta(days=int(input_str[0]) * 30)
                passed = str(passed).split(' ')[0]
                now = datetime.now()
                passed = now - diff
                return passed.strftime(self.DATETIME_FORMAT)
            elif "tuan" in input_str:
                diff = timedelta(days=int(input_str[0]) * 7)
                passed = str(passed).split(' ')[0]
                now = datetime.now()
                passed = now - diff
                return passed.strftime(self.DATETIME_FORMAT)
            elif "ngay truoc" in input_str:
                diff = timedelta(days=int(input_str[0]))
                now = datetime.now()
                passed = now - diff
                return passed.strftime(self.DATETIME_FORMAT)
            elif "gio truoc" in input_str:
                diff = timedelta(hours=int(input_str[0]))
                now = datetime.now()
                passed = now - diff
                return passed.strftime(self.DATETIME_FORMAT)
            elif "phut truoc" in input_str:
                diff = timedelta(minutes=int(input_str[0]))
                now = datetime.now()
                passed = now - diff
                return passed.strftime(self.DATETIME_FORMAT)
            else:
                str_date = input_str[2] + " " + input_str[3]
                return datetime.strptime(str_date, "%d-%m-%Y %H:%M:%S").strftime(self.DATETIME_FORMAT)
        except Exception:
            try:
                if "SA" in input_str:
                        hours = 0
                        input_str = input_str.replace(" SA", "")

                if "CH" in input_str:
                    hours = 12
                    input_str = input_str.replace(" CH", "")

                date_rex = "\d+/\d+/\d+"
                time_rex = "\d+:\d+"
                date_str = re.findall(date_rex, input_str)[0]
                time_str = re.findall(time_rex, input_str)[0]

                stripped = time_str + " " + date_str
                stripped = stripped.strip()

                temp = datetime.strptime(stripped, "%H:%M %d/%m/%Y")
                if (hours == 12):
                    timeFormat = (temp + timedelta(hours=12)).strftime(self.DATETIME_FORMAT)

                if (hours == 0):
                    timeFormat = temp.strftime(self.DATETIME_FORMAT)
                return timeFormat
            except Exception:
                print ("[EXCEPTION] datetime converting exception, baohaiphong.vn")
                return datetime.today().strftime(self.DATETIME_FORMAT)
            
    def format_trianlietsi(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, trianlietsi.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_bongdadoisong(self, input_str):
        input_str = input_str.replace("T"," ").replace(".000000+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, bongdadoisong.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_oto365(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, oto365.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tinthethao(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tinthethao.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_thiennhienmoitruong(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, thiennhienmoitruong.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_finlog(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, finlog.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_bankso(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, bankso.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_bizlife(self, input_str):
        input_str = input_str.strip()
        try:
            if "AM" in input_str:
                    hours = 0
                    input_str = input_str.replace(" AM", "")

            if "PM" in input_str:
                hours = 12
                input_str = input_str.replace(" PM", "")

            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]

            stripped = time_str + " " + date_str
            stripped = stripped.strip()

            temp = datetime.strptime(stripped, "%H:%M %d/%m/%Y")
            if (hours == 12):
                timeFormat = (temp + timedelta(hours=12)).strftime(self.DATETIME_FORMAT)

            if (hours == 0):
                timeFormat = temp.strftime(self.DATETIME_FORMAT)
            return timeFormat
        except Exception:
            print ("[EXCEPTION] datetime converting exception, bizlife.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_nxbctqg(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, nxbctqg.org.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_cucthuyloi(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, cucthuyloi.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_kinhdoanhplusV2(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, kinhdoanhplus.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_xaydung_gov(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, xaydung.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_duonghaichieu(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, duonghaichieu.info")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_thuonghieuduluan(self, input_str):
        input_str = input_str.replace("T"," ").replace(".000000+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, thuonghieuduluan.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tradingview(self, input_str):
        input_str = input_str.replace("T"," ").replace(".000Z"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tradingview.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_khcncongthuong(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, khcncongthuong.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tietkiemnangluong(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tietkiemnangluong.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_thanhhoa_dcs(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+.\d+.\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d.%m.%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, thanhhoa.dcs.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_thoibao_de(self, input_str):
        input_str = input_str.replace("T"," ").replace("+02:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, thoibao.de")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tintuc24h_vip(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tintuc24h.vip")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_hoichieusangvietnam(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hoichieusangvietnam.org.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_kenhkinhtevn(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, kenhkinhte.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_coin98(self,input_str):
        input_str = str(unidecode.unidecode(input_str)).strip().lower()
        try:
            if "dece" in input_str:
                month = 12
                input_str = input_str.replace("dec", str(month))

            if "nov" in input_str:
                month = 11
                input_str = input_str.replace("nov", str(month))

            if "oct" in input_str:
                month = 10
                input_str = input_str.replace("oct", str(month))

            if "sep" in input_str:
                month = 9
                input_str = input_str.replace("sep", str(month))

            if "aug" in input_str:
                month = 8
                input_str = input_str.replace("aug", str(month))

            if "jul" in input_str:
                month = 7
                input_str = input_str.replace("jul", str(month))

            if "jun" in input_str:
                month = 6
                input_str = input_str.replace("june", str(month))

            if "may" in input_str:
                month = 5
                input_str = input_str.replace("may", str(month))

            if "apr" in input_str:
                month = 4
                input_str = input_str.replace("apr", str(month))

            if "mar" in input_str:
                month = 3
                input_str = input_str.replace("mar", str(month))

            if "feb" in input_str:
                month = 2
                input_str = input_str.replace("feb", str(month))

            if "jan" in input_str:
                month = 1
                input_str = input_str.replace("jan", str(month))

            input_str = input_str.replace(",", "")
            input_str = input_str.strip()
            date_rex = "\d+ \d+ \d+"
            date_str = re.findall(date_rex,input_str)[0]
            stripped = date_str

            return datetime.strptime(stripped, "%m %d %Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, coin98.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_docbaomoi(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, docbaomoi.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_ehoinhap_vanhoavaphattrien(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, ehoinhap.vanhoavaphattrien.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_icom(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, icom.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_dnvn(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, dnvn.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_diaocthoibao(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, diaocthoibao.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_2lua(self,input_str):
        try:
            input_str = str(unidecode.unidecode(input_str)).strip()
            print (input_str)
            if "thang truoc kia" in input_str:
                diff = timedelta(days=int(input_str[0]) * 30)
                passed = str(passed).split(' ')[0]
                now = datetime.now()
                passed = now - diff
                return passed.strftime(self.DATETIME_FORMAT)
            elif "tuan truoc kia" in input_str:
                diff = timedelta(days=int(input_str[0]) * 7)
                passed = str(passed).split(' ')[0]
                now = datetime.now()
                passed = now - diff
                return passed.strftime(self.DATETIME_FORMAT)
            elif "ngay truoc kia" in input_str:
                input_str = input_str.split(" ")
                diff = timedelta(days=int(input_str[0]))
                now = datetime.now()
                passed = now - diff
                return passed.strftime(self.DATETIME_FORMAT)
            elif "nhieu gio truoc kia" in input_str:
                input_str = input_str.split(" ")
                diff = timedelta(hours=int(input_str[0]))
                now = datetime.now()
                passed = now - diff
                return passed.strftime(self.DATETIME_FORMAT)
            elif "nhieu phut truoc kia" in input_str:
                input_str = input_str.split(" ")
                diff = timedelta(minutes=int(input_str[0]))
                now = datetime.now()
                passed = now - diff
                return passed.strftime(self.DATETIME_FORMAT)
            else:
                str_date = input_str[2] + " " + input_str[3]
                return datetime.strptime(str_date, "%d-%m-%Y %H:%M:%S").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, 2lua.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_bongdaphui(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %d-%m-%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, bongdaphui.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_truyenthongtre(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d-%m-%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, truyenthongtre.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_dtck(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, dtck.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_dulichgiaitriV2(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, dulichgiaitriV2.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_congan_hoabinh(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, congan.hoabinh.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_tapchidoanhnghiep(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tapchidoanhnghiep.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_bietthulienke(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, bietthulienke.info")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_phantichchungkhoan(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, phantichchungkhoan.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_trungtamnhietdoivietnga(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, trungtamnhietdoivietnga.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_hami_org(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hami.org.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_tapchilaoviet(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tapchilaoviet.org")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_bdscuatui(self, input_str):
        data = json.loads(input_str)
        input_str = data['datePublished']
        try:
            date_rex = "\d+-\d+-\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped = date_str
            return datetime.strptime(stripped, "%Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, bdscuatui.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_hiephoixangdau(self, input_str):
        input_str = str(unidecode.unidecode(input_str)).strip()
        if "Thang Muoi Hai" in input_str:
            month = 12
            input_str = input_str.replace("Thang Muoi Hai", str(month))

        if "Thang Muoi Mot" in input_str:
            month = 11
            input_str = input_str.replace("Thang Muoi Mot", str(month))

        if "Thang Muoi" in input_str:
            month = 10
            input_str = input_str.replace("Thang Muoi", str(month))

        if "Thang Chin" in input_str:
            month = 9
            input_str = input_str.replace("Thang Chin", str(month))

        if "Thang Tam" in input_str:
            month = 8
            input_str = input_str.replace("Thang Tam", str(month))

        if "Thang Bay" in input_str:
            month = 7
            input_str = input_str.replace("Thang Bay", str(month))

        if "Thang Sau" in input_str:
            month = 6
            input_str = input_str.replace("Thang Sau", str(month))

        if "Thang Nam" in input_str:
            month = 5
            input_str = input_str.replace("Thang Nam", str(month))

        if "Thang Tu" in input_str:
            month = 4
            input_str = input_str.replace("Thang Tu", str(month))

        if "Thang Ba" in input_str:
            month = 3
            input_str = input_str.replace("Thang Ba", str(month))

        if "Thang Hai" in input_str:
            month = 2
            input_str = input_str.replace("Thang Hai", str(month))

        if "Thang Mot" in input_str:
            month = 1
            input_str = input_str.replace("Thang Mot", str(month))

        input_str = input_str.replace(", ", " ")
        input_str = input_str.strip()

        print(input_str)
        print("==============>>>>>>>>>>>>>")
    
        try:
            if "SA" in input_str:
                    hours = 0
                    input_str = input_str.replace(" SA", "")

            if "CH" in input_str:
                hours = 12
                input_str = input_str.replace(" CH", "")

            date_rex = "\d+ \d+ \d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]

            stripped = time_str + " " + date_str
            stripped = stripped.strip()

            temp = datetime.strptime(stripped, "%H:%M %d %m %Y")
            if (hours == 12):
                timeFormat = (temp + timedelta(hours=12)).strftime(self.DATETIME_FORMAT)

            if (hours == 0):
                timeFormat = temp.strftime(self.DATETIME_FORMAT)
            return timeFormat
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hiephoixangdau.org")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_vietone(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, vietone.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_yeuthethao_thethaovanhoa(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, yeuthethao.thethaovanhoa.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_hoduongvietnam(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hoduongvietnam.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_nguoibaotroonline(self,input_str):
        input_str = str(unidecode.unidecode(input_str)).strip()
        input_str = input_str.replace("Thang","")
        try:
            date_rex = "\d+  \d+ \d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d  %m %Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, nguoibaotroonline.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_dulichthonhikyaz(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, dulichthonhikyaz.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_agribankplus(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped = date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, agribankplus.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tapchisonghuong(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tapchisonghuong.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_hoinongdanhatinh(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hoinongdanhatinh.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_nganhangvi(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, nganhangvi.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_nghesiviet(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, nghesiviet.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_dichvuthuonghieu(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, dichvuthuonghieu.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_tapchinongthonmoi(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tapchinongthonmoi.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_myvnnews(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped = date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, myvnnews.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_vietnamdaily_kienthuc(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, vietnamdaily.kienthuc.net.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_hoichannuoi(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped = date_str
            return datetime.strptime(stripped, "%m/%d/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hoichannuoi.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_congdoancaosu(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, congdoancaosu.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_giaothong24h(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, giaothong24h.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tuetamvh(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tuetamvh.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
    
    def format_otopro(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, otopro.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_yeuninhthuan(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped = date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, yeuninhthuan.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_phatgiaoquangnam(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, phatgiaoquangnam.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_doingoailaocai(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+-\d+-\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped = date_str
            return datetime.strptime(stripped, "%d-%m-%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, doingoailaocai.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_thegioivanhoa(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, thegioivanhoa.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tuyengiaobinhphuoc_org(self, input_str):
        input_str = input_str.replace("+07"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tuyengiaobinhphuoc.org.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_chungkhoanao(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, chungkhoanao.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tuyengiaokontum_org(self, input_str):
        input_str = input_str.replace("+07"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tuyengiaokontum.org.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_chopmat(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, chopmat.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_cuclamnghiep_gov(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, cuclamnghiep.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_thongtinxe(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, thongtinxe.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_xedien360(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, xedien360.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_canhsatbien(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, canhsatbien.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_tudonghoangaynay(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tudonghoangaynay.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tuoitrehaugiang_org(self, input_str):
        data = json.loads(input_str)
        input_str = data['props']['pageProps']['data']['public_date']
        try:
            input_str = input_str.replace("T", " ").replace("+07:00", " ").strip()
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tuoitrehaugiang.org.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_daututhongminh247(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, daututhongminh247.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_daibieudancukontum_gov(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+-\d+-\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped = date_str
            return datetime.strptime(stripped, "%d-%m-%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, daibieudancukontum.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_autocarvietnam(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, autocarvietnam.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tintucoto360(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tintucoto360.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_giavang(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, giavang.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_emagazine24(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, emagazine24.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_giaophankontum(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, giaophankontum.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_molistar(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, molistar.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_doisongvathuonghieu(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, doisongvathuonghieu.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_kontum_gov(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            try:
                date_rex = "\d+/\d+/\d+"
                date_str = re.findall(date_rex, input_str)[0]
                stripped = date_str
                return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
            except Exception:
                print ("[EXCEPTION] datetime converting exception, kontum.gov.vn")
                return datetime.today().strftime(self.DATETIME_FORMAT)
            
    def format_quocphongthudo(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, quocphongthudo.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tinhanghoa(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tinhanghoa.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_congchuc24h(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, congchuc24h.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_liendoanluatsu(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, liendoanluatsu.org.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tapchihangkhong(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tapchihangkhong.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_vnhot(self, input_str):
        input_str = input_str.strip()
        try:
            if "AM" in input_str:
                    hours = 0
                    input_str = input_str.replace(" AM", "")

            if "PM" in input_str:
                hours = 12
                input_str = input_str.replace(" PM", "")

            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]

            stripped = time_str + " " + date_str
            stripped = stripped.strip()

            temp = datetime.strptime(stripped, "%H:%M %d/%m/%Y")
            if (hours == 12):
                timeFormat = (temp + timedelta(hours=12)).strftime(self.DATETIME_FORMAT)

            if (hours == 0):
                timeFormat = temp.strftime(self.DATETIME_FORMAT)
            return timeFormat
        except Exception:
            print ("[EXCEPTION] datetime converting exception, vnhot.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_cafebitcoin(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, cafebitcoin.org")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_giaophandalat(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped = date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, giaophandalat.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_en_sggp(self, input_str):
        input_str = input_str.replace("T"," ").replace("+0700"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, en.sggp.org.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_khoahoctv(self, input_str):
        data = json.loads(input_str)
        input_str = data['datePublished']
        try:
            input_str = input_str.replace("T", " ").replace("+07:00", " ").strip()
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, khoahoc.tv")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_doanhnghieptoday(self, input_str):
        input_str = str(unidecode.unidecode(input_str)).strip()
        if "Thang Muoi Hai" in input_str:
            month = 12
            input_str = input_str.replace("Thang Muoi Hai", str(month))

        if "Thang Muoi Mot" in input_str:
            month = 11
            input_str = input_str.replace("Thang Muoi Mot", str(month))

        if "Thang Muoi" in input_str:
            month = 10
            input_str = input_str.replace("Thang Muoi", str(month))

        if "Thang Chin" in input_str:
            month = 9
            input_str = input_str.replace("Thang Chin", str(month))

        if "Thang Tam" in input_str:
            month = 8
            input_str = input_str.replace("Thang Tam", str(month))

        if "Thang Bay" in input_str:
            month = 7
            input_str = input_str.replace("Thang Bay", str(month))

        if "Thang Sau" in input_str:
            month = 6
            input_str = input_str.replace("Thang Sau", str(month))

        if "Thang Nam" in input_str:
            month = 5
            input_str = input_str.replace("Thang Nam", str(month))

        if "Thang Tu" in input_str:
            month = 4
            input_str = input_str.replace("Thang Tu", str(month))

        if "Thang Ba" in input_str:
            month = 3
            input_str = input_str.replace("Thang Ba", str(month))

        if "Thang Hai" in input_str:
            month = 2
            input_str = input_str.replace("Thang Hai", str(month))

        if "Thang Mot" in input_str:
            month = 1
            input_str = input_str.replace("Thang Mot", str(month))

        input_str = input_str.replace(",", "")
        input_str = input_str.strip()
        try:
            date_rex = "\d+ \d+ \d+"
            date_str = re.findall(date_rex, input_str)[0]
            stripped = date_str
            return datetime.strptime(stripped, "%d %m %Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, doanhnghieptoday.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_kenhnguoinoitieng(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, kenhnguoinoitieng.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_congdoanxaydungvn_org(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, congdoanxaydungvn.org.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_thegioinguoidep(self, input_str):
        input_str = input_str.replace("T"," ").replace(".000000+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, thegioinguoidep.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_iavvn(self, input_str):
        input_str = input_str.strip()
        try:
            if "SA" in input_str:
                hours = 0
                input_str = input_str.replace(" SA", "")

            if "CH" in input_str:
                hours = 12
                input_str = input_str.replace(" CH", "")

            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]

            stripped = time_str + " " + date_str
            stripped = stripped.strip()

            temp = datetime.strptime(stripped, "%H:%M:%S %d/%m/%Y")
            if (hours == 12):
                timeFormat = (temp + timedelta(hours=12)).strftime(self.DATETIME_FORMAT)

            if (hours == 0):
                timeFormat = temp.strftime(self.DATETIME_FORMAT)
            return timeFormat
        except Exception:
            print ("[EXCEPTION] datetime converting exception, iav.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_phunucuocsong(self, input_str):
        input_str = input_str.replace("T"," ").replace(".000000+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, phunucuocsong.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tiepthiplus(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tiepthiplus.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_vinabull(self, input_str):
        input_str = input_str.replace("T"," ").replace(".000000+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, vinabull.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_foundation_miraeasset(self,input_str):
        input_str = str(unidecode.unidecode(input_str)).strip().lower()
        try:
            if "dece" in input_str:
                month = 12
                input_str = input_str.replace("dec", str(month))

            if "nov" in input_str:
                month = 11
                input_str = input_str.replace("nov", str(month))

            if "oct" in input_str:
                month = 10
                input_str = input_str.replace("oct", str(month))

            if "sep" in input_str:
                month = 9
                input_str = input_str.replace("sep", str(month))

            if "aug" in input_str:
                month = 8
                input_str = input_str.replace("aug", str(month))

            if "jul" in input_str:
                month = 7
                input_str = input_str.replace("jul", str(month))

            if "jun" in input_str:
                month = 6
                input_str = input_str.replace("june", str(month))

            if "may" in input_str:
                month = 5
                input_str = input_str.replace("may", str(month))

            if "apr" in input_str:
                month = 4
                input_str = input_str.replace("apr", str(month))

            if "mar" in input_str:
                month = 3
                input_str = input_str.replace("mar", str(month))

            if "feb" in input_str:
                month = 2
                input_str = input_str.replace("feb", str(month))

            if "jan" in input_str:
                month = 1
                input_str = input_str.replace("jan", str(month))

            input_str = input_str.replace(",", "")
            input_str = input_str.strip()
            date_rex = "\d+ \d+ \d+"
            date_str = re.findall(date_rex,input_str)[0]
            stripped = date_str

            return datetime.strptime(stripped, "%m %d %Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, foundation.miraeasset.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_doanhnhansaoviet(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, doanhnhansaoviet.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_vda_org(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, vda.org.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tamnhin_kienthuc(self, input_str):
        input_str = input_str.replace("T"," ").replace("+0700"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tamnhin.kienthuc.net.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_doanhnhan_baophapluat(self, input_str):
        input_str = input_str.replace("T"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, doanhnhan.baophapluat.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_mafc(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, mafc.com.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_blogchiasekienthuc(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, blogchiasekienthuc.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_bancanbiet(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, bancanbiet.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_ketnoidautu(self, input_str):
        input_str = input_str.replace("T"," ").replace(".000000+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, ketnoidautu.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_doanhnhanthuonghieuviet(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, doanhnhanthuonghieuviet.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_topsao(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, topsao.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_nongthonmoiphutho(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, nongthonmoiphutho.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_congdoandsvn_org(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, congdoandsvn.org.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_1phutsaigon(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, 1phutsaigon.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_chiase2vn(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, chiase2vn.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_congdoanlaichau_org(self, input_str):
        input_str = input_str.replace("+07"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, congdoanlaichau.org.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_congdoantkv(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"  
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, congdoantkv.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_kinhtechaua(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"  
            date_str = re.findall(date_rex, input_str)[0]
            stripped =  date_str
            return datetime.strptime(stripped, "%d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, kinhtechaua.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_toasangnganh(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, toasangnganh.net")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_ttth247(self, input_str):
        input_str = input_str.replace("T"," ").replace(".276Z"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, ttth247.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_phapluatplus_baophapluat(self,input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex,input_str)[0]
            time_str = re.findall(time_rex,input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            try:
                input_str = str(unidecode.unidecode(input_str)).strip()
                input_str = input_str.replace(",", "").strip()
                input_str = input_str.replace("  ", " ").strip()
                print (str(input_str))
                if "thang" in input_str:
                    diff = timedelta(days=int(input_str[0]) * 30)
                    passed = str(passed).split(' ')[0]
                    now = datetime.now()
                    passed = now - diff
                    return passed.strftime(self.DATETIME_FORMAT)
                elif "tuan truoc" in input_str:
                    diff = timedelta(days=int(input_str[0]) * 7)
                    passed = str(passed).split(' ')[0]
                    now = datetime.now()
                    passed = now - diff
                    return passed.strftime(self.DATETIME_FORMAT)
                elif "ngay truoc" in input_str:
                    diff = timedelta(days=int(input_str[0]))
                    now = datetime.now()
                    passed = now - diff
                    return passed.strftime(self.DATETIME_FORMAT)
                elif "gio truoc" in input_str:
                    diff = timedelta(hours=int(input_str[0]))
                    now = datetime.now()
                    passed = now - diff
                    return passed.strftime(self.DATETIME_FORMAT)
                elif "phut truoc" in input_str:
                    diff = timedelta(minutes=int(input_str[0]))
                    now = datetime.now()
                    passed = now - diff
                    return passed.strftime(self.DATETIME_FORMAT)
                else:
                    str_date = input_str[2] + " " + input_str[3]
                    return datetime.strptime(str_date, "%d-%m-%Y %H:%M:%S").strftime(self.DATETIME_FORMAT)
            except Exception:
                print ("[EXCEPTION] datetime converting exception, phapluatplus.baophapluat.vn")
                return datetime.today().strftime(self.DATETIME_FORMAT)
            
    def format_hometoday(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, hometoday.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_saobiz(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, saobiz.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_thoibaonga(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, thoibaonga.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_tieudungthoinay(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tieudungthoinay.vn")

    def format_tantheky(self, input_str):
        input_str = input_str.replace("T"," ").replace("+07:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tantheky.org")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_thebanker(self, input_str):
        data = json.loads(input_str)
        input_str = data['datePublished']
        try:
            input_str = input_str.replace("T", " ").replace(".225Z", " ").strip()
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, thebanker.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_theasianbanker(self,input_str):
        input_str = str(unidecode.unidecode(input_str)).strip().lower()
        try:
            if "dece" in input_str:
                month = 12
                input_str = input_str.replace("dec", str(month))

            if "nov" in input_str:
                month = 11
                input_str = input_str.replace("nov", str(month))

            if "oct" in input_str:
                month = 10
                input_str = input_str.replace("oct", str(month))

            if "sep" in input_str:
                month = 9
                input_str = input_str.replace("sep", str(month))

            if "aug" in input_str:
                month = 8
                input_str = input_str.replace("aug", str(month))

            if "jul" in input_str:
                month = 7
                input_str = input_str.replace("jul", str(month))

            if "jun" in input_str:
                month = 6
                input_str = input_str.replace("june", str(month))

            if "may" in input_str:
                month = 5
                input_str = input_str.replace("may", str(month))

            if "apr" in input_str:
                month = 4
                input_str = input_str.replace("apr", str(month))

            if "mar" in input_str:
                month = 3
                input_str = input_str.replace("mar", str(month))

            if "feb" in input_str:
                month = 2
                input_str = input_str.replace("feb", str(month))

            if "jan" in input_str:
                month = 1
                input_str = input_str.replace("jan", str(month))

            input_str = input_str.replace(",", "")
            input_str = input_str.strip()
            date_rex = "\d+ \d+ \d+"
            date_str = re.findall(date_rex,input_str)[0]
            stripped = date_str

            return datetime.strptime(stripped, "%d %m %Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            input_str = str(unidecode.unidecode(input_str)).strip().lower()
            try:
                if "dece" in input_str:
                    month = 12
                    input_str = input_str.replace("dec", str(month))

                if "nov" in input_str:
                    month = 11
                    input_str = input_str.replace("nov", str(month))

                if "oct" in input_str:
                    month = 10
                    input_str = input_str.replace("oct", str(month))

                if "sep" in input_str:
                    month = 9
                    input_str = input_str.replace("sep", str(month))

                if "aug" in input_str:
                    month = 8
                    input_str = input_str.replace("aug", str(month))

                if "jul" in input_str:
                    month = 7
                    input_str = input_str.replace("jul", str(month))

                if "jun" in input_str:
                    month = 6
                    input_str = input_str.replace("june", str(month))

                if "may" in input_str:
                    month = 5
                    input_str = input_str.replace("may", str(month))

                if "apr" in input_str:
                    month = 4
                    input_str = input_str.replace("apr", str(month))

                if "mar" in input_str:
                    month = 3
                    input_str = input_str.replace("mar", str(month))

                if "feb" in input_str:
                    month = 2
                    input_str = input_str.replace("feb", str(month))

                if "jan" in input_str:
                    month = 1
                    input_str = input_str.replace("jan", str(month))

                input_str = input_str.replace(",", "")
                input_str = input_str.strip()
                date_rex = "\d+ \d+ \d+"
                date_str = re.findall(date_rex,input_str)[0]
                stripped = date_str

                return datetime.strptime(stripped, "%m %d %Y").strftime(self.DATETIME_FORMAT)
            except Exception:
                print ("[EXCEPTION] datetime converting exception, theasianbanker.com")
                return datetime.today().strftime(self.DATETIME_FORMAT)
            
    def format_gfmag(self, input_str):
        input_str = input_str.replace("T"," ").replace("+00:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, gfmag.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_euromoney(self, input_str):
        input_str = input_str.replace("T"," ").replace(".014"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, euromoney.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_businesstimes(self, input_str):
        input_str = input_str.replace("T"," ").replace("+08:00"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, businesstimes.com.sg")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_theasset(self,input_str):
        input_str = str(unidecode.unidecode(input_str)).strip().lower()
        try:
            if "dece" in input_str:
                month = 12
                input_str = input_str.replace("dec", str(month))

            if "nov" in input_str:
                month = 11
                input_str = input_str.replace("nov", str(month))

            if "oct" in input_str:
                month = 10
                input_str = input_str.replace("oct", str(month))

            if "sep" in input_str:
                month = 9
                input_str = input_str.replace("sep", str(month))

            if "aug" in input_str:
                month = 8
                input_str = input_str.replace("aug", str(month))

            if "jul" in input_str:
                month = 7
                input_str = input_str.replace("jul", str(month))

            if "jun" in input_str:
                month = 6
                input_str = input_str.replace("june", str(month))

            if "may" in input_str:
                month = 5
                input_str = input_str.replace("may", str(month))

            if "apr" in input_str:
                month = 4
                input_str = input_str.replace("apr", str(month))

            if "mar" in input_str:
                month = 3
                input_str = input_str.replace("mar", str(month))

            if "feb" in input_str:
                month = 2
                input_str = input_str.replace("feb", str(month))

            if "jan" in input_str:
                month = 1
                input_str = input_str.replace("jan", str(month))

            input_str = input_str.replace(",", "")
            input_str = input_str.strip()
            date_rex = "\d+ \d+ \d+"
            date_str = re.findall(date_rex,input_str)[0]
            stripped = date_str

            return datetime.strptime(stripped, "%d %m %Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, theasset.com")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_thuonghieuquocgia_nhandan(self, input_str):
        input_str = input_str.replace("T"," ").replace("+0700"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, thuonghieuquocgia.nhandan.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)
        
    def format_ktds(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, ktds.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_baoxaydungvn(self, input_str):
        input_str = input_str.strip()
        try:
            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M %d/%m/%Y").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, baoxaydung.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_tapchivietnamhuongsac(self, input_str):
        input_str = input_str.replace("T"," ").replace("+0700"," ").strip()
        try:
            date_rex = "\d+-\d+-\d+"
            time_rex = "\d+:\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]
            stripped = time_str + " " + date_str
            return datetime.strptime(stripped, "%H:%M:%S %Y-%m-%d").strftime(self.DATETIME_FORMAT)
        except Exception:
            print ("[EXCEPTION] datetime converting exception, tapchivietnamhuongsac.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)

    def format_sonoivu_hanoi_gov(self, input_str):
        input_str = input_str.replace("|"," ").strip()
        try:
            if "AM" in input_str:
                    hours = 0
                    input_str = input_str.replace(" AM", "")

            if "PM" in input_str:
                hours = 12
                input_str = input_str.replace(" PM", "")

            date_rex = "\d+/\d+/\d+"
            time_rex = "\d+:\d+"
            date_str = re.findall(date_rex, input_str)[0]
            time_str = re.findall(time_rex, input_str)[0]

            stripped = time_str + " " + date_str
            stripped = stripped.strip()

            temp = datetime.strptime(stripped, "%H:%M %d/%m/%Y")
            if (hours == 12):
                timeFormat = (temp + timedelta(hours=12)).strftime(self.DATETIME_FORMAT)

            if (hours == 0):
                timeFormat = temp.strftime(self.DATETIME_FORMAT)
            return timeFormat
        except Exception:
            print ("[EXCEPTION] datetime converting exception, sonoivu.hanoi.gov.vn")
            return datetime.today().strftime(self.DATETIME_FORMAT)