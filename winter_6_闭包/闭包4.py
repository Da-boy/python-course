#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 0014 下午 3:52
# @Author  : Aries
# @Site    : 
# @File    : 闭包1.py
# @Software: PyCharm Community Edition
lst = ['h', 'e', 'l', 'l', 'o']

it = lst.__iter__()
# print(it.__next__(), end='')
# print(it.__next__(), end='')
# print(it.__next__(), end='')
# print(it.__next__(), end='')
# print(it.__next__(), end='')


while True:
    try:
        name = it.__next__()
        print(name)
    except StopIteration:
        break

