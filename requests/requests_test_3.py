#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

# 使用cookie跟踪网站状态
params = {'username': 'Ryan', 'password': 'password'}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print("Cookie is set to:")
print(r.cookies.get_dict())
print("---------")
print("Going to profile page...")
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print(r.text)