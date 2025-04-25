# -*- coding: utf-8 -*-

# //Author: Vuongnm at vuongnguyen710@gmail.com
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

__author__ = 'VuongNM'

import time, hashlib, logging, re, json

from .base_spider import BaseSpider
from .helper import Helper
from .dispatcherLib import DispatcherLibrary
from datetime import datetime
from lxml import html
from html.parser import HTMLParser
from scrapy.http import Request

class BaodanangSpider(BaseSpider):
    name = 'baodanang'
    allowed_domains = ['baodanang.vn']
    service_id  = 100000
    
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'wb.middlewares.RandomUserAgentMiddleware': 400,
            # 'wb.middlewares.RandomProxyBuyingTEST': 410,
        }
    }

class KhuyenNongvnGOVVNSpider(BaseSpider):
    name = 'khuyennongvn_gov'
    allowed_domains = ['khuyennongvn.gov.vn']
    service_id  = 100001

class DuBaoTienTeComSpider(BaseSpider):
    name = 'dubaotiente'
    allowed_domains = ['dubaotiente.com']
    service_id  = 100002

class ThongTinBankComSpider(BaseSpider):
    name = 'thongtinbank'
    allowed_domains = ['thongtinbank.com']
    service_id  = 100003

class TapChiCaoSuVNSpider(BaseSpider):
    name = 'tapchicaosu'
    allowed_domains = ['tapchicaosu.vn']
    service_id  = 100004

class HoTroNghienCuuComSpider(BaseSpider):
    name = 'hotronghiencuu'
    allowed_domains = ['hotronghiencuu.com']
    service_id  = 100005

class LamChuTaiChinhVNSpider(BaseSpider):
    name = 'lamchutaichinh'
    allowed_domains = ['lamchutaichinh.vn']
    service_id  = 100006

class NganHangazComSpider(BaseSpider):
    name = 'nganhangaz'
    allowed_domains = ['nganhangaz.com']
    service_id  = 100007

class TapChiKienTrucComVNSpider(BaseSpider):
    name = 'tapchikientruc'
    allowed_domains = ['tapchikientruc.com.vn']
    service_id  = 100008

class ChinhSachDauTuVNSpider(BaseSpider):
    name = 'chinhsachdautu'
    allowed_domains = ['chinhsachdautu.vn']
    service_id  = 100009

class TamNhinDoanhNhanVNSpider(BaseSpider):
    name = 'tamnhindoanhnhan'
    allowed_domains = ['tamnhindoanhnhan.vn']
    service_id  = 100010

class DienDanDoThiKinhTeDoThiVNSpider(BaseSpider):
    name = 'diendandothi_kinhtedothi'
    allowed_domains = ['diendandothi.kinhtedothi.vn']
    service_id  = 100011

class TinTucTienAoNetSpider(BaseSpider):
    name = 'tintuctienao'
    allowed_domains = ['tintuctienao.net']
    service_id  = 100012

class VanNgheQuanDoiComVNSpider(BaseSpider):
    name = 'vannghequandoi'
    allowed_domains = ['vannghequandoi.com.vn']
    service_id  = 100013

class ChongBanPhaGiaVNSpider(BaseSpider):
    name = 'chongbanphagia'
    allowed_domains = ['chongbanphagia.vn']
    service_id  = 100014

class KinhTeVaDauTuVNSpider(BaseSpider):
    name = 'kinhtevadautu'
    allowed_domains = ['kinhtevadautu.vn']
    service_id  = 100015

class TriTueMoiVNSpider(BaseSpider):
    name = 'trituemoi'
    allowed_domains = ['trituemoi.vn']
    service_id  = 100016

class ChuongTrinhMucTieuQuocGiaBaoDanTocVNSpider(BaseSpider):
    name = 'chuongtrinhmuctieuquocgia_baodantoc'
    allowed_domains = ['chuongtrinhmuctieuquocgia.baodantoc.vn']
    service_id  = 100017

class UyTinThuongHieuVNSpider(BaseSpider):
    name = 'uytinthuonghieu'
    allowed_domains = ['uytinthuonghieu.vn']
    service_id  = 100018

class TheGioiDiSanVNSpider(BaseSpider):
    name = 'thegioidisan'
    allowed_domains = ['thegioidisan.vn']
    service_id  = 100019

class CgvdtVNSpider(BaseSpider):
    name = 'cgvdt'
    allowed_domains = ['cgvdt.vn']
    service_id  = 100020

class QuanLyNhaNuocVNSpider(BaseSpider):
    name = 'quanlynhanuoc'
    allowed_domains = ['quanlynhanuoc.vn']
    service_id  = 100021

class TaiChinhCoBanComSpider(BaseSpider):
    name = 'taichinhcoban'
    allowed_domains = ['taichinhcoban.com']
    service_id  = 100022

class KhuyenNongKienGiangComVNSpider(BaseSpider):
    name = 'khuyennongkiengiang'
    allowed_domains = ['khuyennongkiengiang.com.vn']
    service_id  = 100023

class KienThucKinhTeVNSpider(BaseSpider):
    name = 'kienthuckinhte'
    allowed_domains = ['kienthuckinhte.vn']
    service_id  = 100024

class BlogNganHangOrgSpider(BaseSpider):
    name = 'blognganhang'
    allowed_domains = ['blognganhang.org']
    service_id  = 100025

class TapChiLaoDongXaHoiVNSpider(BaseSpider):
    name = 'tapchilaodongxahoi'
    allowed_domains = ['tapchilaodongxahoi.vn']
    service_id  = 100026

class PhapLuatPhatTrienVNSpider(BaseSpider):
    name = 'phapluatphattrien'
    allowed_domains = ['phapluatphattrien.vn']
    service_id  = 100027

class NganHangNongThonComSpider(BaseSpider):
    name = 'nganhangnongthon'
    allowed_domains = ['nganhangnongthon.com']
    service_id  = 100028

class VnTreVNSpider(BaseSpider):
    name = 'vntre'
    allowed_domains = ['vntre.vn']
    service_id  = 100029

class LapPhapVNSpider(BaseSpider):
    name = 'lapphap'
    allowed_domains = ['lapphap.vn']
    service_id  = 100030
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'wb.middlewares.RandomUserAgentMiddleware': 400,
            'wb.middlewares.RandomProxyBuyingTEST': 410,
        }
    }

class GocNhinPhapLyNguoiDuaTinVNSpider(BaseSpider):
    name = 'gocnhinphaply_nguoiduatin'
    allowed_domains = ['gocnhinphaply.nguoiduatin.vn']
    service_id  = 100031

class SSCGOVVNSpider(BaseSpider):
    name = 'ssc_gov'
    allowed_domains = ['ssc.gov.vn']
    service_id  = 100032

class DoanhNhanVaTieuDungComSpider(BaseSpider):
    name = 'doanhnhanvatieudungV2'
    allowed_domains = ['doanhnhanvatieudung.com']
    service_id  = 100033

class SaiGonEconomyNetSpider(BaseSpider):
    name = 'saigoneconomynet'
    allowed_domains = ['saigoneconomy.net']
    service_id  = 100034

class ThoiBaoVietNamNetSpider(BaseSpider):
    name = 'thoibaovietnamnet'
    allowed_domains = ['thoibaovietnam.net']
    service_id  = 100035

class TheGioiTiepThiVietNamComSpider(BaseSpider):
    name = 'thegioitiepthivietnam'
    allowed_domains = ['thegioitiepthivietnam.com']
    service_id  = 100036

class DoiThoaiPhatTrienVNSpider(BaseSpider):
    name = 'doithoaiphattrien'
    allowed_domains = ['doithoaiphattrien.vn']
    service_id  = 100037

class TheBusinessVNSpider(BaseSpider):
    name = 'thebusiness'
    allowed_domains = ['thebusiness.vn']
    service_id  = 100038
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'wb.middlewares.RandomUserAgentMiddleware': 400,
            'wb.middlewares.RandomProxyBuyingTEST': 410,
        }
    }

class KinhDoanhPlusVNSpider(BaseSpider):
    name = 'kinhdoanhplus'
    allowed_domains = ['kinhdoanhplus.vn']
    service_id  = 100039

class VnewsTodayCOMSpider(BaseSpider):
    name = 'vnewstoday'
    allowed_domains = ['vnewstoday.com']
    service_id  = 100040

class BaoBacKanVNSpider(BaseSpider):
    name = 'baobackan'
    allowed_domains = ['baobackan.vn']
    service_id  = 100041

class NewSliverSiteSpider(BaseSpider):
    name = 'newsliver_site'
    allowed_domains = ['newsliver.site']
    service_id  = 100042

class DbndhanoiGovVNSpider(BaseSpider):
    name = 'dbndhanoi_gov'
    allowed_domains = ['dbndhanoi.gov.vn']
    service_id  = 100043

class XetvVNSpider(BaseSpider):
    name = 'xetv'
    allowed_domains = ['xetv.vn']
    service_id  = 100044

class CanhCoNetSpider(BaseSpider):
    name = 'canhco'
    allowed_domains = ['canhco.net']
    service_id  = 100045

class AutotvVNSpider(BaseSpider):
    name = 'autotv'
    allowed_domains = ['autotv.vn']
    service_id  = 100046

class InfofinanceVNSpider(BaseSpider):
    name = 'infofinance'
    allowed_domains = ['infofinance.vn']
    service_id  = 100047

class DbkcqdnbacninhVNSpider(BaseSpider):
    name = 'dbkcqdnbacninh'
    allowed_domains = ['dbkcqdnbacninh.vn']
    service_id  = 100048

class BankVietComSpider(BaseSpider):
    name = 'bankviet'
    allowed_domains = ['bankviet.com']
    service_id  = 100049

class SauChinInvestVNSpider(BaseSpider):
    name = '69invest'
    allowed_domains = ['69invest.vn']
    service_id  = 100050

class TrangGameNetSpider(BaseSpider):
    name = 'tranggame'
    allowed_domains = ['tranggame.net']
    service_id  = 100051

class DoanhNhanNgayNayComSpider(BaseSpider):
    name = 'doanhnhanngaynay'
    allowed_domains = ['doanhnhanngaynay.com']
    service_id  = 100052

class BlogHuuIchComSpider(BaseSpider):
    name = 'bloghuuich'
    allowed_domains = ['bloghuuich.com']
    service_id  = 100053

