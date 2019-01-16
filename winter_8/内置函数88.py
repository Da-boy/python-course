#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 0016 上午 9:34
# @Author  : Aries
# @Site    : 
# @File    : 内置函数1.py
# @Software: PyCharm Community Edition

print(any([0, 'sj', 98, 'asd']))
print(all([0, 'sj', 98, 'asd']))

lst1 = ['wang', 'ni', 'ma']
lst2 = ['tian', 'tiang', 'jian']
lst3 = [12, 23, 54, 67, 789, 89, 90]
for el in zip(lst1, lst2, lst3):
    print(el)
