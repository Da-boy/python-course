#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 0017 下午 9:14
# @Author  : Aries
# @Site    : 
# @File    : 封装.py
# @Software: PyCharm Community Edition


#私有静态方法

class B:
    __money = 900000
    def __f1(self):
        print('heheh')

class A(B):
    name = 'jia'
    __age = 1000
    def __func(self):
        print('haha')
    def func1(self):
        self.__func()
    def func2(self):
        self.__f1() # 无法访问父类的f1函数
a1 = A()
# a1.__func() 类外部不能访问
a1.func1()