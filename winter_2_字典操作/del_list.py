#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 0009 下午 9:20
# @Author  : Aries
# @Site    : 
# @File    : del_list.py
# @Software: PyCharm Community Edition

lst = {'jay': 'jay', 'jj': 'jj', 'kay': 'kay', 'ou': 'ju'}
del_lst = []
for k in lst:
    if 'j' in k:
        del_lst.append(k)
for el in del_lst:
    del lst[el]
print(lst)
