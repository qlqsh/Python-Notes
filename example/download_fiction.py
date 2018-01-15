#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  从166小说阅读网爬小说的爬虫
import re, os, time
import requests
from bs4 import BeautifulSoup

# 通过URL获取小说目录
headers = {
    'User-Agent': 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'
}

def urlList(catalogURL):
    """通过目录URL获取所有的章节URL"""
    r = requests.get(catalogURL, headers=headers, timeout=20) # 设定headers
    html = r.text.encode('iso-8859-1').decode('gbk') # 编码转换
    urls = []
    bsObj = BeautifulSoup(html, "html.parser") # html解析
    for a in bsObj.findAll("a", href=re.compile(r"^[0-9]+.html")): # 过滤URL
        urls.append(str(catalogURL+a["href"]))
    return urls[1:] # 删掉第一个最新章节URL，因为重复。

def getAnChapter(url, waittime=3):
    """获取一章的标题、内容"""
    time.sleep(waittime) # 等待2秒，过于频繁会被网站封杀的。
    r = requests.get(url, headers=headers, timeout=10)
    if r.status_code == requests.codes.ok: # 正常访问
        html = r.text.encode('iso-8859-1').decode('gbk', 'ignore')
        html = html.replace('<br />', '\n') # 转换br
        bsObj = BeautifulSoup(html, "html.parser")
        [s.extract() for s in bsObj(['script', 'span', 'strong'])] # 移除不需要的Tag
        title = bsObj.find("h2").text 
        content = bsObj.find("p", {"class": "Book_Text"}).get_text()
        if title == None or content == None:
            return None
        return Chapter(title, content.replace('166小说阅读网', ''))
    return None

class Chapter(object):
    """章节类（包括标题、内容）"""
    def __init__(self, title, content):
        super(Chapter, self).__init__()
        self.title = title
        self.content = content

def writeChapterToTxt(chapter, filename):
    """将一章的内容写入到指定文档"""
    txtPath = "/Users/liuming/Documents/"+filename+".txt"
    if chapter != None:        
        if os.path.exists(txtPath): # 判断文件是否存在
            with open(txtPath, 'a') as f:
                f.write("\n\n")
                f.write(chapter.title)
                f.write(chapter.content)
        else:
            with open(txtPath, 'w') as f:
                f.write(chapter.title)
                f.write(chapter.content)

def createTxt(catalogURL, filename):
    """通过目录URL，获取小说内容，保存到本地"""
    urls = urlList(catalogURL)
    count = 0
    total = len(urls)
    for url in urls:
        count += 1
        print("获取：" + url)
        print("%.2f%%" % (count/total*100))
        chapter = getAnChapter(url)
        writeChapterToTxt(chapter, filename)

# createTxt('http://www.166xs.com/xiaoshuo/90/90168/', '放开那个女巫')
# createTxt('http://www.166xs.com/xiaoshuo/82/82802/', '科学家日记')
createTxt('http://www.166xs.com/xiaoshuo/111/111048/', '末世之黑夜将至')
