# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv,datetime
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')

class FangjiaPipeline(object):
    def process_item(self, item, spider):
        return item
class Csv_writer_Pipeline(object):
    time_stamp = "%Y_%m_%d"
    content = ['SPOT_id','SPOT_name','SPOT_districts',\
                'SPOT_level','SPOT_product_star_level','SPOT_intro',\
                'SPOT_point','SPOT_address']
    def __init__(self):
        self.filename = 'spot{0}.csv'.format(datetime.datetime.now().strftime(self.time_stamp))
        self.file_obj = open(self.filename,'w')
        self.file_obj.write(codecs.BOM_UTF8)
        self.writer = csv.writer(self.file_obj)
        self.writer.writerow([' ','name','districts','address'])

    def process_item(self, item, spider):
        if len(item) > 0 :
            self.writer.writerow([item[self.content[0]],item[self.content[1]],item[self.content[2]],\
                item[self.content[3]],item[self.content[4]],item[self.content[5]],
                item[self.content[6]],item[self.content[7]]])
        return item