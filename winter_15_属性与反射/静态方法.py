#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 0018 下午 3:24
# @Author  : Aries
# @Site    : 
# @File    : 静态方法.py
# @Software: PyCharm Community Edition

# 静态方法
class A:
    @staticmethod  # 开发中要把方法放到类中
    def login(username, password):
        if username == 'jia' and password == '666':
            print(777)
        else:
            print('失败')


A.login('jia', 'jjj')