class ITheThaoVNSpider(BaseSpider):
    name = 'ithethao'
    allowed_domains = ['ithethao.vn']
    service_id  = 100054
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'wb.middlewares.RandomUserAgentMiddleware': 400,
            'wb.middlewares.RandomProxyBuyingTEST': 410,
        }
    }

class HanoiTopListComSpider(BaseSpider):
    name = 'hanoitoplist'
    allowed_domains = ['hanoitoplist.com']
    service_id  = 100055

class BankCuaToiNetSpider(BaseSpider):
    name = 'bankcuatoi'
    allowed_domains = ['bankcuatoi.net']
    service_id  = 100056

class UsefulVNSpider(BaseSpider):
    name = 'useful'
    allowed_domains = ['useful.vn']
    service_id  = 100057

class Vncash24hComSpider(BaseSpider):
    name = 'vncash24h'
    allowed_domains = ['vncash24h.com']
    service_id  = 100058

class DongThapGovVNSpider(BaseSpider):
    name = 'dongthap_gov'
    allowed_domains = ['dongthap.gov.vn']
    service_id  = 100059

class TuyenGiaoPhuYenGovVNSpider(BaseSpider):
    name = 'tuyengiao_phuyen_gov'
    allowed_domains = ['tuyengiao.phuyen.gov.vn']
    service_id  = 100060
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'wb.middlewares.RandomUserAgentMiddleware': 400,
            'wb.middlewares.RandomProxyBuyingTEST': 410,
        }
    }

    def parse_full_post(self, response):
        if response.status != 200:
            print ("SERVER ERROR ON THIS URL: "+ str(response.url))
            return

#        filename = "response_debugtinnhanhnhadat.html"
#        open(filename, 'wb').write(response.body)

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
        item['web_content'] = Helper()._join_data(" ", response.selector.xpath(response.meta['xpath_config']['post_content']).extract()).replace(r" +", " ").strip().encode('utf-8')
        item['web_author'] = Helper()._join_data(",", response.selector.xpath(response.meta['xpath_config']['post_author']).extract()).strip().encode('utf-8')
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

        print ("[PARSED DATETIME]: " + item['web_created'])
        print ('[PARSED WEBTITLE]: ' + item['web_title'])
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

    def parse(self, response):
        post_urls = response.selector.xpath(response.meta['xpath_config']['post_url']).extract()
        # COUNT URL
        self.url_count += len(post_urls)
        if len(post_urls) == 0 and response.status == 200:
            self.empty_cates.append( (self.allowed_domains[0], response.meta['category_url']))
        if response.status == 404:
            print ("[ERROR] 404 cate : " + response.url)
            self.deleted_cates.append( (self.allowed_domains[0],response.meta['category_url']))

        self.visiting_cates.append((self.allowed_domains[0], response.meta['domain_id'],response.meta['category_url'], str(datetime.now())))

        cate_seen_urls = []
        domain = self.getDomainFromURL(response.url)
        for post_url in post_urls:
            meta_req = response.meta
            if (not post_url.startswith("http://") ) and (not post_url.startswith("https://")):
                if not post_url.startswith("/"):
                    post_url = "/" + post_url
                post_url = "http://"+domain+post_url
            meta_req['post_url'] = post_url
            post_url = post_url.encode("utf-8")
            if post_url not in self.visited_urls:
                if post_url not in self.media_urls:
                    string = str(post_url) + "_" + str(meta_req['domain'])
                    key_insert = hashlib.md5(str(string).decode('utf-8').encode('utf-8')).hexdigest()

                    duplicate = self.redis_exists(key_insert)
                    if duplicate == True:
                        print ("[INFO] ITEM ALREADY EXISTS DON'T REQUEST AGAIN")
                        print ("[INFO] THE KEY: " + key_insert)
                        print ("[INFO] THE WEB LINK : " + str(post_url))
                    else:
                        yield Request(post_url, callback=self.parse_full_post, meta=meta_req)
                else:
                    logging.info( "[FILTER MEDIA] request filtered " + post_url)
            else:
                logging.info( "[FILTER] request filtered " + post_url)
                self.to_update_urls.append(post_url)

            cate_seen_urls.append(post_url)
        self.seen_urls.append((response.meta['domain_id'],response.meta['category_name'],cate_seen_urls))

class HoiNhaBaoVNSpider(BaseSpider):
    name = 'hoinhabao'
    allowed_domains = ['hoinhabao.vn']
    service_id  = 100062

class DoiSongDoanhNhanVNSpider(BaseSpider):
    name = 'doisongdoanhnhan'
    allowed_domains = ['doisongdoanhnhan.vn']
    service_id  = 100063

class KimSonNinhBinhGovVNSpider(BaseSpider):
    name = 'kimson_ninhbinh_gov'
    allowed_domains = ['kimson.ninhbinh.gov.vn']
    service_id  = 100064

class C4cComVNSpider(BaseSpider):
    name = 'c4cvn'
    allowed_domains = ['c4c.com.vn']
    service_id  = 100065

class YenThanhNgheAnGovVNSpider(BaseSpider):
    name = 'yenthanh_nghean_gov'
    allowed_domains = ['yenthanh.nghean.gov.vn']
    service_id  = 100066

class SnnptntLaoCaiGovVNSpider(BaseSpider):
    name = 'snnptnt_laocai_gov'
    allowed_domains = ['snnptnt.laocai.gov.vn']
    service_id  = 100067

class CafeKinhTeVNSpider(BaseSpider):
    name = 'cafekinhte'
    allowed_domains = ['cafekinhte.vn']
    service_id  = 100068

class HoChiMinhCityGovVNSpider(BaseSpider):
    name = 'hochiminhcity_gov'
    allowed_domains = ['hochiminhcity.gov.vn']
    service_id  = 100069 

class HungHaThaiBinhGovVNSpider(BaseSpider):
    name = 'hungha_thaibinh_gov'
    allowed_domains = ['hungha.thaibinh.gov.vn']
    service_id  = 100070
    
class LaoDongVaPhapLuatLaoDongThuDoVNSpider(BaseSpider):
    name = 'laodongvaphapluat_laodongthudo'
    allowed_domains = ['laodongvaphapluat.laodongthudo.vn']
    service_id  = 100071

class HoaBinhTvVNSpider(BaseSpider):
    name = 'hoabinhtv'
    allowed_domains = ['hoabinhtv.vn']
    service_id  = 100072

class QrtVNSpider(BaseSpider):
    name = 'qrt'
    allowed_domains = ['qrt.vn']
    service_id  = 100073

class HaTinhTvVNSpider(BaseSpider):
    name = 'hatinhtv'
    allowed_domains = ['hatinhtv.vn']
    service_id  = 100074

class SputniknewsVNSpider(BaseSpider):
    name = 'sputniknews'
    allowed_domains = ['sputniknews.vn']
    service_id  = 100075

class ThieuHoaThanhHoaGovVNSpider(BaseSpider):
    name = 'thieuhoa_thanhhoa_gov'
    allowed_domains = ['thieuhoa.thanhhoa.gov.vn']
    service_id  = 100076

class ThanhGiongVNSpider(BaseSpider):
    name = 'thanhgiong'
    allowed_domains = ['thanhgiong.vn']
    service_id  = 100077

class TapChiGiaoDucEduVNSpider(BaseSpider):
    name = 'tapchigiaoduc_edu'
    allowed_domains = ['tapchigiaoduc.edu.vn']
    service_id  = 100078

class DaNangGovVNSpider(BaseSpider):
    name = 'danang_gov'
    allowed_domains = ['danang.gov.vn']
    service_id  = 100079

class CemaGovVNSpider(BaseSpider):
    name = 'cema_gov'
    allowed_domains = ['cema.gov.vn']
    service_id  = 100080

class GdsrGovVNSpider(BaseSpider):
    name = 'gdsr_gov'
    allowed_domains = ['gdsr.gov.vn']
    service_id  = 100081

class EtvQuocHoiVNSpider(BaseSpider):
    name = 'etv_quochoi'
    allowed_domains = ['etv.quochoi.vn']
    service_id  = 100082
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'wb.middlewares.RandomUserAgentMiddleware': 400,
            'wb.middlewares.RandomProxyBuyingTEST': 410,
        }
    }

class VimcCoSpider(BaseSpider):
    name = 'vimc'
    allowed_domains = ['vimc.co']
    service_id  = 100083

class HoangQuanComVNSpider(BaseSpider):
    name = 'hoangquan'
    allowed_domains = ['hoangquan.com.vn']
    service_id  = 100084

class CongDoanttttOrgVNSpider(BaseSpider):
    name = 'congdoantttt'
    allowed_domains = ['congdoantttt.org.vn']
    service_id  = 100085

class Stockvn247ComSpider(BaseSpider):
    name = 'stockvn247'
    allowed_domains = ['stockvn247.com']
    service_id  = 100086

class AtmbankingEduVNSpider(BaseSpider):
    name = 'atmbanking_edu'
    allowed_domains = ['atmbanking.edu.vn']
    service_id  = 100087

class TcnnVNSpider(BaseSpider):
    name = 'tcnn'
    allowed_domains = ['tcnn.vn']
    service_id  = 100088

class NtdvnNetSpider(BaseSpider):
    name = 'ntdvn'
    allowed_domains = ['ntdvn.net']
    service_id  = 100089

class HaiPhong24hOrgSpider(BaseSpider):
    name = 'haiphong24h'
    allowed_domains = ['haiphong24h.org']
    service_id  = 100090

class VqhHaNoiHGovVNSpider(BaseSpider):
    name = 'vqh_hanoi_gov'
    allowed_domains = ['vqh.hanoi.gov.vn']
    service_id  = 100091

class TinTucXeDienComSpider(BaseSpider):
    name = 'tintucxedien'
    allowed_domains = ['tintucxedien.com']
    service_id  = 100092
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'wb.middlewares.RandomUserAgentMiddleware': 400,
            'wb.middlewares.RandomProxyBuyingTEST': 410,
        }
    }

class DanVanHaiPhongVNSpider(BaseSpider):
    name = 'danvanhaiphong'
    allowed_domains = ['danvanhaiphong.vn']
    service_id  = 100093

class BoDePhatQuocOrgSpider(BaseSpider):
    name = 'bodephatquoc'
    allowed_domains = ['bodephatquoc.org']
    service_id  = 100094

