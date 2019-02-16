#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 0013 下午 7:42
# @Author  : Aries
# @Site    : 
# @File    : 继承.py
# @Software: PyCharm Community Edition


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s吃东西%s' % (self.name,self.age))


class Dog(Animal):
    pass


class Cat:
    pass


class Chick:
    pass

eat1 = Dog('tom',1)
eat1.eat()