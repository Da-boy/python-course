#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 0017 上午 9:54
# @Author  : Aries
# @Site    : 
# @File    : lambda.py
# @Software: PyCharm Community Edition

def func(n):
    return n + n


print(func(5))
print(func.__name__) 
c = func
c(66)
print(c.__name__) #查看函数名

a = lambda x: x + x # 一行搞定一个函数，但不能完成复杂的函数操作
# lambda 匿名函数
# x 为参数
# :后面是函数体
print(a)
print(a(6))

b = lambda x,y:x+y
print(b(3,6))
