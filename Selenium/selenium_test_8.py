#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver

# 截屏
driver = webdriver.PhantomJS(executable_path="/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs")
driver.get("http://www.pythonscraping.com/")
driver.get_screenshot_as_file('./Resources/pythonscraping.png')
driver.close()