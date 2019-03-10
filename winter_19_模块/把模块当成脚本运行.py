#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/24 0024 上午 10:47
# @Author  : Aries
# @Site    : 
# @File    : 把模块当成脚本运行.py
# @Software: PyCharm Community Edition


# 运行一个py文件的两种方式
# 1、以模块的形式运行
import my_module2
# if __name__ == '__main__':
#     my_module2.login()


import sys

# print(sys.modules)

# '__main__':当前直接执行文件所在的地址
# sys.modules 中存储了所有导入的文件的名字和这个文件的内存地址
# 2、直接运行----以脚本的形式运行
# 那么需要在本文件中直接打印代码上加入if __name__ == '__main__':


