#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nltk.book import *
from nltk import FreqDist
fdist = FreqDist(text6) # 单词频率分布对象
print(fdist.most_common(10))
print(fdist["Grail"])