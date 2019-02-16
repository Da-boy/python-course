#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 0013 下午 7:42
# @Author  : Aries
# @Site    : 
# @File    : 继承.py
# @Software: PyCharm Community Edition


# 单继承：新式类，经典类查询顺序一样

class A:
    def func(self):
        print('in A')


class B(A):
    def func(self):
        print('in B')


class C(B):
    pass
    # def func(self):
    #     print('in C')

c1 = C()
c1.func()


