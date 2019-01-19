#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/18 0018 上午 8:49
# @Author  : Aries
# @Site    : 
# @File    : 二分查找.py
# @Software: PyCharm Community Edition

lst = [1, 5, 34, 56, 57, 59, 66, 78, 99]

n = 66

left = 0
right = len(lst) - 1
count = 1
while left <= right:
    middle = (left + right) // 2
    if n > lst[middle]:
        left = middle + 1
    elif n < lst[middle]:
        right = middle - 1
    else:
        print('灿在')
        print(middle)
        print(count)
        break
    count = count + 1
else:
    print('不存在')
