#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/18 0018 下午 7:45
# @Author  : Aries
# @Site    : 
# @File    : 猜数字.py
# @Software: PyCharm Community Edition
n = 66
count = 1
while count <= 3:
    num = int(input('猜一个数字：'))
    if num > n:
        print('太大了')

    elif num < n:
        print('太小了')

    else:
        print('猜对了')
        break
    print('你已经猜了%d次了' % count)
    count = count + 1
else:
    print('太笨了')
