#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 0014 上午 9:11
# @Author  : Aries
# @Site    : 
# @File    : 函数的应用.py
# @Software: PyCharm Community Edition


def f1():
    print('hello1')


def f2():
    print('hello2')


def f3():
    print('hello3')


def f4():
    print('hello4')


lst = [f1, f2, f3, f4]
print(lst)
for el in lst:
    el()
