#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

# 提交文件和图像到远程服务器
files = {'uploadFile': open('./Resources/uploadTest.jpeg')}
r = requests.post("http://pythonscraping.com/pages/processing2.php", files=files)
print(r.text)