#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 0026 下午 7:52
# @Author  : Aries
# @Site    : 
# @File    : 绝对路径.py
# @Software: PyCharm Community Edition

try:
    f = open(r'F:/python课程/python-course/winter_20_包/打开文件/doc/userinfo')  # r表示取消每一个'/'转义的意思
    print(f.read())
finally:
    f.close()
