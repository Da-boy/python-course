#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 0011 上午 10:20
# @Author  : Aries
# @Site    : 
# @File    : file7.py
# @Software: PyCharm Community Edition

f = open('file/test3', mode='r+', encoding='utf-8')
f.read(3)
f.seek(6)
print(f.read())