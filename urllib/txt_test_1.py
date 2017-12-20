#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

# textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
# print(str(textPage.read(), 'utf-8'))

try:
    html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
except URLError as e:
    print(e)
except HTTPError as e:
    print(e)
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
# print(content)

# 感觉下面的转换很没有意义。除非bytes里面不是utf-8，而是iso编码，可能就有必要了。
content = bytes(content, "UTF-8")
# print(content)
content = content.decode("UTF-8")
# print(content)