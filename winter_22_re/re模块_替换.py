#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 0009 下午 2:47
# @Author  : Aries
# @Site    : 
# @File    : re模块_替换.py
# @Software: PyCharm Community Edition

import re

str = 'dsadasdlk12asjdhahsd123asdkl'
ret = re.sub('\d+', 'KK', str)
print(ret)

ret2 = re.subn('\d+','OO',str)
print(ret2)
