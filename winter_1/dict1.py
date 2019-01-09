#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 0008 上午 10:29
# @Author  : Aries
# @Site    : 
# @File    : dict1.py
# @Software: PyCharm Community Edition

dic = {'百度':'李彦宏'}
dic['腾讯'] = "马化腾" #新增
dic['腾讯'] = "马勇" #如果key重复，会替换掉原来的value
print(dic)