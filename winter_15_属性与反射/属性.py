#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 0018 上午 11:12
# @Author  : Aries
# @Site    : 
# @File    : 属性.py
# @Software: PyCharm Community Edition


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter  # 把属性变成可修改对象
    def age(self, a):
        print(a)


p1 = Person('wo', 19)
print(p1.age)  # 方法伪装成一个属性

p1.age = 88
