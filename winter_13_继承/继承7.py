#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 0013 下午 7:42
# @Author  : Aries
# @Site    : 
# @File    : 继承.py
# @Software: PyCharm Community Edition

# 多继承：
# 	新式类：查询顺序遵循广度优先
# 	经典类：查询顺序遵循深度优先
class A:
    def func(self):
        print('in A')


class B(A):
    def func(self):
        print('in B')


class C(A):
    def func(self):
        print('in C')
class D(B):
    def func(self):
        print('in D')
class E(C):
    def func(self):
        print('in E')
class F(D,E):
    def func(self):
        print('in F')
f1 = F()
f1.func()
print(F.mro()) # 查询类的继承顺序


