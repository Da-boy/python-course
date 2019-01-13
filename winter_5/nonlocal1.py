#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 0013 下午 3:37
# @Author  : Aries
# @Site    : 
# @File    : nonlocal1.py
# @Software: PyCharm Community Edition

a = 1


def func1():
    a = 2

    def func2():

        def func3():
            nonlocal a
            a = 4
            print(a)

        print(a)
        func3()
        print(a)

    print(a)
    func2()
    print(a)


print(a)
func1()
print(a)