class CongAnQuangNinhGovVNSpider(BaseSpider):
    name = 'conganquangninh_gov'
    allowed_domains = ['conganquangninh.gov.vn']
    service_id  = 100095
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'wb.middlewares.RandomUserAgentMiddleware': 400,
            'wb.middlewares.RandomProxyBuyingTEST': 410,
        }
    }

    def parse(self, response):
        post_urls = response.selector.xpath(response.meta['xpath_config']['post_url']).extract()
        # COUNT URL
        self.url_count += len(post_urls)
        if len(post_urls) == 0 and response.status == 200:
            self.empty_cates.append( (self.allowed_domains[0], response.meta['category_url']))
        if response.status == 404:
            print ("[ERROR] 404 cate : " + response.url)
            self.deleted_cates.append( (self.allowed_domains[0],response.meta['category_url']))

        self.visiting_cates.append((self.allowed_domains[0], response.meta['domain_id'],response.meta['category_url'], str(datetime.now())))

        cate_seen_urls = []
        domain = self.getDomainFromURL(response.url)
        for post_url in post_urls:
            meta_req = response.meta
            if (not post_url.startswith("http://") ) and (not post_url.startswith("https://")):
                if not post_url.startswith("/"):
                    post_url = "/" + post_url
                post_url = "http://"+domain+post_url
            meta_req['post_url'] = post_url
            post_url = post_url.encode("utf-8")
            if post_url not in self.visited_urls:
                if post_url not in self.media_urls:
                    string = str(post_url) + "_" + str(meta_req['domain'])
                    key_insert = hashlib.md5(str(string).decode('utf-8').encode('utf-8')).hexdigest()

                    duplicate = self.redis_exists(key_insert)
                    if duplicate == True:
                        print ("[INFO] ITEM ALREADY EXISTS DON'T REQUEST AGAIN")
                        print ("[INFO] THE KEY: " + key_insert)
                        print ("[INFO] THE WEB LINK : " + str(post_url))
                    else:
                        yield Request(post_url, callback=self.parse_full_post, meta=meta_req)
                else:
                    logging.info( "[FILTER MEDIA] request filtered " + post_url)
            else:
                logging.info( "[FILTER] request filtered " + post_url)
                self.to_update_urls.append(post_url)

            cate_seen_urls.append(post_url)
        self.seen_urls.append((response.meta['domain_id'],response.meta['category_name'],cate_seen_urls))

class HoiChuThapDoQuangBinhGovVNSpider(BaseSpider):
    name = 'hoichuthapdoquangbinh_gov'
    allowed_domains = ['hoichuthapdoquangbinh.gov.vn']
    service_id  = 100096

class KinhNghiemOptComSpider(BaseSpider):
    name = 'kinhnghiemopt'
    allowed_domains = ['kinhnghiemopt.com']
    service_id  = 100097

class ChungTaVNSpider(BaseSpider):
    name = 'chungta'
    allowed_domains = ['chungta.vn']
    service_id  = 100098

class VnaskComSpider(BaseSpider):
    name = 'vnask'
    allowed_domains = ['vnask.com']
    service_id  = 100099

class CachVayTienNganHangComSpider(BaseSpider):
    name = 'cachvaytiennganhang'
    allowed_domains = ['cachvaytiennganhang.com']
    service_id  = 100100

class VdcaOrgVNSpider(BaseSpider):
    name = 'vdca_org'
    allowed_domains = ['vdca.org.vn']
    service_id  = 100101

class VinanetVNSpider(BaseSpider):
    name = 'vinanet'
    allowed_domains = ['vinanet.vn']
    service_id  = 100102

class VNStockProxxComSpider(BaseSpider):
    name = 'vn_stockproxx'
    allowed_domains = ['vn.stockproxx.com']
    service_id  = 100103

class TuanGiaoGovVnSpider(BaseSpider):
    name = 'tuangiao_gov'
    allowed_domains = ['tuangiao.gov.vn']
    service_id  = 100104

class BackanGovVnSpider(BaseSpider):
    name = 'backan_gov'
    allowed_domains = ['backan.gov.vn']
    service_id  = 100105

class BanTinDoanhNghiep24hVnSpider(BaseSpider):
    name = 'bantindoanhnghiep24h'
    allowed_domains = ['bantindoanhnghiep24h.vn']
    service_id  = 100106

class BusinessTodayVnSpider(BaseSpider):
    name = 'businesstoday'
    allowed_domains = ['businesstoday.vn']
    service_id  = 100107


class NhipSongSaiGonComVnSpider(BaseSpider):
    name = 'nhipsongsaigonV2'
    allowed_domains = ['nhipsongsaigon.com.vn']
    service_id  = 100108


class TiepThiInfoVnSpider(BaseSpider):
    name = 'tiepthiinfo'
    allowed_domains = ['tiepthiinfo.vn']
    service_id  = 100109


class HoangHoaThanhHoaGovVnSpider(BaseSpider):
    name = 'hoanghoa_thanhhoa_gov'
    allowed_domains = ['hoanghoa.thanhhoa.gov.vn']
    service_id  = 100110


class DbndThanhHoaGovVnSpider(BaseSpider):
    name = 'dbndthanhhoa_gov'
    allowed_domains = ['dbndthanhhoa.gov.vn']
    service_id  = 100111
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'wb.middlewares.RandomUserAgentMiddleware': 400,
            # 'wb.middlewares.RandomProxyBuyingTEST': 410,
        }
    }

class VanvnVnSpider(BaseSpider):
    name = 'vanvn'
    allowed_domains = ['vanvn.vn']
    service_id  = 100112

class BaoTangTuoiTreVnSpider(BaseSpider):
    name = 'baotangtuoitre'
    allowed_domains = ['baotangtuoitre.vn']
    service_id  = 100113

class DbndNgheAnVnSpider(BaseSpider):
    name = 'dbndnghean'
    allowed_domains = ['dbndnghean.vn']
    service_id  = 100114

class ThvComVnSpider(BaseSpider):
    name = 'thv'
    allowed_domains = ['thv.com.vn']
    service_id  = 100115

class DanChuPhapLuatVnSpider(BaseSpider):
    name = 'danchuphapluat'
    allowed_domains = ['danchuphapluat.vn']
    service_id  = 100116

class VietNamDefenceComSpider(BaseSpider):
    name = 'vietnamdefence'
    allowed_domains = ['vietnamdefence.com']
    service_id  = 100117

class HoiNongDanNinhBinhOrgVNSpider(BaseSpider):
    name = 'hoinongdanninhbinh'
    allowed_domains = ['hoinongdanninhbinh.org.vn']
    service_id  = 100118

class HaGiangGovVNSpider(BaseSpider):
    name = 'hagiang_gov'
    allowed_domains = ['hagiang.gov.vn']
    service_id  = 100119

class TapChiNongNghiepVNSpider(BaseSpider):
    name = 'tapchinongnghiep'
    allowed_domains = ['tapchinongnghiep.vn']
    service_id  = 100120

class SucKhoeSoVNSpider(BaseSpider):
    name = 'suckhoeso'
    allowed_domains = ['suckhoeso.vn']
    service_id  = 100121

class NghienCuuQuocTeOrgSpider(BaseSpider):
    name = 'nghiencuuquocte'
    allowed_domains = ['nghiencuuquocte.org']
    service_id  = 100122

class QuyDauTuPhatTrienHaNoiGovVnSpider(BaseSpider):
    name = 'quydautuphattrien_hanoi_gov'
    allowed_domains = ['quydautuphattrien.hanoi.gov.vn']
    service_id  = 100123

class UbkttwVnSpider(BaseSpider):
    name = 'ubkttw'
    allowed_domains = ['ubkttw.vn']
    service_id  = 100124

class HoahHauDoanhNhanVietNamVnSpider(BaseSpider):
    name = 'hoahaudoanhnhanvietnam'
    allowed_domains = ['hoahaudoanhnhanvietnam.vn']
    service_id  = 100125

class TruyenThongKhoaHocVnSpider(BaseSpider):
    name = 'truyenthongkhoahoc'
    allowed_domains = ['truyenthongkhoahoc.vn']
    service_id  = 100126

class BaoHaiPhongVnSpider(BaseSpider):
    name = 'baohaiphongV2'
    allowed_domains = ['baohaiphong.vn']
    service_id  = 100127

class TriAnLietSiVnSpider(BaseSpider):
    name = 'trianlietsi'
    allowed_domains = ['trianlietsi.vn']
    service_id  = 100128  

class BongDaDoiSongVnSpider(BaseSpider):
    name = 'bongdadoisong'
    allowed_domains = ['bongdadoisong.vn']
    service_id  = 100129  

class Oto365NetSpider(BaseSpider):
    name = 'oto365'
    allowed_domains = ['oto365.net']
    service_id  = 100130

class TinTheThaoComVNSpider(BaseSpider):
    name = 'tinthethao'
    allowed_domains = ['tinthethao.com.vn']
    service_id  = 100131

class ThienNhienMoiTruongVNSpider(BaseSpider):
    name = 'thiennhienmoitruong'
    allowed_domains = ['thiennhienmoitruong.vn']
    service_id  = 100132

class FinLogVNSpider(BaseSpider):
    name = 'finlog'
    allowed_domains = ['finlog.vn']
    service_id  = 100133

class BankSoVNSpider(BaseSpider):
    name = 'bankso'
    allowed_domains = ['bankso.vn']
    service_id  = 100134

class BizLifeVNSpider(BaseSpider):
    name = 'bizlife'
    allowed_domains = ['bizlife.vn']
    service_id  = 100135

class NxbctqgOrgVNSpider(BaseSpider):
    name = 'nxbctqg'
    allowed_domains = ['nxbctqg.org.vn']
    service_id  = 100136

class CucThuyLoiGovVNSpider(BaseSpider):
    name = 'cucthuyloi'
    allowed_domains = ['cucthuyloi.gov.vn']
    service_id  = 100137

class KinhDoanhPlusComSpider(BaseSpider):
    name = 'kinhdoanhplusV2'
    allowed_domains = ['kinhdoanhplus.com']
    service_id  = 100138

class XayDungGovVNSpider(BaseSpider):
    name = 'xaydung_gov'
    allowed_domains = ['xaydung.gov.vn']
    service_id  = 100139

class DuongHaiChieuInfoSpider(BaseSpider):
    name = 'duonghaichieu'
    allowed_domains = ['duonghaichieu.info']
    service_id  = 100140

