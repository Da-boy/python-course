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
        Count.count = self.count +1


Count.count = 6 # 通过类名可以改变类中的静态变量值
obj1 = Count()
print(Count.count)

obj2 = Count()
obj2.count = 10 # 通过对象，只能引用类中的静态变量
print(Count.count)


