#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 0018 下午 2:38
# @Author  : Aries
# @Site    : 
# @File    : 类方法.py
# @Software: PyCharm Community Edition


class A:
    def func(self): # 普通方法
        print(self)
    @classmethod
    def func1(cls): # 类方法
        print(cls)
A.func1()

a1 = A()
a1.func1() # 对象调用类方法，cls得到的是类本身