class ThuongHieuDuLuanVNSpider(BaseSpider):
    name = 'thuonghieuduluan'
    allowed_domains = ['thuonghieuduluan.vn']
    service_id  = 100141

class TradingViewComVNSpider(BaseSpider):
    name = 'tradingview'
    allowed_domains = ['tradingview.com.vn']
    service_id  = 100142

class TradingViewComVNSpider(BaseSpider):
    name = 'tradingview'
    allowed_domains = ['tradingview.com.vn']
    service_id  = 100143

class KhcnCongThuongVNSpider(BaseSpider):
    name = 'khcncongthuong'
    allowed_domains = ['khcncongthuong.vn']
    service_id  = 100144

class TietKiemNangLuongComVNSpider(BaseSpider):
    name = 'tietkiemnangluong'
    allowed_domains = ['tietkiemnangluong.com.vn']
    service_id  = 100145

class ThanhHoaDcsVNSpider(BaseSpider):
    name = 'thanhhoa_dcs'
    allowed_domains = ['thanhhoa.dcs.vn']
    service_id  = 100146

class ThoiBaoDESpider(BaseSpider):
    name = 'thoibao_de'
    allowed_domains = ['thoibao.de']
    service_id  = 100147

class Tintuc24hVIPSpider(BaseSpider):
    name = 'tintuc24h_vip'
    allowed_domains = ['tintuc24h.vip']
    service_id  = 100148

class HoiChieuSangVietNamOrgVNSpider(BaseSpider):
    name = 'hoichieusangvietnam'
    allowed_domains = ['hoichieusangvietnam.org.vn']
    service_id  = 100149

class KenhKinhTeVNSpider(BaseSpider):
    name = 'kenhkinhtevn'
    allowed_domains = ['kenhkinhte.vn']
    service_id  = 100150

class Coin98NetSpider(BaseSpider):
    name = 'coin98'
    allowed_domains = ['coin98.net']
    service_id  = 100151

class DocBaoMoiNetSpider(BaseSpider):
    name = 'docbaomoi'
    allowed_domains = ['docbaomoi.net']
    service_id  = 100152

class EHoiNhapVanHoaVaPhatTrienVNSpider(BaseSpider):
    name = 'ehoinhap_vanhoavaphattrien'
    allowed_domains = ['ehoinhap.vanhoavaphattrien.vn']
    service_id  = 100153

class YboxVNSpider(BaseSpider):
    name = 'ybox'
    allowed_domains = ['ybox.vn']
    service_id  = 100154

    # def parse(self, response):
    #     post_urls = response.selector.xpath(response.meta['xpath_config']['post_url']).extract()
    #     print (post_urls)
    #     print ("=============>>>>>>>>>>>>>>")
        # COUNT URL
        # self.url_count += len(post_urls)
        # if len(post_urls) == 0 and response.status == 200:
        #     self.empty_cates.append( (self.allowed_domains[0], response.meta['category_url']))
        # if response.status == 404:
        #     print "[ERROR] 404 cate : " + response.url
        #     self.deleted_cates.append( (self.allowed_domains[0],response.meta['category_url']))

        # self.visiting_cates.append((self.allowed_domains[0], response.meta['domain_id'],response.meta['category_url'], str(datetime.now())))

        # cate_seen_urls = []
        # domain = self.getDomainFromURL(response.url)
        # for post_url in post_urls:
        #     meta_req = response.meta
        #     if (not post_url.startswith("http://") ) and (not post_url.startswith("https://")):
        #         if not post_url.startswith("/"):
        #             post_url = "/" + post_url
        #         post_url = "http://"+domain+post_url
        #     meta_req['post_url'] = post_url
        #     post_url = post_url.encode("utf-8")
        #     if post_url not in self.visited_urls:
        #         if post_url not in self.media_urls:
        #             string = str(post_url) + "_" + str(meta_req['domain'])
        #             key_insert = hashlib.md5(str(string).decode('utf-8').encode('utf-8')).hexdigest()

        #             duplicate = self.redis_exists(key_insert)
        #             if duplicate == True:
        #                 print "[INFO] ITEM ALREADY EXISTS DON'T REQUEST AGAIN"
        #                 print "[INFO] THE KEY: " + key_insert
        #                 print "[INFO] THE WEB LINK : " + str(post_url)
        #             else:
        #                 yield Request(post_url, callback=self.parse_full_post, meta=meta_req)
        #         else:
        #             logging.info( "[FILTER MEDIA] request filtered " + post_url)
        #     else:
        #         logging.info( "[FILTER] request filtered " + post_url)
        #         self.to_update_urls.append(post_url)

        #     cate_seen_urls.append(post_url)
        # self.seen_urls.append((response.meta['domain_id'],response.meta['category_name'],cate_seen_urls))


class IcomComVNSpider(BaseSpider):
    name = 'icom'
    allowed_domains = ['icom.com.vn']
    service_id  = 100155

class DnvnComVNSpider(BaseSpider):
    name = 'dnvn'
    allowed_domains = ['dnvn.com.vn']
    service_id  = 100156

class DiaOcThoiBaoComSpider(BaseSpider):
    name = 'diaocthoibao'
    allowed_domains = ['diaocthoibao.com']
    service_id  = 100157

class HaiLuaComSpider(BaseSpider):
    name = '2lua'
    allowed_domains = ['2lua.com']
    service_id  = 100158

class BongDaPhuiNetSpider(BaseSpider):
    name = 'bongdaphui'
    allowed_domains = ['bongdaphui.net']
    service_id  = 100159

class TruyenThongTreVNSpider(BaseSpider):
    name = 'truyenthongtre'
    allowed_domains = ['truyenthongtre.vn']
    service_id  = 100160

class DtckComVNSpider(BaseSpider):
    name = 'dtck'
    allowed_domains = ['dtck.com.vn']
    service_id  = 100161

class DuLichGiaiTriVNSpider(BaseSpider):
    name = 'dulichgiaitriV2'
    allowed_domains = ['dulichgiaitri.vn']
    service_id  = 100162

class CongAnHoaBinhVNSpider(BaseSpider):
    name = 'congan_hoabinh'
    allowed_domains = ['congan.hoabinh.gov.vn']
    service_id = 100163
    
    # def start_requests(self):

    #     print "==="
    #     print "BEGIN CRAWLER WEBSITE " + self.allowed_domains[0]
    #     print "==="

    #     page = 1
    #     cf_domain = self.allowed_domains[0]
    #     parser_xpath = self.get_xpaths()
    #     # parser_xpath = self.get_xpaths_mysql()
    #     # if parser_xpath:
    #     #     print "[INFO] GET XPATH IN DB"
    #     # else:
    #     #     print "[INFO] GET XPATH IN FILE CFG"
    #     #     parser_xpath = self.get_xpaths()

    #     if parser_xpath:
    #         if self.crawl_one_url == None and self.crawl_one_cate == None :

    #             list_data = DispatcherLibrary(self.service_id, self.group).getCateUrls(cf_domain)
    #             if len(list_data) > 0:
    #                 i = 1
    #                 for row in list_data:
    #                     id, domain_url, category_name, domain_name, domain_group, status, created, pay_category = row
    #                     if i == 1:
    #                         self.url_category_first = domain_url
    #                         if self.url_category_first != "":
    #                             i += 1

    #                     meta = {"domain": cf_domain, "xpath_config": parser_xpath, "domain_id": id, "category_name": category_name, "category_url": domain_url, "pay": pay_category}
    #                     print domain_url
    #                     yield Request(domain_url,meta=meta,callback=self.parse)
    #             else:
    #                 #LOG SPIDER NOT CATEGORY
    #                 print "[INFO] LOG SPIDER NOT CATEGORY"
    #                 filename = "logs-no-category.txt"
    #                 log_text = "Domain: "+ cf_domain+" --- Spider Name: "+self.name+"\n"
    #                 open(filename, 'a+').write(log_text)

    #         elif self.crawl_one_url != None and self.crawl_one_cate == None :

    #             url_post_api = "https://congan.hoabinh.gov.vn/api/pub/articles/slug?slug=" +self.crawl_one_url.split("articles/")[1]+"&pageSize=5"
    #             # print(url_post_api)
    #             # print("================= WWTF ")
    #             meta = {
    #                 'post_url': self.crawl_one_url,
    #                 "xpath_config": parser_xpath,
    #                 "domain": self.allowed_domains[0],
    #                 "domain_id": 1,
    #                 "category_name": self.name,
    #                 "category_url": self.allowed_domains[0],
    #                 "pay":0
    #             }
    #             if self.crawl_one_url in self.visited_urls:
    #                 print "[INFO] url exists in pre-request filter"
    #             else:
    #                 print "[INFO] url NOT exists in pre-request filter"

    #             if self.is_debug_scrape != None:
    #                 yield Request(self.crawl_one_url, callback = self.parse_full_post_for_debug, meta=meta)
    #                 print self.is_debug_scrape
    #             else:
    #                 if self.is_debug_again != None:
    #                     string = str(self.crawl_one_url.encode('utf-8')) + "_" + str(self.allowed_domains[0])
    #                     key_insert = hashlib.md5(str(string).decode('utf-8').encode('utf-8')).hexdigest()
    #                     duplicate = self.redis_exists(key_insert)
    #                     if duplicate == True:
    #                         print "[INFO][DEBUG] ITEM ALREADY EXISTS DON'T REQUEST AGAIN"
    #                         print "[INFO][DEBUG] THE KEY: " + key_insert
    #                         self.delete_key_to_redis(key_insert)
    #                 yield Request(url_post_api, callback = self.parse_full_post , meta=meta)

    #         elif self.crawl_one_url == None and self.crawl_one_cate != None :
    #             while True:
    #                 list_data = DispatcherLibrary(self.service_id, self.group).getUrlLeech(cf_domain, self.group, page)
    #                 if len(list_data) > 0:
    #                     for row in list_data:
    #                         id, domain_url, category_name, domain_name, domain_group, status, created, pay_category = row
    #                         meta = {"domain": cf_domain, "xpath_config": parser_xpath, "domain_id": id, "category_name": category_name, "category_url": domain_url, "pay": pay_category}
    #                         if domain_url == self.crawl_one_cate:

    #                             print "==="
    #                             print domain_url
    #                             print "==="

    #                             yield Request(domain_url,meta=meta,callback=self.parse)
    #                 else:
    #                     break
    #                 page = page + 1
    #         else:
    #             print "[ERROR] pass url OR cate, not both of them "
    #     else:
    #         print "[ERROR] GET XPATH IN DB ERROR!!! "  

    # def remove_accent(self, text):
    #     return unidecode.unidecode(text)

    # def slugify(self, s):
    #     s = s.lower().strip()
    #     s = re.sub(r'[^\w\s-]', '', s)
    #     s = re.sub(r'[\s_-]+', '-', s)
    #     s = re.sub(r'^-+|-+$', '', s)
    #     return s

    # def parse(self, response):
    #     meta_req = response.meta
    #     res = json.loads(response.body)
    #     if len(res['rows']) > 0:
    #         datas = res['rows']
    #         for row in datas:
    #             post_url = "https://congan.hoabinh.gov.vn/articles/" + row['slug']
    #             meta_req['post_url'] = post_url
    #             string = str(post_url.encode('utf-8')) + "_" + str(meta_req['domain'])
    #             key_insert = hashlib.md5(str(string).decode('utf-8').encode('utf-8')).hexdigest()
    #             duplicate = self.redis_exists(key_insert)
    #             if duplicate == True:
    #                 print "[INFO] ITEM ALREADY EXISTS DON'T REQUEST AGAIN"
    #                 print "[INFO] THE KEY: " + key_insert
    #                 print "[INFO] THE WEB LINK : " + str(post_url.encode("utf-8"))
    #             else:
    #                 meta_req["post_url_rq"] = post_url
    #                 url_post_api = "https://congan.hoabinh.gov.vn/api/pub/articles/slug?slug="+row['slug']+"&pageSize=5"
    #                 yield Request(url_post_api, callback=self.parse_full_post, meta=meta_req)

    # def parse_full_post(self, response):
       
    #     # print "============== PARSE REQUEST =============="
    #     # print str(meta_req["post_url_rq"])
    #     # print "============================================"

    #     if response.status != 200:
    #         print "SERVER ERROR ON THIS URL: "+ str(response.url) 
    #         return  
        
    #     res_body = json.loads(response.body)
        
    #     if len(res_body) == 0:
    #         return

    #     item = Helper().getItem()
    #     item['web_parent_id'] = 0
    #     item['web_grand_parent_id'] = 0
    #     item['web_cid'] = 0
    #     item['web_id'] = 0
    #     item['web_title'] = res_body["article"]["title"]
    #     item['web_lead'] = res_body["article"]["title"]
    #     c = res_body["article"]["content"]
    #     item['web_content'] = Helper().sub(r"<[^>]*>", "", c).strip().encode('utf-8')
    #     # item['web_content'] = data_post_header["content"]
    #     item['web_author'] = 0
    #     item['web_author_link'] = ""
    #     item['web_image'] = 0

    #     print (item['web_content'])
    #     print ("=========>>>>>>>>>>>>")
            
        # item['web_category_name'] = response.meta['category_name'].strip().encode("utf-8")
        # item['web_category_url'] = response.meta['category_url'].strip().encode('utf-8')
        # # get like count
        # item['web_like_count'] = 0
        # item['web_share_count'] = 0
        # item['web_child_count'] = 0
        # item['web_url_comment'] = ""

        # item['web_link'] = response.meta['post_url_rq'].strip().encode('utf-8')
        # item['web_domain_id'] = response.meta['domain_id']
        # item['web_domain_name'] = response.meta['domain']
        # item['web_post_type'] = 0
        # item['web_branch'] = ""
        # item['web_sub_branch'] = ""
        # item['web_is_crawled'] = 0
        # item['web_crawler_time'] = int(time.time())
        # item['web_created'] = datetime.fromtimestamp(data_post_header["published_date"]).strftime("%Y-%m-%d %H:%M:%S")

        # item['web_tag'] = ""
        # item['web_group'] = self.group
        # item['web_type'] = 0
        # item['web_price'] = self.article_price(item,response.meta["pay"])

        # print "[PARSED DATETIME]: " + item['web_created']
        # print '[PARSED WEBTITLE]: ' + item['web_title'] 
        # if self.crawl_one_url != None:
        #     print "[PARSED CONTENT] ---------------------------------------"
        #     print item['web_content']
        #     print "---------------------------------------"
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

        # # print(item)
        # yield item

