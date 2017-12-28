#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
import unittest

# 测试拖动。HTML有问题，无法测试。
class TestAddition(unittest.TestCase):
    driver = None
    def setUp(self):
        """每个测试的开始都会运行一次"""
        print("设置测试---")
        global driver
        driver = webdriver.PhantomJS(executable_path="/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs")
        driver.get("http://pythonscraping.com/pages/javascript/draggableDemo.html")
    
    def tearDown(self):
        """每个测试的结束都会运行一次"""
        print("结束测试---")
        global driver
        driver.close()
    
    # 测试拖动
    def test_drag(self):
        global driver
        element = driver.find_element_by_id("draggable")
        target = driver.find_element_by_id("div2")
        actions = ActionChains(driver)
        actions.drag_and_drop(element, target).perform()
        self.assertEqual("You are definitely not a bot!", driver.find_element_by_id("message").text)

if __name__ == '__main__':
    unittest.main()
    