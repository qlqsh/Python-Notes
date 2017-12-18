#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# lambda测试

li = [
    {"age": 20, "name": "def"},
    {"age": 25, "name": "abc"},
    {"age": 10, "name": "ghi"}
]

# 正常使用
def comp(x):
    return x["age"]
newli1 = sorted(li, key=comp)
print(newli1)

# 使用lambda
newli2 = sorted(li, key=lambda x: x["age"])
print(newli2)
