#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 0015 上午 8:47
# @Author  : Aries
# @Site    : 
# @File    : 生成器.py
# @Software: PyCharm Community Edition


def func():
    print('aaa')
    a = yield '111'
    print('a=', a)
    print('bbb')
    b = yield '222'
    print('b=',b)
    print('ccc')
    c = yield '333'
    print('c=',c)

g = func()

print(g.__next__())
print(g.send(1))
print(g.send(2))
print(g.send(3))