#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 0021 上午 11:46
# @Author  : Aries
# @Site    : 
# @File    : 内置方法__len__.py
# @Software: PyCharm Community Edition

# 内置函数和类的内置方法是有联系的

class mylist:
    def __init__(self):
        self.lst = [1, 2, 4, 6]

    def __len__(self):
        print('this is len')
        return len(self.lst)


l = mylist()
print(len(l))  # len(obj)相当于调用这个obj的__len__方法


# __len__方法return的值就是len函数的返回值
# 如果一个obj对象没有__len__方法，那么len函数会报错

class mystr:
    def __init__(self,str):
        self.str = str

    def __len__(self):
        return len(self.str)

str = mystr('hsdhadha')
print(len(str))