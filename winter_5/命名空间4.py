#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 0013 上午 11:28
# @Author  : Aries
# @Site    : 
# @File    : 命名空间1.py
# @Software: PyCharm Community Edition

a = 20


def func():
    a = 10
    print(a)
    print(globals())
    print(locals())

func()

print(globals())
print(locals())