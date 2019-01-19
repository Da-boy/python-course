#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 0013 上午 10:09
# @Author  : Aries
# @Site    : 
# @File    : 动态传参1.py
# @Software: PyCharm Community Edition

def hello(*he):
    print('this is', he)


hello('hello', 'world')


def func(a, b, c, *args, d=5):
    print(a, b, c, d, args)


func(1, 2, 3)
func(1, 2, 3, 4, 5, 6, 7)
