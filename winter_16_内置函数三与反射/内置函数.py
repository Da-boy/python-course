#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 0019 上午 10:12
# @Author  : Aries
# @Site    : 
# @File    : 内置函数.py
# @Software: PyCharm Community Edition

class A:
    pass

class B(A):
    pass

b = B()
print(isinstance(b,B)) # 判断对象所属类型,包括继承关系
print(isinstance(b,A)) # 不包含所有的继承关系

# l = list()
# print(type

print(type(b) is A) # 不包含继承关系，只管一层
print(type(b) is B)

# == 值相等        is 内存地址相等
