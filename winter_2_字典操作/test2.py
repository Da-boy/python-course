#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 0009 下午 2:11
# @Author  : Aries
# @Site    : 
# @File    : test1.py
# @Software: PyCharm Community Edition

zhubo = {
    'jay': 10000,
    'jj': 30000,
    'way': 50000,
    'doc': 40000
}
sum = 0
for value in zhubo.values():
    sum += value
print(sum/len(zhubo))
avg = sum/len(zhubo)

lst = []
for k,v in zhubo.items():
    if v < int(avg):
        lst.append(k)
for el in lst :
    zhubo.pop(el)
print(zhubo)