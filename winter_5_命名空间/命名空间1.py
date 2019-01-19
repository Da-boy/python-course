#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 0013 上午 11:28
# @Author  : Aries
# @Site    : 
# @File    : 命名空间1.py
# @Software: PyCharm Community Edition

def func1():
    print('hehe')
def func2():
    func1()
    print('haha')
    func1()
func2()