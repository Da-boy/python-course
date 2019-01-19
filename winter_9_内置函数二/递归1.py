#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 0017 下午 6:40
# @Author  : Aries
# @Site    : 
# @File    : 递归.py
# @Software: PyCharm Community Edition

# 递归遍历树形结构

import os

filePath = 'F:\python课程\python-course'


def read(filePath, n):
    it = os.listdir(filePath) # 查看文件夹中的文件，这是一个可迭代对象
    for el in it:
        fp = os.path.join(filePath, el) # 拿到路径
        if os.path.isdir(fp): #判断文件是文件夹还是文件
            print("\t" * n, el)
            read(fp, n + 1)
        else:# 不是文件夹
            print("\t" * n, el) #递归出口


read(filePath, 0)
