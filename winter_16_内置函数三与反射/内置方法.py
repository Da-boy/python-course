#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 0020 下午 8:07
# @Author  : Aries
# @Site    : 
# @File    : 内置方法.py
# @Software: PyCharm Community Edition


# __call__
class A:
    def __call__(self, *args, **kwargs):
        print('this is call')


# a = A()
# a()   # 相当于调用__call__方法
# A()() # 相当于调用__call__方法

class B:
    def __init__(self, cls):
        self.a = cls()
        self.a()


B(A)
