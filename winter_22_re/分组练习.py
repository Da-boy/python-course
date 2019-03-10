#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 0009 下午 4:35
# @Author  : Aries
# @Site    : 
# @File    : 分组练习.py
# @Software: PyCharm Community Edition


import re

ret = re.findall(r'\d+(?:\.\d+)|(\d+)', '1-2*(60+(-40.35/5)-(-4*3))')
# (?:) | ()优先显示（）中内容,?:取消分组优先

print(ret)
ret.remove('')
print(ret)

ret1 = re.search(r'<(\w+)>(\w+)</(\w+)>', r'<a>helloworld</a>')
print(ret1)
print(ret1.group())
print(ret1.group(1))
print(ret1.group(2))
print(ret1.group(3))
