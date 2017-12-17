#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import quote

url = 'http://www.example.com/api.php?text=这里是中文'

# 不带附加参数
# http%3A//www.example.com/api.php%3Ftext%3D%E8%BF%99%E9%87%8C%E6%98%AF%E4%B8%AD%E6%96%87
print('\n不带附加参数：\n%s' % quote(url))

# 附带不转换字符参数
# http://www.example.com/api.php?text=%E8%BF%99%E9%87%8C%E6%98%AF%E4%B8%AD%E6%96%87
print('\n附加不转换字符参数：\n%s' % quote(url, safe='/:?='))