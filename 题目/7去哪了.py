#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/18 0018 下午 7:58
# @Author  : Aries
# @Site    : 
# @File    : 7去哪了.py
# @Software: PyCharm Community Edition

# 使用while循环输出1 2 3 4 5 6 8 9 10
# 方法1
for i in range(1, 11):
    if i == 7:
        continue
    print(i, end=' ')
print()
# 方法2
count = 1
while count <= 10:
    if count == 7:
        count = count + 1
        continue
    print(count, end=' ')
    count += 1
