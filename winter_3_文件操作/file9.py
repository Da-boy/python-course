#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 0011 上午 10:20
# @Author  : Aries
# @Site    : 
# @File    : file7.py
# @Software: PyCharm Community Edition

f = open('file/test4', mode='r', encoding='utf-8')
for line in f: # 每次读取一行，赋值给前面的line变量
    print(line)
f.close()