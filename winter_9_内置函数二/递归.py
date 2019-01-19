#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 0017 下午 6:40
# @Author  : Aries
# @Site    : 
# @File    : 递归.py
# @Software: PyCharm Community Edition

import os
filePath = 'F:\python课程\python-course'

it  = os.listdir(filePath)
for el in it:
    print(el)