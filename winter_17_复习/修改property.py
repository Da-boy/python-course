#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 0021 下午 9:47
# @Author  : Aries
# @Site    : 
# @File    : 修改property.py
# @Software: PyCharm Community Edition


class A:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter # 修改名字
    def name(self,new_name):
        if type(new_name) is str:
            self.__name = new_name

    @name.deleter
    def name(self):
        del self.__name


a = A('pp')
print(a.name)
a.name = '333'
print(a.name)