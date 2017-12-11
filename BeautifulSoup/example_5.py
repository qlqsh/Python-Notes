#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj, includeUrl):
    """获取页面所有内链的列表。"""
    internalLinks = []
    # 找出所有以"/"或"传递进来的链接"开头的链接
    for link in bsObj.findAll("a", href=re.compile(r"^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

def getExternalLinks(bsObj, excludeUrl):
    """获取页面所有外链的列表"""
    externalLinks = []
    # 找出所有以"http"或"www"开头且不包含当前URL的链接
    for link in bsObj.findAll("a", href=re.compile(r"^(http|www)((?!" + excludeUrl +").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    """获取一个随机外链"""
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getRandomExternalLink(internalLinks[random.randint(0, len(externalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingPage):
    externalLink = getRandomExternalLink("http://oreilly.com")
    print("随机外链是：" + externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")