#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 0013 上午 10:09
# @Author  : Aries
# @Site    : 
# @File    : 动态传参1.py
# @Software: PyCharm Community Edition


def sum(*n):
    sum2 = 0
    for el in n:
        sum2 += el
    return sum2


print(sum(9, 9, 0))
