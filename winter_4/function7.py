#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 0012 下午 4:03
# @Author  : Aries
# @Site    : 
# @File    : function3.py
# @Software: PyCharm Community Edition

# 1+2+3+...+100=?

def sum(n):
    i = 0
    count = 1
    while count <= n:
        i +=count
        count = count + 1
    return i
ret = sum(999)
print(ret)
