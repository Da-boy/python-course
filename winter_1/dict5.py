#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 0008 上午 11:07
# @Author  : Aries
# @Site    : 
# @File    : dict3.py
# @Software: PyCharm Community Edition

dic = {'key1': '1', 'key2': '2', 'key3': '3', 'key4': '4'}
print(dic.get('key1'))
print(dic.get('hehe'))
print(dic['key2'])
print(dic.setdefault('key3'))
print(dic.setdefault('key3', '88'))