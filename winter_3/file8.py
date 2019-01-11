#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 0011 上午 10:20
# @Author  : Aries
# @Site    : 
# @File    : file7.py
# @Software: PyCharm Community Edition

import os
with open('file/test4', mode='r', encoding='utf-8') as f1, \
        open('file/test4_1', mode='w', encoding='utf-8') as f2:
    s =f1.read()
    ss = s.replace('j', 'w')
    f2.write(ss)
os.remove('file/test4')
os.rename('file/test4_1', 'file/test4')