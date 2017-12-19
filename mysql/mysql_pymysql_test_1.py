#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
# 需要MySQL运行状态
conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='nianchuanyuan', db='mysql')
cur = conn.cursor()
cur.execute("USE wikipedia")

cur.execute("SELECT * FROM links")
# print(cur.fetchone()) # 取一行
print(cur.fetchall()) # 取所有
cur.close()
conn.close()