#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 0015 上午 10:35
# @Author  : Aries
# @Site    : 
# @File    : 推倒是.py
# @Software: PyCharm Community Edition

# 语法[最终结果（变量） for 变量 in 可迭代对象 if条件]

# 寻找带有两个e的人名

names = [['tom', 'sever', 'tui', 'jiaaeee', 'wangee'], ['tianeyre', 'laopao', 'llerte', 'hehe', 'ok']]

lst = [name for first in names for name in first if name.count('e') == 2]
print(lst)
