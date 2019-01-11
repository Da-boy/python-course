#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 0010 下午 8:31
# @Author  : Aries
# @Site    : 
# @File    : file1.py
# @Software: PyCharm Community Edition

f = open('file/test', mode='rb')
bs = f.read()
print(bs.decode('utf-8'))
f.close()


f = open('file/test', mode='wb')
f.write('hello'.encode('utf-8'))
f.flush()
f.close()

f = open('file/test', mode='ab')
f.write('world'.encode('utf-8'))
f.flush()
f.close()
# b:处理非文本
