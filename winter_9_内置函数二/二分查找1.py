#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/18 0018 上午 8:49
# @Author  : Aries
# @Site    : 
# @File    : 二分查找.py
# @Software: PyCharm Community Edition

lst = [1, 5, 34, 56, 57, 59, 66, 78, 99]

def bin_seach(left,right,n):
    if left<=right:
        middle = (left+right)//2
        if n>lst[middle]:
            left = middle+1
        elif n<lst[middle]:
            right = middle-1
        else:
            return middle
        return bin_seach(left,right,n)
    else:
        return -1
print(bin_seach(0,len(lst)-1,77))
