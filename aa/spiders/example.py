# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class ExampleSpider(scrapy.Spider):
    name = 'e'
    allowed_domains = ['192.168.43.133']
    start_urls = ['http://192.168.43.133/images/poweredby.png']

    def parse(self, response):
        sel = Selector(response)
        data = sel.extract()
        print(data)
        pass
