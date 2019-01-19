#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 0015 下午 9:39
# @Author  : Aries
# @Site    : 
# @File    : 推导式3.py
# @Software: PyCharm Community Edition


lst1 = ['a', 'b', 'c', 'd']

lst2 = [1, 2, 3, 4]

dic = {lst1[i]:lst2[i] for i in range(len(lst1))}
print(dic)