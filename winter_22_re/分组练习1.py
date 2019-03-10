#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 0009 下午 4:35
# @Author  : Aries
# @Site    : 
# @File    : 分组练习.py
# @Software: PyCharm Community Edition


import re


ret1 = re.search(r'<(?P<tag_name>\w+)>\w+</(?P=tag_name)>', r'<a>helloworld</a>')
print(ret1)
print(ret1.group('tag_name'))


ret2 = re.search(r'<(\w+)>\w+</\1>', r'<a>helloworld</a>')

print(ret2.group())

ret3 = re.search(r'<(?P<tag_name>\w+)>(?P<content>\w+)</(?P=tag_name)>', r'<a>helloworld</a>')
print(ret3.group('content'))