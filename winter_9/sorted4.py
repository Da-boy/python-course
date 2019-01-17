#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 0017 上午 10:51
# @Author  : Aries
# @Site    : 
# @File    : sorted1.py
# @Software: PyCharm Community Edition
lst = ['hello', 'wang', 'sda', 'sd', 's', '阿斯顿']


def func(s):
    return len(s)


ll = sorted(lst, key=func)
print(ll)
