#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(str(textPage.read(), 'utf-8'))