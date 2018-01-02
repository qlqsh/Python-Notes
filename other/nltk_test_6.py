#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nltk.book import *
from nltk import word_tokenize
from nltk import pos_tag
text = word_tokenize("Strange women lying in ponds distributing swords is no basis for a system of government. Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony.")
# 词性分析
print(pos_tag(text))