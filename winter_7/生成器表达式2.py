#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 0015 上午 10:59
# @Author  : Aries
# @Site    : 
# @File    : 生成器表达式1.py
# @Software: PyCharm Community Edition

def func():
    print(111)
    yield 222


g = func()
g1 = (i for i in g)
g2 = (i for i in g1)
print(list(g))
print(list(g1))
print(list(g2))
