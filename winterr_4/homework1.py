#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 0012 下午 7:32
# @Author  : Aries
# @Site    : 
# @File    : homework1.py
# @Software: PyCharm Community Edition

# 计算n是奇数还是偶数

def fn(n):
    if n % 2 == 0:
        return '偶数'
    else:
        return '奇数'


print(fn(135))
