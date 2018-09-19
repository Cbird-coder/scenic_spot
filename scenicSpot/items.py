# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpotItem(scrapy.Item):
    # define the fields for your item here like:
    SPOT_id = scrapy.Field()
    SPOT_name = scrapy.Field()
    SPOT_districts = scrapy.Field()
    SPOT_level = scrapy.Field()
    SPOT_product_star_level = scrapy.Field()
    SPOT_intro = scrapy.Field()
    SPOT_point = scrapy.Field()
    SPOT_address = scrapy.Field()