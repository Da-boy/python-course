#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 0026 下午 7:46
# @Author  : Aries
# @Site    : 
# @File    : manager.py
# @Software: PyCharm Community Edition


try:
    f = open('userinfo')
    print(f.read())
    print(__file__)
finally:
    f.close()
