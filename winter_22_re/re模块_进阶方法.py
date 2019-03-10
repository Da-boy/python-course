#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 0009 下午 2:47
# @Author  : Aries
# @Site    : 
# @File    : re模块_替换.py
# @Software: PyCharm Community Edition

import re

str = 'dsadasdlk-12asjdhahsd123asdk-l'
res = re.compile('-0\.\d+|-[1-9]+(\.\d+)?') # 正则表达式预处理，节省时间
ret = res.search(str)
print(ret)
if ret:
    print(ret.group())


# finditer
ret2 = re.finditer('\d+',str)
print(ret2)
for r in ret2:
    print(r.group())