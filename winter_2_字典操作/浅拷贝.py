#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 0010 上午 9:19
# @Author  : Aries
# @Site    : 
# @File    : 浅拷贝.py
# @Software: PyCharm Community Edition


lst1 = ['jay', 'jaa', 'juy']
lst2 = lst1

lst2.append('jyy')
print(lst2)
print(lst1)

# 浅拷贝
lst3 = ['wang','tuo', 'rong']

lst4 = lst3.copy()
lst5 = lst3[:]


lst4.append('hao')
print(lst3,id(lst3))
print(lst4,id(lst4))
print(lst5, id(lst5))