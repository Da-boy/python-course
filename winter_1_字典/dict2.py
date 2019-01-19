#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 0008 上午 11:04
# @Author  : Aries
# @Site    : 
# @File    : dict2.py
# @Software: PyCharm Community Edition

# 增加
dic = {'百度': '李彦宏'}
dic.setdefault('李嘉诚', 'hh') # 默认值设置后不会被其他默认值替代,dict.setdefault(key, default=None)
dic.setdefault('李嘉诚', '房地产')
dic.get('王美丽','heu')
print(dic)
