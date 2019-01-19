#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 0010 上午 9:19
# @Author  : Aries
# @Site    : 
# @File    : 浅拷贝.py
# @Software: PyCharm Community Edition

lst1 = ['wang', 'tuo', 'rong', ['da', 'qiang', 'ge']]
lst2 = lst1.copy() # 浅拷贝

lst1[3].append('ddd')

print(lst2,lst1)

import copy
lst3 = copy.deepcopy(lst1) # 深拷贝
lst1[3].append('hehe')
print(lst1,lst3)




