# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TechtalkPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def __init__(self, crawler):
        pass
        filename = crawler.spider.name
        self.file = open('{}.json'.format(filename), 'w')

    def process_item(self, item, spider):
        line = "{}\n".format(json.dumps(dict(item)))
        self.file.write(line)
        print(line)
        return item