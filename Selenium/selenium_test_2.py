#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 通过"id"是"loadedButton"的按钮检查页面是不是已经完全加载。
driver = webdriver.PhantomJS(executable_path="/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs")
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
    # 驱动等待10秒，直到出现"ID"是"loadedButton"的按钮。
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loadedButton")))
finally:
    # driver.find_element(By.ID "content")与driver.find_element_by_id("content")是一样的。
    print(driver.find_element_by_id("content").text)
    driver.close()