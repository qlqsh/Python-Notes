#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except URLError as e:
    print(e)
except HTTPError as e:
    print(e)
print(html.read())