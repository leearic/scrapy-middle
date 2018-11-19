# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AaPipeline(object):
    def process_item(self, item, spider):

        print("==" * 10)
        print(spider.name)
        print("==" * 10)
        return item
