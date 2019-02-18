#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 0018 上午 10:10
# @Author  : Aries
# @Site    : 
# @File    : BMI指数.py
# @Software: PyCharm Community Edition


class BMI:
    def __init__(self, weight, hight):
        self.weight = weight
        self.hight = hight

    def sum(self):# 工作中不要打印
        x = self.weight / (self.hight * self.hight)
        if x <= 18.5:
            print('%s太轻了' % x)
        elif x > 18.5 and x <= 23.9:
            print('%s正常' % x)
        elif x > 23.9 and x <= 27:
            print('%s过重' % x)
        elif x > 28 and x <= 32:
            print('%s肥胖' % x)
        elif x > 32:
            print('%s过度疯胖' % x)
        else:
            print('%s不正常' % x)

a1 = BMI(60,1.6)
a1.sum()