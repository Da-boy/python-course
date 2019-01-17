#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 0017 下午 4:27
# @Author  : Aries
# @Site    : 
# @File    : map.py
# @Software: PyCharm Community Edition
lst1 = [1, 3, 5, 6, 8]
lst2 = [2, 4, 6, 8, 0]

it = map(lambda x, y: x + y, lst1, lst2)
print(list(it))

lst3 = [3, 5, 6, 7]
it1 = map(lambda x, y: x * y, lst1, lst3)
print(list(it1))
