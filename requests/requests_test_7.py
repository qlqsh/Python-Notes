#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from urllib.parse import quote

# 地址通过网页内部SRC获取<audio src="..."></audio>
downloadMP3 = r"http://180j.ysts8.com:8000/玄幻小说/一指成仙/001.mp3?12505417304057x1515983830x12505729916811-58b9377298408b334a515b8fa519ea2f?3"
# 流下载
r = requests.get(quote(downloadMP3, safe='/:?='), stream=True)
with open("test1.mp3", 'wb') as f:
    for chunk in r.iter_content(chunk_size=512):
        f.write(chunk)