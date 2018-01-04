#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver

# 创建新的Selenium driver
# driver = webdriver.PhantomJS(executable_path="/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs")

# 有时PhantomJS查找元素有问题，但是Firefox没有。
# 如果运行程序出现问题，可以试试Firefox、Safari等。
# Safari webdriver自带驱动，但需要设置Safari，开发->运行远程自动化。
driver = webdriver.Safari()

driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
time.sleep(2)

# 单击图书预览按钮
print("单击图片预览按钮")
driver.find_element_by_id("sitbLogoImg").click()
imageList = set()

# 等待页面加载完成
time.sleep(5)
print("页面加载完成")
# 当向右箭头可以点击时，开始翻页。通过探知style属性里是否有pointer来判断是否有下一页。
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    print("有下一页按钮")
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)
    # 获取已加载的新页面（一次可以加载多个页面，但是重复的页面不能加载到集合中）
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    print("有弹出新页面")
    for page in pages:
        image = page.get_attribute("src")
        imageList.add(image)
        print("读取每个图片: "+image)

driver.close()

# 用Tesseract处理收集的图片URL链接
for image in sorted(imageList):
    urlretrieve(image, "./Resources/page.jpg")
    p = subprocess.Popen(["tesseract", "./Resources/page.jpg", "./Resources/page"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    f = open("./Resources/page.txt", 'r')
    print(f.read())
