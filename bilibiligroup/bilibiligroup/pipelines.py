# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
from bilibiligroup import settings
from bilibiligroup.items import BilibiligroupItem
from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter


class BilibiligroupPipeline(object):
    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file = open('%s_items.csv' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        self.exporter.fields_to_export = ['user_url', 'PrivateProfile', 'CSGO', 'VACBan', 'GameBan']
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    # def __init__(self):
    #     # item = BilibiligroupItem()
    #     # item['user_url'] = 'user_url'
    #     # item['PrivateProfile'] = 'PrivateProfile'
    #     # item['CSGO'] = 'CSGO'
    #     # item['VACBan'] = 'VACBan'
    #     # item['GameBan'] = 'GameBan'
    #     self.file = open(settings.csv_file_path, 'a')
    #     # self.writer = csv.writer(self.file, lineterminator='\n')
    #     self.exporter = CsvItemExporter(self.file)
    #     self.exporter.fields_to_export = ['user_url', 'PrivateProfile', 'CSGO', 'VACBan', 'GameBan']
    #     self.exporter.start_exporting()
    #     # self.writer.writerow([item[key] for key in item.keys()])
    #
    # def spider_opened(self, spider):
    #     pass
    # def spider_closed(self ,spider):
    #     self.exporter.finish_exporting()
    #     self.file.close()
    #     pass
    #
    # def process_item(self, item, spider):
    #     # self.writer = csv.writer(open(settings.csv_file_path, 'a'), lineterminator='\n')
    #     # self.writer.writerow([item[key] for key in item.keys()])
    #     self.exporter.export_item(item)
    #     return item

    pass
