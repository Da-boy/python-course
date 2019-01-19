#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 0017 下午 4:16
# @Author  : Aries
# @Site    : 
# @File    : filter.py
# @Software: PyCharm Community Edition

lst = [
    {'id': 1, 'name': 'jia', 'age': 10},
    {'id': 2, 'name': 'jia23', 'age': 120},
    {'id': 3, 'name': 'jia3', 'age': 20},
    {'id': 4, 'name': 'jia4', 'age': 30},
    {'id': 5, 'name': 'jia6', 'age': 40}
]

print(list(filter(lambda i: i['age'] >= 38, lst)))

