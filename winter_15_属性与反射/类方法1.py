#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 0018 下午 2:38
# @Author  : Aries
# @Site    : 
# @File    : 类方法.py
# @Software: PyCharm Community Edition


class A:
    name = 'jia'
    count = 1
    @classmethod
    def func1(cls): # 此方法无需对象参与
        return cls.name + str(cls.count+8)

print(A.func1())

a1 = A()
print(a1.func1())
