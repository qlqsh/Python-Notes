#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

def sendMail(subject, body):
    """发送邮件"""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "qlqsh@sina.com"
    msg['To'] = "qlqsh@icloud.com"
    server = smtplib.SMTP('smtp.sina.com')          # 适用于发件服务器的SMTP信息
    server.set_debuglevel(1)                        # 打印与SMTP服务器交互的信息
    server.login("qlqsh@sina.com", "niannian@%")    # 用户名、密码
    server.send_message(msg)                        # 发送邮件
    server.quit()                                   # 退出服务

# 每小时检查一次"https://isitchristmas.com/"网站，根据日期判断当天是不是圣诞节。
bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"), "html.parser")
# 无法访问https://isitchristmas.com/，所以这个程序while部分始终运行，直接发邮件了。
while(bsObj.find("a", {"id":"answer"}).attrs['title'] == "NO"):
    print("圣诞节还没到")
    time.sleep(3600)
sendMail("圣诞节到了", "来自 http://itischristmas.com, 圣诞节到了")