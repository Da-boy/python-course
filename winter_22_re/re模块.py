#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 0009 下午 2:25
# @Author  : Aries
# @Site    : 
# @File    : re模块.py
# @Software: PyCharm Community Edition


import re

ret = re.findall('\d', '1203129da')
print(ret)  # 返回类型：列表

ret2 = re.search('\d', '287adsa12')
print(ret2)  # 如果匹配上了，返回类型：正则匹配结果的对象，返回值个数：1
print(ret2.group())  # 只能匹配第一个结果
if ret2:
    print(ret2.group()) # 先判断ret2是否有值,防止报错
ret3 = re.search('\s+', '12987897asd')
print(ret3)  # 如果没匹配上了，返回None