class TapChiDoanhNghiepComSpider(BaseSpider):
    name = 'tapchidoanhnghiep'
    allowed_domains = ['xn--tpchdoanhnghiep-7ob8730k.com']
    service_id = 100164

class BietThuLienKeInfoSpider(BaseSpider):
    name = 'bietthulienke'
    allowed_domains = ['bietthulienke.info']
    service_id = 100165

class PhanTichChungKhoanNetSpider(BaseSpider):
    name = 'phantichchungkhoan'
    allowed_domains = ['phantichchungkhoan.net']
    service_id = 100166

class TrungTamNhietDoiVietNgaComVNSpider(BaseSpider):
    name = 'trungtamnhietdoivietnga'
    allowed_domains = ['trungtamnhietdoivietnga.com.vn']
    service_id = 100167

class HamiOrgVNSpider(BaseSpider):
    name = 'hami_org'
    allowed_domains = ['hami.org.vn']
    service_id = 100168

class TapChiLaoVietOrgSpider(BaseSpider):
    name = 'tapchilaoviet'
    allowed_domains = ['tapchilaoviet.org']
    service_id = 100169

class BdsCuaTuiComSpider(BaseSpider):
    name = 'bdscuatui'
    allowed_domains = ['bdscuatui.com']
    service_id = 100170

class HiepHoiXangDauOrgSpider(BaseSpider):
    name = 'hiephoixangdau'
    allowed_domains = ['hiephoixangdau.org']
    service_id = 100171

class VietOneVNSpider(BaseSpider):
    name = 'vietone'
    allowed_domains = ['vietone.vn']
    service_id = 100172

class YeuTheThaoTheThaoVanHoaVNSpider(BaseSpider):
    name = 'yeuthethao_thethaovanhoa'
    allowed_domains = ['yeuthethao.thethaovanhoa.vn']
    service_id = 100173

class HoDuongVietNamComVNSpider(BaseSpider):
    name = 'hoduongvietnam'
    allowed_domains = ['hoduongvietnam.com.vn']
    service_id = 100174

class NguoiBaoTroOnlineVNSpider(BaseSpider):
    name = 'nguoibaotroonline'
    allowed_domains = ['nguoibaotroonline.vn']
    service_id = 100175

class DuLichThoNhiKyazComSpider(BaseSpider):
    name = 'dulichthonhikyaz'
    allowed_domains = ['dulichthonhikyaz.com']
    service_id = 100176

class AgribankPlusVNSpider(BaseSpider):
    name = 'agribankplus'
    allowed_domains = ['agribankplus.vn']
    service_id = 100177

class TapChiSongHuongComVNSpider(BaseSpider):
    name = 'tapchisonghuong'
    allowed_domains = ['tapchisonghuong.com.vn']
    service_id = 100178

class HoiNongDanHaTinhVNSpider(BaseSpider):
    name = 'hoinongdanhatinh'
    allowed_domains = ['hoinongdanhatinh.vn']
    service_id = 100179

class NganHangViComSpider(BaseSpider):
    name = 'nganhangvi'
    allowed_domains = ['nganhangvi.com']
    service_id = 100180

class NgheSiVietVNSpider(BaseSpider):
    name = 'nghesiviet'
    allowed_domains = ['nghesiviet.vn']
    service_id = 100181

class DichVuThuongHieuVNSpider(BaseSpider):
    name = 'dichvuthuonghieu'
    allowed_domains = ['dichvuthuonghieu.vn']
    service_id = 100182

class TapChiNongThonMoiVNSpider(BaseSpider):
    name = 'tapchinongthonmoi'
    allowed_domains = ['tapchinongthonmoi.vn']
    service_id = 100183

class MyVNNewsComSpider(BaseSpider):
    name = 'myvnnews'
    allowed_domains = ['myvnnews.com']
    service_id = 100184

class VietNamDailyKienThucNetVNSpider(BaseSpider):
    name = 'vietnamdaily_kienthuc'
    allowed_domains = ['vietnamdaily.kienthuc.net.vn']
    service_id = 100185

class HoiChanNuoiVNSpider(BaseSpider):
    name = 'hoichannuoi'
    allowed_domains = ['hoichannuoi.vn']
    service_id = 100186

class CongDoanCaoSuVNSpider(BaseSpider):
    name = 'congdoancaosu'
    allowed_domains = ['congdoancaosu.vn']
    service_id = 100187

class KhuyenNongHaiPhongGovVNSpider(BaseSpider):
    name = 'khuyennonghaiphong_gov'
    allowed_domains = ['khuyennonghaiphong.gov.vn']
    service_id = 100188

class GiaoThong24hVNSpider(BaseSpider):
    name = 'giaothong24h'
    allowed_domains = ['giaothong24h.vn']
    service_id = 100189

class TueTamvhComSpider(BaseSpider):
    name = 'tuetamvh'
    allowed_domains = ['tuetamvh.com']
    service_id = 100190

class OtoProComVNSpider(BaseSpider):
    name = 'otopro'
    allowed_domains = ['otopro.com.vn']
    service_id = 100191

class YeuNinhThuanNetSpider(BaseSpider):
    name = 'yeuninhthuan'
    allowed_domains = ['yeuninhthuan.net']
    service_id = 100192

class PhatGiaoQuangNamComSpider(BaseSpider):
    name = 'phatgiaoquangnam'
    allowed_domains = ['phatgiaoquangnam.com']
    service_id = 100193

class DoiNgoaiLaoCaiVNSpider(BaseSpider):
    name = 'doingoailaocai'
    allowed_domains = ['doingoailaocai.vn']
    service_id = 100194

class TheGioiVanHoaNetSpider(BaseSpider):
    name = 'thegioivanhoa'
    allowed_domains = ['thegioivanhoa.net']
    service_id = 100195

class TuyenGiaoBinhPhuocOrgVNSpider(BaseSpider):
    name = 'tuyengiaobinhphuoc_org'
    allowed_domains = ['tuyengiaobinhphuoc.org.vn']
    service_id = 100196

class ChungKhoanAoComSpider(BaseSpider):
    name = 'chungkhoanao'
    allowed_domains = ['chungkhoanao.com']
    service_id = 100197

