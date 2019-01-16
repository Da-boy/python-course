#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 0016 上午 9:45
# @Author  : Aries
# @Site    : 
# @File    : homework.py
# @Software: PyCharm Community Edition

# 过滤掉小于三的字符串列表，并将剩下的转换为大写字母
lst = ['laex', 'ss', 'loei', 'ppps', 'sst']

new_lst = [el.upper() for el in lst if len(el) >= 3]

print(new_lst)

# 求（x,y）其中x是0-5之间的偶数，y是0-5之间的奇数组成的元组列表
lst1 = [(x, y) for x in range(6) if x % 2 == 0 for y in range(6) if y % 2 == 1]
print(lst1)

# 求M中3，6,9组成的列表M=[[1,2,3],[4,5,6],[7,8,9]]
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([i[2] for i in M])

M1 = [3, 6, 9]
print([[x - 2, x - 1, x - 0] for x in M1])

# 求出50以内能被3整除的数的平方，并放入一个列表中
lst2 = [i for i in range(51) if i % 3 == 0 if i != 0]
print(lst2)
