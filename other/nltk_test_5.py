#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nltk.book import *
from nltk import ngrams
fourgrams = ngrams(text6, 4) # 4-grams
fourgramsDist = FreqDist(fourgrams)
# 默认结果：1次
print(fourgramsDist[("father", "smelt", "of", "elderberries")])

for fourgram in fourgrams:
    if fourgram[0] == "coconut":
        print(fourgram)