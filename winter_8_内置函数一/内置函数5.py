#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 0016 上午 9:34
# @Author  : Aries
# @Site    : 
# @File    : 内置函数1.py
# @Software: PyCharm Community Edition

code1 = 'for i in range(4):print(i)'
com = compile(code1, "", mode='exec')
print(com)  # 不可见
exec(com)

code2 = '4+5+98'
com2 = compile(code2,"",mode='eval')
print(eval(com2))