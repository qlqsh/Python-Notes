#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nltk import word_tokenize
from nltk import Text

tokens = word_tokenize("Here is some not very interesting text")
text = Text(tokens)
print(text)