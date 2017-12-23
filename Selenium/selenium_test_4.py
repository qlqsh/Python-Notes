#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.PhantomJS(executable_path="/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs")
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print("driver:", driver.get_cookies())
savedCookies = driver.get_cookies()
driver.close()

driver2 = webdriver.PhantomJS(executable_path="/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs")
driver2.get("http://pythonscraping.com")
print("driver2:", driver2.get_cookies())

driver2.delete_all_cookies()
for cookie in savedCookies:
    driver2.add_cookie(cookie)
driver2.get("http://pythonscraping.com")
driver2.implicitly_wait(1)
print("new driver2:", driver2.get_cookies())