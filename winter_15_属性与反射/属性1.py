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

        if type(age) is int:
            self.__age = age
        else:
            print('数额有误')

    @property
    def age(self):
        return self.__age

    @age.setter  # 把属性变成可修改对象
    def age(self, a):
        if type(a) is int:
            self.__age = a
        else:
            print('数额有误')


p1 = Person('wo', 12)
print(p1.age)  # 方法伪装成一个属性

p1.age = 88
print(p1.age)