#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/20 0020 上午 10:53
# @Author  : Aries
# @Site    : 
# @File    : 面向对象2.py
# @Software: PyCharm Community Edition


class Count:
    count = 0

    def __init__(self):
        Count.count = Count.count + 1


obj1 = Count()
obj2 = Count()
obj3 = Count()
obj4 = Count()
obj5 = Count()
print(Count.count)