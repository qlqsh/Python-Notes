#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("邮件内容", "plain", "utf-8") # 邮件内容、格式、编码
msg['Subject'] = "邮件主题" # 邮件主题
msg['From'] = "qlqsh@sina.com"  # 发送邮件账号
msg['To'] = "qlqsh@icloud.com"  # 接收邮件账号

# 需要去sina设置，打开IMAP4/SMTP，要不无法收发。
server = smtplib.SMTP('smtp.sina.com')          # 适用于发件服务器的SMTP信息
server.set_debuglevel(1)                        # 打印与SMTP服务器交互的信息
server.login("qlqsh@sina.com", "your_password") # 用户名、密码
server.send_message(msg)                        # 发送邮件
server.quit()                                   # 退出服务