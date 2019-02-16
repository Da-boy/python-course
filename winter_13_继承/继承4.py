#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 0013 下午 7:42
# @Author  : Aries
# @Site    : 
# @File    : 继承.py
# @Software: PyCharm Community Edition


# 既要执行子类的方法，又要执行父类的方法
# 方法1、 Animal.__init__(self, name, age)
# 方法2、 super().__init__(name, age)  工作中使用方法2
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s吃东西%s' % (self.name, self.age))


class bird(Animal):
    def __init__(self, name, age, wing):
        
        # Animal.__init__(self, name, age)
        super().__init__(name, age)
        self.wing = wing

    def bork(self):
        print('bork')


b1 = bird('鸟', 2, '翅膀')
b1.bork()
b1.eat()
print(b1.__dict__)
