#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/18 0018 上午 11:27
# @Author  : Aries
# @Site    : 
# @File    : 函数总结1.py
# @Software: PyCharm Community Edition

def func(*args, **kwargs):
    print(args)
    print(*args)
    print(kwargs)


func(1, 2, 3, 4, a=2,b=3)

l1 = [1,2,3]
l2 = [4,12,32]
func(l1,l2)
func(*l1,*l2)
