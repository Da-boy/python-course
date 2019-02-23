#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 0023 下午 2:44
# @Author  : Aries
# @Site    : 
# @File    : eq.py
# @Software: PyCharm Community Edition


class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True


a1 = A('wang', 15)
a2 = A('wang', 15)
a3 = A('wang', 15)
a4 = A('wang', 15)
a5 = A('wang', 15)
a6 = A('wang', 15)

print(a1 == a3)
