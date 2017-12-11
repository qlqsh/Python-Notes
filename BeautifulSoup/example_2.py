#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

# 用当前系统时间生成一个随机数生成器
random.seed(datetime.datetime.now()) 
def getLinks(articleUrl):
    """获取词条链接列表"""
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    # 过滤：
    # 1、id 是 bodyContent 的 div 标签
    # 2、URL 链接不包括分号
    # 3、URL 链接都以 /wiki/ 开头
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    # 获取一个随机指定范围（链接数量）的随机链接。
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
