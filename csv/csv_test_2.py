#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
except URLError as e:
    print(e)
except HTTPError as e:
    print(e)

bsObj = BeautifulSoup(html, "html.parser")
# 主对比表格是当前页面上的第一个表格
table = bsObj.findAll("table", {"class": "wikitable"})[0]
rows = table.findAll("tr")

csvFile = open("./files/editors.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()