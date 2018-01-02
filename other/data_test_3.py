#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from random import randint

def wordListSum(wordList):
    """单词列表总数（单词出现的总次数）"""
    sum = 0
    for word, value in wordList.items():
        sum += value
    return sum

def retrieveRandomWord(wordList):
    """提取一个随机单词，value越高出现的可能性越大。"""
    randIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word

def buildWordDict(text):
    """建立一个词典。格式：{单词：{后面出现的单词：次数}, ...}"""
    # 替换换行符和引号
    text = text.replace("\n", " ")
    text = text.replace("\"", "")
    
    # 保留标点符号，两端加空格。这样分割的时候标点符号会单独保留下来。
    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, " " + symbol + " ")
    
    # 分割单词，过滤空单词
    words = text.split(" ")
    words = [word for word in words if word != ""]
    
    wordDict = {}
    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
            # 为单词新建一个词典
            wordDict[words[i-1]] = {}
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]] = 0
        wordDict[words[i-1]][words[i]] = wordDict[words[i-1]][words[i]]+1
    return wordDict

text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
wordDict = buildWordDict(text)

# 生成链长100的马尔可夫链
length = 100
chain = ""
currentWord = "I"
for i in range(0, length):
    chain += currentWord + " "
    currentWord = retrieveRandomWord(wordDict[currentWord])
print(chain)
