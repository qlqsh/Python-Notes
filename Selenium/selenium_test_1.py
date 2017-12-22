#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

# 需要使用"PhantomJS"来把网页加载到内存并执行页面上的JavaScript。
driver = webdriver.PhantomJS(executable_path="/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs")
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
# selenium的选择器
# driver.find_element_by_css_selector("#content")
# driver.find_element_by_css_selector("div")
# driver.find_element_by_tag_name("div")
# driver.page_source 返回页面源代码
print(driver.find_element_by_id('content').text)
driver.close()