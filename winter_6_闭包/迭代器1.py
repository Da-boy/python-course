#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 0014 下午 3:52
# @Author  : Aries
# @Site    : 
# @File    : 闭包1.py
# @Software: PyCharm Community Edition
from collections import Iterable  # 可迭代的
from collections import Iterator  # 迭代器

f = open('函数.txt', mode='r', encoding='utf-8')
print(isinstance(f, Iterable))
print(isinstance(f, Iterator))

for line in f:
    print(line)
