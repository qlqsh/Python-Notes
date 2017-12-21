#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

# 通过post方式提交表单数据。
params = { 'firstname': 'Ryan', 'lastname': "Mitchell" }
r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
print(r.text)