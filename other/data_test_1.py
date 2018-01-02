#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import re
import string

def cleanInput(input):
    """清理数据。"""
    input = re.sub('\n+', " ", input)   # 多'\n'替换为一个空格
    input = re.sub(r'[[0-9]*]', "", input) # 删除所有应用标记，例：[1]
    input = re.sub(' +', " ", input)    # 多空格替换为一个空格
    input = bytes(input, "UTF-8")       # 把内容转换为'UTF-8'消除转义字符
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation) # 删除标点符号
        # 删除单字符的单词，除非这个字符是"i"或"a"。
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def ngrams(input, n):
    """
    把字符串内容，转换为n-gram列表。
    例如："a b c" 2-gram是：[['a', 'b'], ['b', 'c']]。
    """
    inputs = cleanInput(input)
    output = []
    for i in range(len(inputs)-n+1):
        output.append(inputs[i:i+n])
    outputDict = {}
    for words in output:
        wordString = " ".join(words)
        if wordString in outputDict:
            outputDict[wordString] += 1
        else:
            outputDict[wordString] = 1
    return outputDict

try:
    html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
except URLError as e:
    print(e)
except HTTPError as e:
    print(e)
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
ngrams = ngrams(content, 2)
ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
print(ngrams)
print("2-grams count is: " + str(len(ngrams)))