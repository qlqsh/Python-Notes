#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from wikiSpider.items import Article
from scrapy.linkextractors import LinkExtractor

class ArticleSpider(CrawlSpider):
    # 爬虫名称
    name = "article2"
    # 允许的主机域名
    allowed_domains = ["en.wikipedia.org"]
    # 爬取的URL数组
    start_urls = ["http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
    # 规则。提取指定链接。
    rules = [Rule(LinkExtractor(allow=('(/wiki/)((?!:).)*%'), ), callback="parse_item", follow=True)]
    # 爬取指定内容。
    def parse_item(self, response):
        item = Article()
        # 这里有点问题，有的页面不止是h1里面嵌套i，所以就报错了。
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is: " + title)
        item['title'] = title
        return item
