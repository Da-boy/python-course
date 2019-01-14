#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 0014 下午 3:52
# @Author  : Aries
# @Site    : 
# @File    : 闭包1.py
# @Software: PyCharm Community Edition

from collections import Iterable  # 可迭代的
from collections import Iterator  # 迭代器

lst = [1, 2, 3]
print(isinstance(lst, Iterable))
print(isinstance(lst, Iterator))
print('------')
it = lst.__iter__()
print(isinstance(it, Iterable))
print(isinstance(it, Iterator))
print('----')

