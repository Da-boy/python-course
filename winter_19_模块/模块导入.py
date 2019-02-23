#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 0023 下午 8:35
# @Author  : Aries
# @Site    : 
# @File    : 模块导入.py
# @Software: PyCharm Community Edition


import my_module


# 导入文件不加后缀名
# 模块的名字必须满足命名规范，一般都是小写字母开头
# import 模块 相当于执行这个模块的py文件
# 一个模块不会重复导入


# 如何使用模块？

def login():
    print('文件中的登录')


login()
my_module.login()

name = 'haha'

print(name)
