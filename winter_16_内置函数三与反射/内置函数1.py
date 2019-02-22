#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 0019 上午 10:12
# @Author  : Aries
# @Site    : 
# @File    : 内置函数.py
# @Software: PyCharm Community Edition


# issubclass() 判断类与类之间的继承关系

class A:
    pass
class B(A):
    pass

print(issubclass(B,A))
print(issubclass(A,B))