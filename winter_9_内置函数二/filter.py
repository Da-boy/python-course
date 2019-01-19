#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 0017 下午 4:16
# @Author  : Aries
# @Site    : 
# @File    : filter.py
# @Software: PyCharm Community Edition

lst = [1, 2, 3, 4, 5, 67, 89, ]

ll = filter(lambda i: i % 2 == 1, lst)
print(ll)
print('__iter__' in dir(ll))
print('__next__' in dir(ll))  # filter()是迭代器

print(list(ll))  # 获取迭代器中的元素
