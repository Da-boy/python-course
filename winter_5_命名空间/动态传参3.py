#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 0013 上午 10:09
# @Author  : Aries
# @Site    : 
# @File    : 动态传参1.py
# @Software: PyCharm Community Edition

def func(**food):
    print(food)


func(id=1, str='mean', la='zh')
