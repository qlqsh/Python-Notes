#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import unquote
import unittest
import random
import re

# 标准单元测试
class TestWikipedia(unittest.TestCase):
    bsObj = None
    url = None
    
    def test_PageProperties(self):
        global bsObj
        global url
        url = "http://en.wikipedia.org/wiki/Monty_Python"
        # 测试遇到的前100个页面
        for i in range(1, 100):
            bsObj = BeautifulSoup(urlopen(url), "html.parser")
            titles = self.titleMatchesURL()
            self.assertEqual(titles[0], titles[1])
            self.assertTrue(self.contentExists())
            url = self.getNextLink()
        print("Done!")
    
    def titleMatchesURL(self):
        """判断URL里面的文字与标题是否匹配。"""
        global bsObj
        global url
        pageTitle = bsObj.find("h1").get_text()
        urlTitle = url[(url.index("/wiki/")+6):] # 返回"/wiki/"右边到结尾的字符串。
        urlTitle = urlTitle.replace("_", " ")
        urlTitle = unquote(urlTitle)
        # 返回字符串列表，而不是布尔变量。主要是调试起来更加方便、详细。出现异常情况：
        #   assertTrue   => AssertionError: False is not true
        #   assertEquals => AssertionError: 'lockheed u-2' != 'u-2 spy plane'
        return [pageTitle.lower(), urlTitle.lower()]
    
    def contentExists(self):
        """判断内容是否存在（div节点id属性是mw-content-text）。"""
        global bsObj
        content = bsObj.find("div", {"id": "mw-content-text"})
        if content is not None:
            return True
        return False
    
    def getNextLink(self):
        """获取一个随机链接。"""
        global bsObj
        links = bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile(r"^(/wiki/)((?!:).)*$"))
        link = links[random.randint(0, len(links)-1)].attrs['href']
        print("Next link is: " + link)
        return "http://en.wikipedia.org" + link
        
if __name__ == '__main__':
    unittest.main()