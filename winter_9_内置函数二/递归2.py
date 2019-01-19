#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 0017 下午 6:40
# @Author  : Aries
# @Site    : 
# @File    : 递归.py
# @Software: PyCharm Community Edition

import sys

sys.setrecursionlimit(10000)  # 增加最大循环次数


def func(count):
    print('hello' + str(count))
    func(count + 1)


func(1)
