#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 加载nltk自带的9本书
from nltk.book import *

# 统计文本中不重复的单词，然后与总单词数据进行比较。
print(len(text6))
# print(len(words)) # 有问题。words找不到。
print(len(text6)/len(words)) 