#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 0017 下午 9:14
# @Author  : Aries
# @Site    : 
# @File    : 封装.py
# @Software: PyCharm Community Edition


#私有静态字段

class B:
    __money = 900000

class A(B):
    name = 'jia'
    __age = 1000
    def func(self):
        print(self.__age)
        print(A.__age)
        print('haha')
    def func1(self):
        print(self.__money)
        print(A.__money)
a1 = A()

# print(a1.__age)   实例化对象不能访问私有静态字段
# print(A.__age)   类名不能访问私有静态字段

# 对于私有静态字段，类的外部不能访问

# 对于私有静态字段，类的内部可以访问
a1.func()

#对于私有静态变量来说，只能在本类中内部访问，类的外部，派生类均不能访问
# a1.func1()
#其实可以访问，但工作中不能使用
print(a1._A__age)
print(A.__dict__)