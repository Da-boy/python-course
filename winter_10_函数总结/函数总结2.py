#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/18 0018 上午 11:27
# @Author  : Aries
# @Site    : 
# @File    : 函数总结1.py
# @Software: PyCharm Community Edition
def func1():
    a = 1
    b = 2
    print(a)

    def func2():
        b = 3
        print(b)
    func2()
    print(666)
    print(b)
    return func2
func1()()
