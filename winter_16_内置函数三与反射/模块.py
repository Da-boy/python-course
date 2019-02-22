#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 0020 下午 4:52
# @Author  : Aries
# @Site    : 
# @File    : 模块.py
# @Software: PyCharm Community Edition


#模块

import os
# os.rename('init.py','__init__.py') # 修改外部文件名称

# getattr(os,'rename')('__init__.py','init.py')

# rename = os.rename
# rename('init.py','__init__.py')

# rename2 = getattr(os,'rename')
# rename2('__init__.py','init.py')


# import 相当于导入一个模块

import sys # 这个模块里的所有方法都是和python解释器相关的

# sys.modules 这个方法，表示所有在当前这个python程序中导入的模块
# print(sys.modules)
print(sys.modules['__main__'])

def func1():
    print(111)

def func2():
    print(222)

my_file = sys.modules['__main__']
getattr(my_file,'func1')()
getattr(my_file,'func2')()