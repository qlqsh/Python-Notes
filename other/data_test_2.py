#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator

def cleanInput(input):
    """清理输入的文档数据。"""
    input = re.sub('\n+', " ", input).lower()   # 多'\n'替换为一个空格，小写。
    input = re.sub(r'[[0-9]*]', "", input)      # '[1]'样式的消除
    input = re.sub(' +', " ", input)            # 多空格替换为一个空格
    input = bytes(input, "UTF-8")               # 编码处理
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)   # 消除文字两端的标点符号
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item) # 除了'a'、'i'之外的单字符单词都不输入。
    return cleanInput

def ngrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        if not isCommon(input[i:i+n]):            
            ngramTemp = " ".join(input[i:i+n])
            if ngramTemp not in output:
                output[ngramTemp] = 0
            output[ngramTemp] += 1
    return output

def isCommon(ngram):
    """过滤没有意义的单词。就像汉语里的'的'、'地'、'得'。"""
    commonWords = [
        "the", "be", "and", "of", "a", "in", "to", "have", "it", "i",
        "that", "for", "you", "he", "with", "on", "do", "say", "this",
        "they", "is", "an", "at", "but","we", "his", "from", "that",
        "not", "by", "she", "or", "as", "what", "go", "their","can", 
        "who", "get", "if", "would", "her", "all", "my", "make", 
        "about", "know", "will", "as", "up", "one", "time", "has", 
        "been", "there", "year", "so", "think", "when", "which", "them", 
        "some", "me", "people", "take", "out", "into", "just", "see", 
        "him", "your", "come", "could", "now", "than", "like", "other", 
        "how", "then", "its", "our", "two", "more", "these", "want", 
        "way", "look", "first", "also", "new", "because", "day", "more", 
        "use", "no", "man", "find", "here", "thing", "give", "many", 
        "well"
    ]
    for word in ngram:
        if word in commonWords:
            return True
    return False

content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
ngrams = ngrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse=True)
print(sortedNGrams)