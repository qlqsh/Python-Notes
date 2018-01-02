#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='nianchuanyuan', db='', charset='utf8')
cur = conn.cursor()
cur.execute("USE wikipedia") # 使用指定数据库

# 发现答案（运行时错误扩展）
class SolutionFound(RuntimeError):
    def __init__(self, message):
        super(SolutionFound, self).__init__()
        self.message = message

# 获得链接。
def getLinks(fromPageId):
    cur.execute("SELECT toPageId FROM links WHERE fromPageId = %s", (fromPageId))
    if cur.rowcount == 0:
        return None
    else:
        return [x[0] for x in cur.fetchall()]

# 构建字典。
def constructDict(currentPageId):
    links = getLinks(currentPageId)
    if links:
        return dict(zip(links, [{}]*len(links))) # 这有什么用不太清楚
    return {}

# 理解起来相当费劲。
def searchDepth(targetPageId, currentPageId, linkTree, depth):
    if depth == 0:
        # 停止递归，返回结果
        return linkTree
    if not linkTree:
        linkTree = constructDict(currentPageId)
        if not linkTree:
            # 若此节点页面无链接，则跳过此节点
            return {}
        if targetPageId in linkTree.keys():
            print("TARGET " + str(targetPageId) + " FOUND!")
            raise SolutionFound("PAGE: " + str(currentPageId))
        
        for branchKey, branchValue in linkTree.items():
            try:
                # 递归建立链接树
                linkTree[branchKey] = searchDepth(targetPageId, branchKey, branchValue, depth-1)
            except SolutionFound as e:
                print(e.message)
                raise SolutionFound("PAGE: " + str(currentPageId))
        return linkTree

try:
    searchDepth(134951, 1, {}, 4)
    print("No solution found")
except SolutionFound as e:
    print(e.message)
finally:
    cur.close()
    conn.close()