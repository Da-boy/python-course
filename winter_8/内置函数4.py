#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 0016 上午 9:34
# @Author  : Aries
# @Site    : 
# @File    : 内置函数1.py
# @Software: PyCharm Community Edition
s = 'for i in range(12):print(i)'
a = exec(s)


str1 = '''
def func():
    print('hahh')
func()
'''
exec(str1)


