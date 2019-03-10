#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 0018 上午 10:32
# @Author  : Aries
# @Site    : 
# @File    : BMI指数(正式版).py
# @Software: PyCharm Community Edition


class People:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    @property
    def bmi(self):
        return self.weight / (self.height ** 2)


p1 = People('egon', 100, 1.85)
print(p1.bmi)

# 属性：将一个方法，伪装成一个属性，在代码上没有本质的提升，但是让其看起来很合理
