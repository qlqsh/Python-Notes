#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from wikiSpider.items import Article
from scrapy.linkextractors import LinkExtractor

class ArticleSpider(CrawlSpider):
    name = "article2"    
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
    rules = [Rule(LinkExtractor(allow=('(/wiki/)((?!:).)*%'), ), callback="parse_item", follow=True)]
    
    def parse_item(self, response):
        item = Article()
        # TODO: 这里有点问题，有的页面不止是h1里面嵌套i，所以就报错了。
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is: " + title)
        item['title'] = title
        return item
