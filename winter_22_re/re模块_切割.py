#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 0009 下午 2:47
# @Author  : Aries
# @Site    : 
# @File    : re模块_替换.py
# @Software: PyCharm Community Edition

import re

str = 'dsadasdlk12asjdhahsd123asdkl9'
ret = re.split('\d+',str)
print(ret)
