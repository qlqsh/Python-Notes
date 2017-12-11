#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    """获取链接列表"""
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll('a', href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages: # 新的链接
                # 我们遇到的新页面
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage) # 递归

getLinks("")