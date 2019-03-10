#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 0023 下午 8:36
# @Author  : Aries
# @Site    : 
# @File    : my_module.py
# @Software: PyCharm Community Edition

if __name__ == '__main__':

    print('我是模块二')
    name = '模块名'
    def login():
        print('模块2登陆啦 %s' % name)

    print(__name__)

import sys
print(__name__)
print('***',sys.modules['__main__'])

my_module = sys.modules[__name__]
getattr(my_module,'login')()
# 使用反射自己模块中的内容时，使用sys.module[__name__]
# getattr(sys.module[__name__],'变量名')

# 在编写py文件时，所有不在函数和类中封装的内容都应该写在if __name__ == '__main__':