class TuyenGiaoKonTumOrgVNSpider(BaseSpider):
    name = 'tuyengiaokontum_org'
    allowed_domains = ['tuyengiaokontum.org.vn']
    service_id = 100198

class ChopMatComSpider(BaseSpider):
    name = 'chopmat'
    allowed_domains = ['chopmat.com']
    service_id = 100199

class CucLamNghiepGovVNSpider(BaseSpider):
    name = 'cuclamnghiep_gov'
    allowed_domains = ['cuclamnghiep.gov.vn']
    service_id = 100200

class ThongTinXeNetSpider(BaseSpider):
    name = 'thongtinxe'
    allowed_domains = ['thongtinxe.net']
    service_id = 100201

class XeDien360ComSpider(BaseSpider):
    name = 'xedien360'
    allowed_domains = ['xedien360.com']
    service_id = 100202
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'wb.middlewares.RandomUserAgentMiddleware': 400,
            'wb.middlewares.RandomProxyBuyingTEST': 410,
        }
    }

class CanhSatBienVNSpider(BaseSpider):
    name = 'canhsatbien'
    allowed_domains = ['canhsatbien.vn']
    service_id = 100203
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'wb.middlewares.RandomUserAgentMiddleware': 400,
            'wb.middlewares.RandomProxyBuyingTEST': 410,
        }
    }

    def start_requests(self):
        page = 1
        cf_domain = self.allowed_domains[0]
        parser_xpath = self.get_xpaths()

        if self.crawl_one_url == None and self.crawl_one_cate == None :

            list_data = DispatcherLibrary(self.service_id, self.group).getCateUrls(cf_domain)
            if len(list_data) > 0:
                for row in list_data:
                    id, domain_url, category_name, domain_name, domain_group, status, created, pay_category = row
                    meta = {"domain": cf_domain, "xpath_config": parser_xpath, "domain_id": id, "category_name": category_name, "category_url": domain_url, "pay": pay_category, "dont_redirect": "True"}
                    print (domain_url)
                    yield Request(domain_url,meta=meta,callback=self.parse)

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
                yield Request(self.crawl_one_url, callback = self.parse_full_post_for_debug,  meta=meta)
            else:
                yield Request(self.crawl_one_url, callback = self.parse_full_post, meta=meta)

        elif self.crawl_one_url == None and self.crawl_one_cate != None :
            while True:
                list_data = DispatcherLibrary(self.service_id, self.group).getUrlLeech(cf_domain, self.group, page)
                if len(list_data) > 0:
                    for row in list_data:
                        id, domain_url, category_name, domain_name, domain_group, status, created, pay_category = row
                        meta = {"domain": cf_domain, "xpath_config": parser_xpath, "domain_id": id, "category_name": category_name, "category_url": domain_url, "pay": pay_category, "dont_redirect": "True"}
                        if domain_url == self.crawl_one_cate:
                            yield Request(domain_url,meta=meta,callback=self.parse)
                else:
                    break
                page = page + 1
        else:
            print ("[ERROR] pass url OR cate, not both of them ")

    def parse(self, response):
        meta_req = response.meta
        res = json.loads(response.body)
        if len(res['listItem']) > 0:
            datas = res['listItem']
            meta_req['alias'] = res['alias']
            for row in datas:
                post_url = "https://canhsatbien.vn/"+ str(row['alias'])+"/" + str(row['id'])+ "/" + str(row['catID'])
                meta_req['post_url'] = post_url
                string = str(post_url.encode('utf-8')) + "_" + str(meta_req['domain'])
                key_insert = hashlib.md5(str(string).decode('utf-8').encode('utf-8')).hexdigest()
                duplicate = self.redis_exists(key_insert)
                if duplicate == True:
                    print ("[INFO] ITEM ALREADY EXISTS DON'T REQUEST AGAIN")
                    print ("[INFO] THE KEY: " + key_insert)
                    print ("[INFO] THE WEB LINK : " + str(post_url.encode("utf-8")))
                else:
                    meta_req["post_url_rq"] = post_url
                    url_post_api = "https://api.canhsatbien.vn/Portal/ArticleDetail?itemId=" + str(row['id'])
                    yield Request(url_post_api, callback=self.parse_full_post, meta=meta_req)

    def parse_full_post(self, response):
        # print "============== PARSE REQUEST =============="
        # print str(meta_req["post_url_rq"])
        # print "============================================"

        if response.status != 200:
            print ("SERVER ERROR ON THIS URL: "+ str(response.url) )
            return  
        
        res_body = json.loads(response.body)
        if len(res_body) == 0:
            return

        item = Helper().getItem()
        item['web_parent_id'] = 0
        item['web_grand_parent_id'] = 0
        item['web_cid'] = 0
        item['web_id'] = 0
        item['web_title'] = res_body["title"]
        item['web_lead'] = res_body["introText"]

        html_parser = HTMLParser()
        c = res_body["fullText"]
        tree = html.fromstring(c)
        clean_text = ''.join(tree.xpath('//text()'))
        clean_text = html_parser.unescape(clean_text)
        clean_text = clean_text.strip()
        item['web_content'] = clean_text.encode('utf-8')
        # item['web_content'] = data_post_header["content"]
        item['web_author'] = 0
        item['web_author_link'] = ""
        item['web_image'] = 0
            
        item['web_category_name'] = response.meta['category_name'].strip().encode("utf-8")
        item['web_category_url'] = response.meta['category_url'].strip().encode('utf-8')
        # get like count
        item['web_like_count'] = 0
        item['web_share_count'] = 0
        item['web_child_count'] = 0
        item['web_url_comment'] = ""    
        item['web_link'] = "https://canhsatbien.vn/" + response.meta['alias'] + "/" + str(res_body["id"])+ "/" + str(res_body["catId"])
        item['web_domain_id'] = response.meta['domain_id']
        item['web_domain_name'] = response.meta['domain']
        item['web_post_type'] = 0
        item['web_branch'] = ""
        item['web_sub_branch'] = ""
        item['web_is_crawled'] = 0
        item['web_crawler_time'] = int(time.time())
        datePost = res_body["datePost"]
        item['web_created'] = (datetime.strptime(datePost, "%Y-%m-%dT%H:%M:%S")).strftime("%Y-%m-%d %H:%M:%S")

        item['web_tag'] = ""
        item['web_group'] = self.group
        item['web_type'] = 0
        item['web_price'] = self.article_price(item,response.meta["pay"])

        print ("[PARSED DATETIME]: " + item['web_created'])
        print ('[PARSED WEBTITLE]: ' + item['web_title'] )
        if self.crawl_one_url != None:
            print ("[PARSED CONTENT] ---------------------------------------")
            print( item['web_content'])
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

        # print(item)
        yield item

class TuDongHoaNgayNayVNSpider(BaseSpider):
    name = 'tudonghoangaynay'
    allowed_domains = ['tudonghoangaynay.vn']
    service_id = 100204
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'wb.middlewares.RandomUserAgentMiddleware': 400,
            'wb.middlewares.RandomProxyBuyingTEST': 410,
        }
    }

class TuoiTreHauGiangOrgVNSpider(BaseSpider):
    name = 'tuoitrehaugiang_org'
    allowed_domains = ['tuoitrehaugiang.org.vn']
    service_id = 100205
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'wb.middlewares.RandomUserAgentMiddleware': 400,
            'wb.middlewares.RandomProxyBuyingTEST': 410,
        }
    }

    def start_requests(self):
        page = 1
        cf_domain = self.allowed_domains[0]
        parser_xpath = self.get_xpaths()

        if self.crawl_one_url == None and self.crawl_one_cate == None :
            list_data = DispatcherLibrary(self.service_id, self.group).getCateUrls(cf_domain)
            if len(list_data) > 0:
                for row in list_data:
                    id, domain_url, category_name, domain_name, domain_group, status, created, pay_category = row
                    meta = {"domain": cf_domain, "xpath_config": parser_xpath, "domain_id": id, "category_name": category_name, "category_url": domain_url, "pay": pay_category, "dont_redirect": "True"}
                    match = re.search(r'/(\d+)$', meta['category_url'])
                    match = match.group(1)
                    
                    headers = {
                        'accept': 'application/json, text/plain, */*',
                        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                        'cache-control': 'no-cache',
                        'content-type': 'application/json;charset=UTF-8',
                        'cookie': '__zi=3000.SSZzejyD3CiaW_sbrGmPp2Q2_RxLInVG9eBaef19GyveZFpXp5j9qNhExlVS45YMDCNjlv4RN9ipoQMsaHeOcpJ5gx6P5HoT.1',
                        'origin': 'https://tuoitrehaugiang.org.vn',
                        'pragma': 'no-cache',
                        'priority': 'u=1, i',
                        'referer': 'https://tuoitrehaugiang.org.vn/chuyen-muc/hoc-tap-va-lam-theo-loi-bac',
                        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
                    }

                    body = {
                        "page": 1,
                        "pageSize": 5,
                        "filters": {
                            "category_id": match
                        }
                    }

                    yield Request(domain_url,method='POST',headers=headers,meta=meta,callback=self.parse, body=json.dumps(body))
                    # yield Request(domain_url,meta=meta,callback=self.parse)

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
                yield Request(self.crawl_one_url, callback = self.parse_full_post_for_debug,  meta=meta)
            else:
                yield Request(self.crawl_one_url, callback = self.parse_full_post, meta=meta)

        elif self.crawl_one_url == None and self.crawl_one_cate != None :
            while True:
                list_data = DispatcherLibrary(self.service_id, self.group).getUrlLeech(cf_domain, self.group, page)
                if len(list_data) > 0:
                    for row in list_data:
                        id, domain_url, category_name, domain_name, domain_group, status, created, pay_category = row
                        meta = {"domain": cf_domain, "xpath_config": parser_xpath, "domain_id": id, "category_name": category_name, "category_url": domain_url, "pay": pay_category, "dont_redirect": "True"}
                        match = re.search(r'/(\d+)$', meta['category_url'])
                        match = match.group(1)
                        headers = {
                            'accept': 'application/json, text/plain, */*',
                            'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                            'cache-control': 'no-cache',
                            'content-type': 'application/json;charset=UTF-8',
                            'cookie': '__zi=3000.SSZzejyD3CiaW_sbrGmPp2Q2_RxLInVG9eBaef19GyveZFpXp5j9qNhExlVS45YMDCNjlv4RN9ipoQMsaHeOcpJ5gx6P5HoT.1',
                            'origin': 'https://tuoitrehaugiang.org.vn',
                            'pragma': 'no-cache',
                            'priority': 'u=1, i',
                            'referer': 'https://tuoitrehaugiang.org.vn/chuyen-muc/hoc-tap-va-lam-theo-loi-bac',
                            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
                        }

                        body = {
                            "page": 1,
                            "pageSize": 5,
                            "filters": {
                                "category_id": match
                            }
                        }
                        if domain_url == self.crawl_one_cate:
                            yield Request(domain_url,method='POST',headers=headers,meta=meta,callback=self.parse, body=json.dumps(body))
                else:
                    break
                page = page + 1
        else:
            print ("[ERROR] pass url OR cate, not both of them ")

    def parse(self, response):
        meta_req = response.meta
        res = json.loads(response.body)
        if len(res['data']) > 0:
            datas = res['data']
            for row in datas:
                post_url = "https://tuoitrehaugiang.org.vn/bai-viet/" + str(row['slug']) + "." + str(row['id'])
                string = str(post_url.encode('utf-8')) + "_" + str(meta_req['domain'])
                key_insert = hashlib.md5(str(string).decode('utf-8').encode('utf-8')).hexdigest()
                duplicate = self.redis_exists(key_insert)
                if duplicate == True:
                    print ("[INFO] ITEM ALREADY EXISTS DON'T REQUEST AGAIN")
                    print ("[INFO] THE KEY: " + key_insert)
                    print ("[INFO] THE WEB LINK : " + str(post_url.encode("utf-8")))
                else:
                    meta_req["post_url"] = post_url
                    yield Request(post_url, callback=self.parse_full_post, meta=meta_req)

