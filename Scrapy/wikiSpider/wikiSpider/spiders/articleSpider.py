#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scrapy.selector import Selector
from scrapy import Spider
from wikiSpider.items import Article

class ArticleSpider(Spider):
    name = "article"    
    allowed_domains = ["en.wiwipedia.org"]
    start_urls =  ["http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
    
    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is: " + title)
        item['title'] = title
        return item