#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 0008 上午 11:07
# @Author  : Aries
# @Site    : 
# @File    : dict3.py
# @Software: PyCharm Community Edition

dic = {'key1': '1g', 'key2': '2', 'key3': '3', 'key4': '4'}

print(dic.keys())
print(list(dic.keys()))
for key in dic.keys():
    print(key)
print(dic.values())
for value in dic.values():
    print(value)
print(dic.items())
it = dic.__iter__()
from collections import Iterable  # 可迭代的
print(isinstance(it, Iterable))
print(list(dic.items()))
for key, value in dic.items():
    print(key, value)
