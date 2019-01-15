#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 0015 上午 8:47
# @Author  : Aries
# @Site    : 
# @File    : 生成器.py
# @Software: PyCharm Community Edition


def func():
    print('hello')
    yield 'world'
    # return '99'
    print('----')
    yield '!!!!'
    print('first')
    print('second')
    yield 'hahahah'

print(func())
g = func()
print(g.__next__())
print(g.__next__())
print(g.__next__())