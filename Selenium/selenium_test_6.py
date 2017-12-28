#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.PhantomJS(executable_path="/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs")

def seleniumTest():
    """使用Selenium进行测试。"""
    global driver
    driver.get("http://en.wikipedia.org/wiki/Monty_Python")
    assert "Monty Python" in driver.title # 测试

def submitForm1():
    """提交表单方式1。"""
    global driver
    driver.get("http://pythonscraping.com/pages/files/form.html")
    firstnameField = driver.find_element_by_name("firstname")
    lastnameField = driver.find_element_by_name("lastname")
    submitButton = driver.find_element_by_id("submit")
    firstnameField.send_keys("Ryan")
    lastnameField.send_keys("Mitchel")
    submitButton.click()
    print(driver.find_element_by_tag_name("body").text)

def submitForm2():
    """提交表单方式2：动作链。"""
    global driver
    driver.get("http://pythonscraping.com/pages/files/form.html")
    # 元素
    firstnameField = driver.find_element_by_name("firstname")
    lastnameField = driver.find_element_by_name("lastname")
    submitButton = driver.find_element_by_id("submit")
    # 动作链
    #   1、点击"firstnameField"文字域，发送字符串"Ryan"；
    #   2、点击"lastnameField"文字域，发送字符串"Mitchel"；
    #   3、回车；
    actions = ActionChains(driver).click(firstnameField).send_keys("Ryan").click(lastnameField).send_keys("Mitchel").send_keys(Keys.RETURN)
    actions.perform()
    print(driver.find_element_by_tag_name("body").text)

seleniumTest()
# submitForm1()
# submitForm2()

driver.close()