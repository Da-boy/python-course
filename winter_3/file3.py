#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 0010 下午 8:31
# @Author  : Aries
# @Site    : 
# @File    : file1.py
# @Software: PyCharm Community Edition

f = open('file/test', mode='a', encoding='utf-8')
f.write('dafff')
f.flush()
f.close()