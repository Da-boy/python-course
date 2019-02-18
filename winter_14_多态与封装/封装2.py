#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 0017 下午 9:14
# @Author  : Aries
# @Site    : 
# @File    : 封装.py
# @Software: PyCharm Community Edition


# 面试题
class Parent:
    def __func(self):
        print('in Parent func')

    def __init__(self):
        self.__func()


class Son(Parent):
    def __func(self):
        print('in Son')


son1 = Son()
