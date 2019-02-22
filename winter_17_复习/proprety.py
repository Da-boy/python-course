#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 0021 下午 9:36
# @Author  : Aries
# @Site    : 
# @File    : proprety.py
# @Software: PyCharm Community Edition

class Circle:
    def __init__(self,r):
        self.r = r

    @property
    def area(self): # 这个方法本身是一个属性，这个属性会随着对象的一些基础数值的变化而变化
        return 3.14*self.r**2

a1 = Circle(5)
print(a1.area)

a2 = Circle(10)
print(a2.area)
