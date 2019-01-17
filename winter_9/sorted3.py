#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 0017 上午 10:51
# @Author  : Aries
# @Site    : 
# @File    : sorted1.py
# @Software: PyCharm Community Edition
lst = ['helloaa', 'wangaaaa', 'aaaasda', 'asda', 'asa', '阿斯顿']


def func(s):
    return len(s)

def func2(s):
    return s.count('a') # 返回数字

ll = sorted(lst, key=func)
print(ll)

ll2 = sorted(lst, key=func2)
print(ll2)

ll3 = sorted(lst, key=lambda s: s.count('a'))
print(ll3)