#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 0008 上午 11:07
# @Author  : Aries
# @Site    : 
# @File    : dict3.py
# @Software: PyCharm Community Edition

dic = {'key1': '1', 'key2': '2', 'key3': '3', 'key4': '4'}
dic1 = {'key1': '1g', 'key2': '22', 'key3': '3', 'key4': '4', 'key5': '5'}
dic.update(dic1)
dic1.update(dic)
print(dic)
print(dic1)
