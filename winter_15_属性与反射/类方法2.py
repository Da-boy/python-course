#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 0018 下午 2:38
# @Author  : Aries
# @Site    : 
# @File    : 类方法.py
# @Software: PyCharm Community Edition


class A:
    count = 13
    @classmethod
    def func1(cls): # 此方法无需对象参与
        print(cls)
        print(cls.count)
        #对B中所有内容都可以进行修改
class B(A):
    count = 99
A.func1()
B.func1()
