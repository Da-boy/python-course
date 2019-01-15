#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 0015 上午 10:35
# @Author  : Aries
# @Site    : 
# @File    : 推倒是.py
# @Software: PyCharm Community Edition

# 生成列表里面包含1-14的数据
lst = []

for i in range(1, 15):
    lst.append('python %s' % i)
print(lst)
print()


# 语法[最终结果（变量） for 变量 in 可迭代对象]

lst = [i for i in range(1, 15)]
print(lst)
