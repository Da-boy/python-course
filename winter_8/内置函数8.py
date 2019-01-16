#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 0016 上午 9:34
# @Author  : Aries
# @Site    : 
# @File    : 内置函数1.py
# @Software: PyCharm Community Edition

s = '你是谁'
a = s.encode('utf-8')
print(a)


bs = bytes('你是谁', encoding='utf-8')
print(bs)


ret = bytearray('你是谁a' ,encoding='utf-8')
print(ret)
print(ret[0])
print(ret[9])
ret[0] = 65
print(str(ret))