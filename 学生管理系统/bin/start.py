#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 0025 下午 8:58
# @Author  : Aries
# @Site    : 
# @File    : start.py
# @Software: PyCharm Community Edition


import sys
lst = __file__.split('/')
base_path = '/'.join(lst[:-2])
sys.path.append(base_path)
from core import main

if __name__ == '__main__':
    print(sys.path)
    main.entry_point()
