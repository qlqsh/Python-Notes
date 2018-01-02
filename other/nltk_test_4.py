#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nltk.book import *
from nltk import bigrams
bigrams = bigrams(text6) # 2-gram模型
bigramsDist = FreqDist(bigrams)
print(bigramsDist[("Sir", "Robin")]) # 出现次数。应该是18