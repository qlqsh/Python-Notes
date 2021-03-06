#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest

# 标准单元测试
class TestWikipedia(unittest.TestCase):
    bsObj = None
    def setUpClass():
        """仅在类的初始化阶段运行一次。"""
        global bsObj
        url = "http://en.wikipedia.org/wiki/Monty_Python"
        bsObj = BeautifulSoup(urlopen(url), "html.parser")
    
    def test_titleText(self):
        global bsObj
        pageTitle = bsObj.find("h1").get_text()
        self.assertEqual("Monty Python", pageTitle)
    
    def test_contentExists(self):
        global bsObj
        # 测试html页面是否有一个"div"节点"id"属性是"mw-content-text"。
        content = bsObj.find("div", {"id": "mw-content-text"})
        self.assertIsNotNone(content) 
    
if __name__ == '__main__':
    unittest.main()