class DauTuThongMinh247ComSpider(BaseSpider):
    name = 'daututhongminh247'
    allowed_domains = ['daututhongminh247.com']
    service_id = 100206

class DaiBieuDanCuKonTumGovVNSpider(BaseSpider):
    name = 'daibieudancukontum_gov'
    allowed_domains = ['daibieudancukontum.gov.vn']
    service_id = 100207

class AutoCarVietNamVNSpider(BaseSpider):
    name = 'autocarvietnam'
    allowed_domains = ['autocarvietnam.vn']
    service_id = 100208

class TinTucOto360ComSpider(BaseSpider):
    name = 'tintucoto360'
    allowed_domains = ['tintucoto360.com']
    service_id = 100209

class GiaVangNetSpider(BaseSpider):
    name = 'giavang'
    allowed_domains = ['giavang.net']
    service_id = 100210

class Emagazine24NetSpider(BaseSpider):
    name = 'emagazine24'
    allowed_domains = ['emagazine24.net']
    service_id = 100211

class GiaoPhanKonTumComSpider(BaseSpider):
    name = 'giaophankontum'
    allowed_domains = ['giaophankontum.com']
    service_id = 100212

class MolistarComSpider(BaseSpider):
    name = 'molistar'
    allowed_domains = ['molistar.com']
    service_id = 100213

class DoiSongVaThuongHieuComSpider(BaseSpider):
    name = 'doisongvathuonghieu'
    allowed_domains = ['doisongvathuonghieu.com']
    service_id = 100214

class KonTumGovVNSpider(BaseSpider):
    name = 'kontum_gov'
    allowed_domains = ['kontum.gov.vn']
    service_id = 100215

class QuocPhongThuDoVNSpider(BaseSpider):
    name = 'quocphongthudo'
    allowed_domains = ['quocphongthudo.vn']
    service_id = 100216

class TinHangHoaVNSpider(BaseSpider):
    name = 'tinhanghoa'
    allowed_domains = ['tinhanghoa.vn']
    service_id = 100217

class CongChuc24hComSpider(BaseSpider):
    name = 'congchuc24h'
    allowed_domains = ['congchuc24h.com']
    service_id = 100218
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'wb.middlewares.RandomUserAgentMiddleware': 400,
            'wb.middlewares.RandomProxyBuyingTEST': 410,
        }
    }

class LienDoanLuatSuOrgVNSpider(BaseSpider):
    name = 'liendoanluatsu'
    allowed_domains = ['liendoanluatsu.org.vn']
    service_id = 100219

class TapChiHangKhongComSpider(BaseSpider):
    name = 'tapchihangkhong'
    allowed_domains = ['tapchihangkhong.com']
    service_id = 100220

class VnhotVNSpider(BaseSpider):
    name = 'vnhot'
    allowed_domains = ['vnhot.vn']
    service_id = 100221

class CafeBitCoinOrgSpider(BaseSpider):
    name = 'cafebitcoin'
    allowed_domains = ['cafebitcoin.org']
    service_id = 100222

class GiaoPhanDaLatComSpider(BaseSpider):
    name = 'giaophandalat'
    allowed_domains = ['giaophandalat.com']
    service_id = 100223

class EnSggpOrgVNSpider(BaseSpider):
    name = 'en_sggp'
    allowed_domains = ['en.sggp.org.vn']
    service_id = 100224

class KhoaHocTVSpider(BaseSpider):
    name = 'khoahoctv'
    allowed_domains = ['khoahoc.tv']
    service_id = 100225

class DoanhNghiepTodayNetSpider(BaseSpider):
    name = 'doanhnghieptoday'
    allowed_domains = ['doanhnghieptoday.net']
    service_id = 100226

class KenhNguoiNoiTiengComSpider(BaseSpider):
    name = 'kenhnguoinoitieng'
    allowed_domains = ['kenhnguoinoitieng.com']
    service_id = 100227

class CongDoanXayDungvnOrgVNSpider(BaseSpider):
    name = 'congdoanxaydungvn_org'
    allowed_domains = ['congdoanxaydungvn.org.vn']
    service_id = 100228

class TheGioiNguoiDepVNSpider(BaseSpider):
    name = 'thegioinguoidep'
    allowed_domains = ['thegioinguoidep.vn']
    service_id = 100229

class IavVNSpider(BaseSpider):
    name = 'iavvn'
    allowed_domains = ['iav.vn']
    service_id = 100230
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'wb.middlewares.RandomUserAgentMiddleware': 400,
            'wb.middlewares.RandomProxyBuyingTEST': 410,
        }
    }
    
    def start_requests(self):
        page = 1
        cf_domain = self.allowed_domains[0]
        parser_xpath = self.get_xpaths()

        if self.crawl_one_url == None and self.crawl_one_cate == None :

            list_data = DispatcherLibrary(self.service_id, self.group).getCateUrls(cf_domain)
            if len(list_data) > 0:
                for row in list_data:
                    id, domain_url, category_name, domain_name, domain_group, status, created, pay_category = row
                    meta = {"domain": cf_domain, "xpath_config": parser_xpath, "domain_id": id, "category_name": category_name, "category_url": domain_url, "pay": pay_category, "dont_redirect": "True"}
                    print (domain_url)
                    yield Request(domain_url,meta=meta,callback=self.parse)

        elif self.crawl_one_url != None and self.crawl_one_cate == None :


            meta = {
                "post_url": self.crawl_one_url,
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
                yield Request(self.crawl_one_url, callback = self.parse_full_post_for_debug,  meta=meta)
            else:
                yield Request(self.crawl_one_url, callback = self.parse_full_post, meta=meta)

        elif self.crawl_one_url == None and self.crawl_one_cate != None :
            while True:
                list_data = DispatcherLibrary(self.service_id, self.group).getUrlLeech(cf_domain, self.group, page)
                if len(list_data) > 0:
                    for row in list_data:
                        id, domain_url, category_name, domain_name, domain_group, status, created, pay_category = row
                        meta = {"domain": cf_domain, "xpath_config": parser_xpath, "domain_id": id, "category_name": category_name, "category_url": domain_url, "pay": pay_category, "dont_redirect": "True"}
                        if domain_url == self.crawl_one_cate:
                            yield Request(domain_url,meta=meta,callback=self.parse)
                else:
                    break
                page = page + 1
        else:
            print ("[ERROR] pass url OR cate, not both of them ")

class PhuNuCuocSongVNSpider(BaseSpider):
    name = 'phunucuocsong'
    allowed_domains = ['phunucuocsong.vn']
    service_id = 100231

class TiepThiPlusNetSpider(BaseSpider):
    name = 'tiepthiplus'
    allowed_domains = ['tiepthiplus.net']
    service_id = 100232

class VinabullVNSpider(BaseSpider):
    name = 'vinabull'
    allowed_domains = ['vinabull.vn']
    service_id = 100233

class FoundationMiraeassetComVNSpider(BaseSpider):
    name = 'foundation_miraeasset'
    allowed_domains = ['foundation.miraeasset.com.vn']
    service_id = 100234
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'wb.middlewares.RandomUserAgentMiddleware': 400,
            'wb.middlewares.RandomProxyBuyingTEST': 410,
        }
    }

    def start_requests(self):
        page = 1
        cf_domain = self.allowed_domains[0]
        parser_xpath = self.get_xpaths()

        if self.crawl_one_url == None and self.crawl_one_cate == None :

            list_data = DispatcherLibrary(self.service_id, self.group).getCateUrls(cf_domain)
            if len(list_data) > 0:
                for row in list_data:
                    id, domain_url, category_name, domain_name, domain_group, status, created, pay_category = row
                    meta = {"domain": cf_domain, "xpath_config": parser_xpath, "domain_id": id, "category_name": category_name, "category_url": domain_url, "pay": pay_category, "dont_redirect": "True"}
                    print (domain_url)
                    yield Request(domain_url,meta=meta,callback=self.parse)

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
                yield Request(self.crawl_one_url, callback = self.parse_full_post_for_debug,  meta=meta)
            else:
                yield Request(self.crawl_one_url, callback = self.parse_full_post, meta=meta)

        elif self.crawl_one_url == None and self.crawl_one_cate != None :
            while True:
                list_data = DispatcherLibrary(self.service_id, self.group).getUrlLeech(cf_domain, self.group, page)
                if len(list_data) > 0:
                    for row in list_data:
                        id, domain_url, category_name, domain_name, domain_group, status, created, pay_category = row
                        meta = {"domain": cf_domain, "xpath_config": parser_xpath, "domain_id": id, "category_name": category_name, "category_url": domain_url, "pay": pay_category, "dont_redirect": "True"}
                        if domain_url == self.crawl_one_cate:
                            yield Request(domain_url,meta=meta,callback=self.parse)
                else:
                    break
                page = page + 1
        else:
            print ("[ERROR] pass url OR cate, not both of them ")
    
    def parse(self, response):
        meta_req = response.meta
        res = json.loads(response.body)
        if len(res['data']['data']) > 0:
            datas = res['data']['data']
            for row in datas:
                post_url = "https://foundation.miraeasset.com.vn/en/news/" + str(row['attributes']['slug']) + "-" + str(row['id'])
                string = str(post_url.encode('utf-8')) + "_" + str(meta_req['domain'])
                key_insert = hashlib.md5(str(string).decode('utf-8').encode('utf-8')).hexdigest()
                duplicate = self.redis_exists(key_insert)
                if duplicate == True:
                    print ("[INFO] ITEM ALREADY EXISTS DON'T REQUEST AGAIN")
                    print ("[INFO] THE KEY: " + key_insert)
                    print ("[INFO] THE WEB LINK : " + str(post_url.encode("utf-8")))
                else:
                    meta_req["post_url"] = post_url
                    yield Request(post_url, callback=self.parse_full_post, meta=meta_req)

