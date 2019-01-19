#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 0015 上午 10:35
# @Author  : Aries
# @Site    : 
# @File    : 推倒是.py
# @Software: PyCharm Community Edition

# 语法[最终结果（变量） for 变量 in 可迭代对象 if条件]

lst = [i for i in range(1, 101) if i % 2 == 0]
print(lst)

lst1 = [i for i in range(1, 101) if i % 3 == 0]
print(lst1)

lst2 = [i**2 for i in range(1, 101) if i % 3 == 0 ]
print(lst2)
