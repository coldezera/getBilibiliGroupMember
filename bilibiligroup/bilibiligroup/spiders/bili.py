# -*- coding: utf-8 -*-
import scrapy
from bilibiligroup.items import BilibiligroupItem
import re
import numpy
import json
import time
import requests
from bilibiligroup.spiders.bili_log import Mylog

log = Mylog()
USERAGENT = [
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 '
]

page_header = {
    'Host': 'steamcommunity.com',
    # 'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': '',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://steamcommunity.com/groups/bilibili',
    'Accept-Encoding': 'gzip, deflate',
    # 'Cookie': 'strInventoryLastContext=730_2; sessionid=4b801e99f374c14912b2f7cb; steamCountry=CN%7Cd61adfb5bcc48106226fe167ccd23066; timezoneOffset=28800,0; _ga=GA1.2.1155326369.1502165761; _gid=GA1.2.2127610333.1502597125'
}

user_header = {
    'Host': 'steamcommunity.com',
    # 'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Accept-Language': 'en-us,en;q=0.8',
    'User-Agent': '',
    'X-Prototype-Version': '1.7',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://steamcommunity.com/groups/bilibili',
    'Accept-Encoding': 'gzip, deflate',
    # 'Cookie': 'strInventoryLastContext=730_2; sessionid=4b801e99f374c14912b2f7cb; steamCountry=CN%7Cd61adfb5bcc48106226fe167ccd23066; timezoneOffset=28800,0; _ga=GA1.2.1155326369.1502165761; _gid=GA1.2.2127610333.1502597125'
}
#2675s
gamelist_header = {
    # 'Host': 'steamcommunity.com',
    # 'Connection': 'keep-alive',
    # 'Cache-Control': 'max-age=0',
    # 'Upgrade-Insecure-Requests': '1',
    'User-Agent': '',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': '',
    'Accept-Encoding': 'gzip, deflate',
    # 'Cookie': 'strInventoryLastContext=730_2; sessionid=d06d925e0936c57781a862cd; steamCountry=CN%7C4b3838352d8fe566aa57a9a666015d83; timezoneOffset=28800,0; _ga=GA1.2.1155326369.1502165761; _gid=GA1.2.385470949.1502942486'
}
class BiliSpider(scrapy.Spider):
    name = 'bili'
    # allowed_domains = ['slekfj']
    # start_urls = ['http://steamcommunity.com/groups/bilibili/members/?p=1&content_only=true']
    start_urls = []
    current_agent = ''
    current_crawl_user = 0
    current_crawl_page = 0
    def __init__(self):
        with open('user-agent.txt', 'rb') as uaf:
            for ua in uaf.readlines():
                if ua:
                    USERAGENT.append(ua.strip()[1:-1 - 1])
        numpy.random.shuffle(USERAGENT)
        for i in range(1, 3653):
            self.start_urls.append('http://steamcommunity.com/groups/bilibili/members/?p=' + str(i) + '&content_only=true')
        pass
    def start_requests(self):
        for url in self.start_urls:
            try:
                page_header['User-Agent'] = numpy.random.choice(USERAGENT)
                yield scrapy.Request(url, dont_filter=True, headers=page_header)
                time.sleep(2)
            except:
                m = re.search('/\?p=(.*)&con', url)
                log.CriticalLog('第'+m.group(1)+'页爬取失败！')
        pass
    def parse(self, response):#解析当前页面内的所有用户的链接并跟进
        self.current_crawl_page += 1
        print('第%s页正在被解析----'%self.current_crawl_page)
        for member in response.xpath('//div[@id="memberList"]/div[@class="member_block "]|\
                                     //div[@id="memberList"]/div[@class="member_block last"]'):
            user_url = member.xpath('.//div[last()]/div[1]/a/@href').extract()[0].strip()
            user_64url = 'http://steamcommunity.com/profiles/{}'
            m = re.search('id/(.*)', user_url)
            if m is not None:
                gamelist_header['User-Agent'] = numpy.random.choice(USERAGENT)
                VanityURL = m.group(1)
                get64url = 'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={Your Steam API key}&vanityurl={}'
                get64url = get64url.format(VanityURL)
                res = requests.get(get64url, headers=gamelist_header)
                js = json.loads(res.text)
                if js['response']['success'] == 1:
                    user64id = js['response']['steamid']
            else:
                m = re.search('profiles/(.*)', user_url)
                user64id = m.group(1)
            user_64url = user_64url.format(user64id)
            user_header['User-Agent'] = numpy.random.choice(USERAGENT)
            try:
                yield scrapy.Request(user_64url,
                                     method='GET',
                                     callback=self.parse_member,
                                     meta={
                                         'url': user_64url,
                                         '64id': user64id,
                                         'dont_redirect': True,
                                         'handle_httpstatus_list': [301,302]
                                     },
                                     headers=user_header)
            except:
                log.CriticalLog(user64id+'个人主页获取失败')
        print('第%s页已经被解析完毕!!' % self.current_crawl_page)
        pass
    def parse_member(self, response):#解析用户信息
        self.current_crawl_user += 1
        item = BilibiligroupItem()
        item['user_url'] = response.meta['url']
        item['VACBan'] = '0'
        item['GameBan'] = '0'
        if str(response.xpath('//div[@class="profile_ban_status"]')) != '[]': #判断是否有VACBAN后者GAMEBAN
            for ban in response.xpath('//div[@class="profile_ban_status"]/div[@class="profile_ban"]'):
                bantext = ban.xpath('.//text()').extract()[0].strip()
                bankind = re.search(' (.*) ban', bantext)
                if bankind.group(1) == 'VAC':
                    item['VACBan'] = '1'
                elif bankind.group(1) == 'game':
                    item['GameBan'] = '1'
        print('正在爬取第%s个组员'%self.current_crawl_user)
        if str(response.xpath('//div[@class="profile_private_info"]').extract()) == '[]':#判断是否是资料私密
            item['PrivateProfile'] = '0'
        else:
            item['PrivateProfile'] = '1'
            return item
        item['CSGO'] = '0'
        for recentgame in response.xpath('//div[@class="recent_game"]'):#判断用户近期游戏是否有CSGO
            if recentgame.xpath('.//div[1]/div[1]/div[3]/a/text()').extract()[0] == 'Counter-Strike: Global Offensive':
                item['CSGO'] = '1'
                return item
        # 近期游戏没有CSGO则调用api进库里寻找
        nexturl = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={Your Steam API key}&steamid={}&format=json'
        nexturl = nexturl.format(response.meta['64id'])
        gamelist_header['User-Agent'] = numpy.random.choice(USERAGENT)
        # 近期游戏没有CSGO则跟进游戏库寻找
        try:
            return scrapy.Request(nexturl,
                                  method='GET',
                                  callback=self.parse_getgame,
                                  headers=gamelist_header,
                                  meta={'item': item})
        except:
            log.CriticalLog('获取'+response.meta['64id']+'游戏库列表失败!')
        pass
    def parse_getgame(self, response):
        item = response.meta['item']
        text = response.body.decode('utf-8')
        m = re.search('"appid": (730),', text)
        if m is not None:
            item['CSGO'] = '1'
        return item
        pass
    def parse_getid(self, response):
        text = response.body.decode('utf-8')
        # print(text)
        js = json.loads(text)
        # if js['response']['success'] == 1:
        return js['response']['steamid']
        pass
