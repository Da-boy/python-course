#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/24 0024 上午 9:36
# @Author  : Aries
# @Site    : 
# @File    : from..,import.py
# @Software: PyCharm Community Edition


from my_module import login

# 仍然相当于执行了整个py文件
# 导入什么就能使用什么，不导入的变量不能使用
# 不导入并不意味着不存，而是没有建立文件到模块中的其他名字的引用

# 1、找到my_module模块
# 2、开辟一块属于这个模块的命名空间
# 3、执行这个模块

login()
# 知道了要import的是login这个名字，那么就会在本文件中创建一个变量login指向模块命名空间中的login函数

# 当模块中导入的方法或者变量和本文件重名的时候，那么这个名字只代表最后一次对它赋值的那个方法或者变量

# 在本文件中的全局变量的修改是不会影响到模块中的变量引用的


# 重命名
from my_module import login as lg

lg()


#导入多个
from my_module import login,name


#导入多个并重命名
from my_module import login as lg,name as nm


#from 模块 import *


#__all__ = [] 可以控制*的导入内容 放在模块中