class DoanhNhanSaoVietVNSpider(BaseSpider):
    name = 'doanhnhansaoviet'
    allowed_domains = ['doanhnhansaoviet.vn']
    service_id = 100235

class VdaOrgVNSpider(BaseSpider):
    name = 'vda_org'
    allowed_domains = ['vda.org.vn']
    service_id = 100236

class TamNhinKienThucNetVNSpider(BaseSpider):
    name = 'tamnhin_kienthuc'
    allowed_domains = ['tamnhin.kienthuc.net.vn']
    service_id = 100237

class DoanhNhanBaoPhapLuatVNSpider(BaseSpider):
    name = 'doanhnhan_baophapluat'
    allowed_domains = ['doanhnhan.baophapluat.vn']
    service_id = 100238

class MafcComVNSpider(BaseSpider):
    name = 'mafc'
    allowed_domains = ['mafc.com.vn']
    service_id = 100239

class BlogChiaSeKienThucComSpider(BaseSpider):
    name = 'blogchiasekienthuc'
    allowed_domains = ['blogchiasekienthuc.com']
    service_id = 100240

class BanCanBietVNSpider(BaseSpider):
    name = 'bancanbiet'
    allowed_domains = ['bancanbiet.vn']
    service_id = 100241

class KetNoiDauTuNetSpider(BaseSpider):
    name = 'ketnoidautu'
    allowed_domains = ['ketnoidautu.net']
    service_id = 100242

class DoanhNhanThuongHieuVietVNSpider(BaseSpider):
    name = 'doanhnhanthuonghieuviet'
    allowed_domains = ['doanhnhanthuonghieuviet.vn']
    service_id = 100243

class TopSaoVNSpider(BaseSpider):
    name = 'topsao'
    allowed_domains = ['topsao.vn']
    service_id = 100244

class NongThonMoiPhuThoVNSpider(BaseSpider):
    name = 'nongthonmoiphutho'
    allowed_domains = ['nongthonmoiphutho.vn']
    service_id = 100245

class CongDoanDsvnOrgVNSpider(BaseSpider):
    name = 'congdoandsvn_org'
    allowed_domains = ['congdoandsvn.org.vn']
    service_id = 100246

class MotPhutSaiGonVNSpider(BaseSpider):
    name = '1phutsaigon'
    allowed_domains = ['1phutsaigon.vn']
    service_id = 100247

class Chiase2vnComSpider(BaseSpider):
    name = 'chiase2vn'
    allowed_domains = ['chiase2vn.com']
    service_id = 100248

class CongDoanLaiChauOrgVNSpider(BaseSpider):
    name = 'congdoanlaichau_org'
    allowed_domains = ['congdoanlaichau.org.vn']
    service_id = 100249
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'wb.middlewares.RandomUserAgentMiddleware': 400,
            'wb.middlewares.RandomProxyBuyingTEST': 410,
        }
    }

class CongDoantkvVNSpider(BaseSpider):
    name = 'congdoantkv'
    allowed_domains = ['congdoantkv.vn']
    service_id = 100250

class KinhTeChauAVNSpider(BaseSpider):
    name = 'kinhtechaua'
    allowed_domains = ['kinhtechaua.vn']
    service_id = 100251

class ToaSangNganhNetSpider(BaseSpider):
    name = 'toasangnganh'
    allowed_domains = ['toasangnganh.net']
    service_id = 100252

class Ttth247ComSpider(BaseSpider):
    name = 'ttth247'
    allowed_domains = ['ttth247.com']
    service_id = 100253

class PhapluatplusBaophapluatSpider(BaseSpider):
    name = 'phapluatplus_baophapluat'
    allowed_domains = ['phapluatplus.baophapluat.vn']
    service_id = 100254

class HomeTodayVNSpider(BaseSpider):
    name = 'hometoday'
    allowed_domains = ['hometoday.vn']
    service_id = 100255

class SaoBizVNSpider(BaseSpider):
    name = 'saobiz'
    allowed_domains = ['saobiz.vn']
    service_id = 100256

class ThoiBaoNgaComSpider(BaseSpider):
    name = 'thoibaonga'
    allowed_domains = ['thoibaonga.com']
    service_id = 100257

class TieuDungThoiNayVNSpider(BaseSpider):
    name = 'tieudungthoinay'
    allowed_domains = ['tieudungthoinay.vn']
    service_id = 100258

class TanTheKyOrgSpider(BaseSpider):
    name = 'tantheky'
    allowed_domains = ['tantheky.org']
    service_id = 100259

class TheBankerComSpider(BaseSpider):
    name = 'thebanker'
    allowed_domains = ['thebanker.com']
    service_id = 100260
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'wb.middlewares.RandomUserAgentMiddleware': 400,
            'wb.middlewares.RandomProxyBuyingTEST': 410,
        }
    }

    def start_requests(self):
        page = 1
        cf_domain = self.allowed_domains[0]
        parser_xpath = self.get_xpaths()

        if self.crawl_one_url == None and self.crawl_one_cate == None :
            list_data = DispatcherLibrary(self.service_id, self.group).getCateUrls(cf_domain)
            if len(list_data) > 0:
                for row in list_data:
                    id, domain_url, category_name, domain_name, domain_group, status, created, pay_category = row
                    meta = {"domain": cf_domain, "xpath_config": parser_xpath, "domain_id": id, "category_name": category_name, "category_url": domain_url, "pay": pay_category, "dont_redirect": "True"}
                    match = re.search(r'/(\d+)$', meta['category_url'])
                    
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Referer": "https://www.google.com/",
                        "Connection": "keep-alive",
                        "Upgrade-Insecure-Requests": "1",
                        "DNT": "1"  # Do Not Track
                    }

                    body = {
                        "page": 1,
                        "pageSize": 5,
                        "filters": {
                            "category_id": match
                        }
                    }

                    yield Request(domain_url,method='POST',headers=headers,meta=meta,callback=self.parse, body=json.dumps(body))
                    # yield Request(domain_url,meta=meta,callback=self.parse)

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
                yield Request(self.crawl_one_url, callback = self.parse_full_post_for_debug,  meta=meta)
            else:
                yield Request(self.crawl_one_url, callback = self.parse_full_post, meta=meta)

        elif self.crawl_one_url == None and self.crawl_one_cate != None :
            while True:
                list_data = DispatcherLibrary(self.service_id, self.group).getUrlLeech(cf_domain, self.group, page)
                if len(list_data) > 0:
                    for row in list_data:
                        id, domain_url, category_name, domain_name, domain_group, status, created, pay_category = row
                        meta = {"domain": cf_domain, "xpath_config": parser_xpath, "domain_id": id, "category_name": category_name, "category_url": domain_url, "pay": pay_category, "dont_redirect": "True"}
                        match = re.search(r'/(\d+)$', meta['category_url'])
                        headers = {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                            "Accept-Language": "en-US,en;q=0.9",
                            "Accept-Encoding": "gzip, deflate, br",
                            "Referer": "https://www.google.com/",
                            "Connection": "keep-alive",
                            "Upgrade-Insecure-Requests": "1",
                            "DNT": "1"  # Do Not Track
                        }

                        body = {
                            "page": 1,
                            "pageSize": 5,
                            "filters": {
                                "category_id": match
                            }
                        }
                        if domain_url == self.crawl_one_cate:
                            yield Request(domain_url,method='POST',headers=headers,meta=meta,callback=self.parse, body=json.dumps(body))
                else:
                    break
                page = page + 1
        else:
            print ("[ERROR] pass url OR cate, not both of them ")

class TheAsianBankerComSpider(BaseSpider):
    name = 'theasianbanker'
    allowed_domains = ['theasianbanker.com']
    service_id = 100261

class GfmagComSpider(BaseSpider):
    name = 'gfmag'
    allowed_domains = ['gfmag.com']
    service_id = 100262

class EuromoneyComSpider(BaseSpider):
    name = 'euromoney'
    allowed_domains = ['euromoney.com']
    service_id = 100263

class BusinesstimesComSGSpider(BaseSpider):
    name = 'businesstimes'
    allowed_domains = ['businesstimes.com.sg']
    service_id = 100264

class TheAssetComSpider(BaseSpider):
    name = 'theasset'
    allowed_domains = ['theasset.com']
    service_id = 100265

class ThuongHieuQuocGiaNhanDanVNSpider(BaseSpider):
    name = 'thuonghieuquocgia_nhandan'
    allowed_domains = ['thuonghieuquocgia.nhandan.vn']
    service_id = 100266

class KtdsVNSpider(BaseSpider):
    name = 'ktds'
    allowed_domains = ['ktds.vn']
    service_id = 100267

class BaoXayDungVNSpider(BaseSpider):
    name = 'baoxaydungvn'
    allowed_domains = ['baoxaydung.vn']
    service_id = 100268

class TapChiVietNamHuongSacVNSpider(BaseSpider):
    name = 'tapchivietnamhuongsac'
    allowed_domains = ['tapchivietnamhuongsac.vn']
    service_id = 100269

class SoNoiVuHaNoiGovVNSpider(BaseSpider):
    name = 'sonoivu_hanoi_gov'
    allowed_domains = ['sonoivu.hanoi.gov.vn']
    service_id = 100270