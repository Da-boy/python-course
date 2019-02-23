#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 0023 上午 10:55
# @Author  : Aries
# @Site    : 
# @File    : item.py
# @Software: PyCharm Community Edition


# 在内置模块中，有一些特殊的方法，要求对象必须实现__getitem__/__setitem__才能使用

class B:
    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __delitem__(self, key):
        return delattr(self, key)


b = B()
b.k1 = 'v1'  # 触发__setitem__
print(b.k1)  # 触发__getitem__
del b['k1']  # 触发__delitem__
# print(b.k1)
