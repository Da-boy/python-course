#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 0017 上午 9:54
# @Author  : Aries
# @Site    : 
# @File    : lambda.py
# @Software: PyCharm Community Edition

a = lambda d, y: d * y
print(a(3, 6))
print(a.__name__)

b = lambda x, y: x + y
print(b(3, 6))
print(b.__name__)
