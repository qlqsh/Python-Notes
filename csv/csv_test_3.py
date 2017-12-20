#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode("ascii", "ignore")
dataFile = StringIO(data)
# csvReader = csv.reader(dataFile) # 列表格式
# for row in csvReader:
#     print(row)

dictReader = csv.DictReader(dataFile) # 字典格式
print(dictReader.fieldnames) # 字段列表，也是字典对象的键
for row in dictReader:
    print(row)