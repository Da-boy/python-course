#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 0023 上午 11:07
# @Author  : Aries
# @Site    : 
# @File    : item1.py
# @Software: PyCharm Community Edition

# 操作列表

class B:
    def __init__(self, lst):
        self.lst = lst

    def __getitem__(self, item):
        return self.lst[item]

    def __setitem__(self, key, value):
        self.lst[key] = value


b = B(['111', '222', 'fff', 'kkk'])

# print(b.lst)
# print(b.lst[0])
print(b[0])
b[2] = 'haha'
print(b.lst)
