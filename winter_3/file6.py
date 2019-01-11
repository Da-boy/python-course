#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 0010 下午 8:31
# @Author  : Aries
# @Site    : 
# @File    : file1.py
# @Software: PyCharm Community Edition

f = open('file/test3', mode='w+', encoding='utf-8')
f.write('weather')
f.seek(0)
s = f.read()
print(s)
f.flush()
f.close()