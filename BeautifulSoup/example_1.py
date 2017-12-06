#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    """提取HTML内容里的标题（<h1>）内容"""
    try:
        html = urlopen(url)
    except URLError as e: # URL错误
        return None
    except HTTPError as e: # HTTP无法访问
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e: # 标签不存在
        return None
    return title
title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)