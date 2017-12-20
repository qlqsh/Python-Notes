#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

try:
    wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
except URLError as e:
    print(e)
except HTTPError as e:
    print(e)
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')

wordObj = BeautifulSoup(xml_content.decode('utf-8'), "lxml-xml")
textStrings = wordObj.findAll("w:t")
for textElem in textStrings:
    closeTag = ""
    try:
        style = textElem.parent.previousSibling.find("w:pstyle")
        if style is not None and style["w:val"] == "Title":
            print("<h1>")
            closeTag = "</h1>"
    except AttributeError:
        pass
    print(textElem.text)
    print(closeTag)