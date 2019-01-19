#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 0019 上午 10:01
# @Author  : Aries
# @Site    : 
# @File    : 元组.py
# @Software: PyCharm Community Edition

# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
tup1 = (50)
print(type(tup1))

tup2 = (50,)
print(type(tup2))


# 元组可以使用下标索引来访问元组中的值

tup3 = ('Google', 'Runoob', 1997, 2000)

print("tup1[0]: ", tup3[0])
print("tup2[1:3]: ", tup3[1:3])

