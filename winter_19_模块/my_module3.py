#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/24 0024 下午 6:51
# @Author  : Aries
# @Site    : 
# @File    : my-module3.py
# @Software: PyCharm Community Edition


import sys
print(__name__)
print(sys.modules[__name__]) # sys.modules[__name__]写在那个文件里，就代表那个命名空间

def func():
    print('func')

getattr(sys.modules[__name__],'func')()