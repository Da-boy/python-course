#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 0013 上午 11:28
# @Author  : Aries
# @Site    : 
# @File    : 命名空间1.py
# @Software: PyCharm Community Edition

a = 10
def func1():
    global a
    a = 30
    print(a)
func1()
print(a)