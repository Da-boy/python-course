# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 0019 上午 10:39
# @Author  : Aries
# @Site    : 
# @File    : 反射.py
# @Software: PyCharm Community Edition

#使用对象进行反射,方法，对象属性
class S:
    def __init__(self, name):
        self.name = name

    def func(self):
        print('func')


a = S('ff')
print(a.name)
print(getattr(a,'name'))
getattr(a,'func')()


setattr(a,'name','haha')
print(a.__dict__)