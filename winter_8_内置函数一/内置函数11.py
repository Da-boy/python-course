#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 0016 上午 9:34
# @Author  : Aries
# @Site    : 
# @File    : 内置函数1.py
# @Software: PyCharm Community Edition

lst = ['a','b','c','d']
for i in range(len(lst)):
    print(i)
    print(lst[i])

for index,el in enumerate(lst,1): # 把索引和元素一起获取，索引默认从0开始，可以更改
    print(index)
    print(el)