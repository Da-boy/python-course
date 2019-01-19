#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 0013 下午 3:32
# @Author  : Aries
# @Site    : 
# @File    : global.py
# @Software: PyCharm Community Edition

def func1():
    a =10
    def func2():
        nonlocal a
        a = 20
        print(a)
    func2()
    print(a)
func1()