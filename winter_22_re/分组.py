#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 0009 下午 4:11
# @Author  : Aries
# @Site    : 
# @File    : 分组.py
# @Software: PyCharm Community Edition


import re

str = 'dsadasdlk-12asjdhahsd123asdk-l'

# findall
ret = re.findall('www.(baidu|lonan).com','www.lonan.com')
print(ret)
# 取消分组优先 只会在findall中发生

ret1 = re.findall('www.(?:baidu|lonan).com','www.lonan.com')
print(ret1)


# split

ret2 = re.split('\d+',str)
print(ret2)
ret3 = re.split('(\d+)',str)
print(ret3)

# search遇见分组

ret4 = re.search('\d+(.\d+)(.\d+)(.\d+)','1.2.3.4')
print(ret4.group(1))
for i in [0,1,2,3]:
    print(ret4.group(i))
