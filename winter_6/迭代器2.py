#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 0014 下午 3:52
# @Author  : Aries
# @Site    : 
# @File    : 闭包1.py
# @Software: PyCharm Community Edition

lst = [1, 2, 3]

lst1 = lst.__iter__().__iter__().__iter__()

print(lst1.__next__())
lst1.__next__()
print(lst1.__next__())
