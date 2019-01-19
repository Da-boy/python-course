#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 0017 下午 4:27
# @Author  : Aries
# @Site    : 
# @File    : map.py
# @Software: PyCharm Community Edition
lst = [1, 2, 3, 4, 5, 6]

it = map(lambda i: i ** 2, lst)
print(list(it))
