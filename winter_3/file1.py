#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 0010 下午 8:31
# @Author  : Aries
# @Site    : 
# @File    : file1.py
# @Software: PyCharm Community Edition

f = open('文件操作.txt',mode='r',encoding='utf-8')
s = f.read()
f.close() #记得关闭句柄
print(s)