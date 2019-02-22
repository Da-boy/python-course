#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 0021 上午 11:46
# @Author  : Aries
# @Site    : 
# @File    : 内置方法__len__.py
# @Software: PyCharm Community Edition

# __new__ 构造方法
# __init__ 初始化方法

class Single:
    def __new__(cls, *args, **kwargs):  # 开辟空间时，首先执行__new__方法
        print('new方法')
        obj = object.__new__(cls)  # 还没有创建self空间，这里只能把类空间传过来
        print(obj)
        return obj

    def __init__(self):
        print('init方法', self)


ob = Single()


# 1、开辟一个属于对象的空间
# 2、把对象的空间传给self,执行init
# 3、将这个对象的空间返回给调用者

# new方法在什么时候执行？
# 在实例化之后，__init__之前执行new来创建一个空间


# 单例：如果一个类，从头到尾只能有一个实例，说明其只开辟了一个属于对象的空间，那么这个类就叫单例类
# 单例类,单例模式
class Single1:
    __ISINSTANCE = None
    def __new__(cls, *args, **kwargs):
        if not cls.__ISINSTANCE:
            cls.__ISINSTANCE = object.__new__(cls)
        return cls.__ISINSTANCE


    def __init__(self,name,age):
        self.name = name
        self.age = age


s1 = Single1('gaga',12)
s2 = Single1('yyyy',78)
print(s1, s2)
print(s1.name,s2.name)
