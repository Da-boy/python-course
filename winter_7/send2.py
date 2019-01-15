#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 0015 上午 8:47
# @Author  : Aries
# @Site    : 
# @File    : 生成器.py
# @Software: PyCharm Community Edition

def func():
    yield 11
    yield 2
    yield 3
    yield 4
    yield 5
g = func()

lst = list(g)
print(g)
print(lst)