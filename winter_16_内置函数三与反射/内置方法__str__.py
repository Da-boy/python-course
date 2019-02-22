#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 0021 下午 4:25
# @Author  : Aries
# @Site    : 
# @File    : 内置方法__str__.py
# @Software: PyCharm Community Edition

class Student:
    def __init__(self,name,stu_cls):
        self.name = name
        self.cls = stu_cls

    def __str__(self):
        return '%s %s' % (self.cls,self.name)

h1 = Student('yu','py12')
h2 = Student('wangu','py13')
print(h1)
print(h2)
# print一个对象相当于调用一个对象的__str__方法