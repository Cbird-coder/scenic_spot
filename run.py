#/usr/bin/env python
#coding:utf-8

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scenicSpot.spiders.scenicSpot import scenicSpotSpider

def runspider():
	# 获取settings.py模块的设置
	process = CrawlerProcess(settings=get_project_settings())
	# 可以添加多个spider
	process.crawl(scenicSpotSpider)
	#启动爬虫，会阻塞，直到爬取完成
	process.start()	

if __name__ == '__main__':
		runspider()	