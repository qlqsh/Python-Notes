#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from selenium import webdriver

# 利用selenium、safari实现新浪微博自动点赞。没验证。

browser = webdriver.Safari()
browser.get('http://weibo.com')
time.sleep(20)
 
# 点击页面中的登录按钮 弹出输入帐号模态框
browser.find_element_by_xpath("//a[@node-type='loginBtn']").click()
time.sleep(2)
 
#输入帐号密码
browser.find_element_by_css_selector('div.item.username.input_wrap input.W_input').send_keys('yourusername')
browser.find_element_by_css_selector('div.item.password.input_wrap input.W_input').send_keys('yourpassword')
time.sleep(1)
 
#点击登录
browser.find_element_by_xpath("//div[@class='item_btn']/a[@suda-data='key=tblog_weibologin3&value=click_sign']").click()
time.sleep(10)
 
#查找页面中的所有 点赞按钮
allzan = browser.find_elements_by_css_selector('em.W_ficon.ficon_praised.S_txt2')
 
#遍历 点击
for temp in allzan:
    print("again")
    time.sleep(1)
    temp.click()
 
browser.close()