#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 0022 下午 9:10
# @Author  : Aries
# @Site    : 
# @File    : 析构方法.py
# @Software: PyCharm Community Edition


class Foo:
    # 垃圾回收机制
    def __del__(self):
        # 析构方法 del Foo的对象，会自动触发这个方法
        # 去释放一些在创建对象的时候借用的资源，例 关闭文件
        print('执行我啦')
        # self.f.close() 关闭文件


f1 = Foo()
# del f1
print('------->')
# 某对象借用了系统资源（文件资源、网络资源），要通过析构方法归还回去

with open: # 没有f=open,f.close可靠
    pass

#with的机制








