# -*- coding: utf-8 -*-
import scrapy
import csv
import os
import re
import bs4
from bs4 import BeautifulSoup
import urllib
from ..items import SpotItem

class scenicSpotSpider(scrapy.Spider):
    name = "fangjia"
    allowed_domins = ["http://piao.qunar.com"]
    start_urls = []
    handle_httpstatus_list = [404,500]

    def after_404(self, response):
        print response.url
    def start_requests(self):
        global headers
        home_url = 'http://piao.qunar.com/ticket/list.htm?keyword=中国'
        for i in range(1000):
            url = home_url+'&page=%s' %(str(i))#
            self.start_urls.append(url)
        print self.start_urls 
        for url in self.start_urls:
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        if response.status in self.handle_httpstatus_list:
             print 'wrong page'
        else:
            item = SpotItem()
            html_string = response.body
            soup = BeautifulSoup(html_string,"html.parser")
            search_list = soup.find('div', attrs={'id': 'search-list'})
            sight_items = search_list.findAll('div', attrs={'class': 'sight_item'})
            for sight_item in sight_items:
                name = sight_item['data-sight-name']
                districts = sight_item['data-districts']
                point = sight_item['data-point']
                address = sight_item['data-address']
                data_id = sight_item['data-id']
                level = sight_item.find('span',attrs={'class':'level'})
                if level:
                    level=level.text
                else:
                    level=""

                product_star_level=sight_item.find('span',attrs={'class':'product_star_level'})

                if product_star_level:
                    product_star_level=product_star_level.text
                else:
                    product_star_level=""
                intro=sight_item.find('div',attrs={'class':'intro'})
                if intro:
                    intro=intro['title']
                else:
                    intro=""
                districts = districts.replace("\n","")
                name = name.replace("\n","")
                data_id = data_id.replace("\n","")
                level = level.replace("\n","")
                product_star_level = product_star_level.replace("\n","")
                address = address.replace("\n","")
                intro = intro.replace("\n","")
                point = point.replace("\n","")

                item['SPOT_id'] = data_id
                item['SPOT_name'] = name
                item['SPOT_districts'] = districts
                item['SPOT_level'] = level
                item['SPOT_product_star_level'] = product_star_level
                item['SPOT_intro'] = intro
                item['SPOT_point'] = point
                item['SPOT_address'] = address
                yield item
