#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 0019 上午 11:22
# @Author  : Aries
# @Site    : 
# @File    : 面向对象.py
# @Software: PyCharm Community Edition


class Person:
    '''
    类体分为两部分：变量部分，方法（函数）部分
    '''

    mind = '有思想'
    animal = '高级动物'
    faith = '信仰'

    def __init__(self, name, age, hobby):  # 约定俗成self
        print(self)
        self.name = name  # 封装属性
        self.age = age  # 封装属性
        self.hobby = hobby  # 封装属性

    def work(self):
        print('人类会工作')

    def shop(self):
        print('people can shop')


# 对象的角度
# Person()  # 类名+（）的过程：实例化过程（创建一个对象的过程）
# Person() ：实例化对象、实例、对象
# 1、只要类名+（）产生一个对象(对象空间)
# 2、自动执行类中的__init__方法
# 3、将对象空间传给__init__的self参数
# 4、给对象封装相应的属性

ret = Person('jia', 19, 'football')
print(ret)
print(ret.__dict__)
#操作对象中的静态变量
#  1、__dict__查询对象中的所有内容
#  2、万能的 .
print(ret.name)
ret.high = 175
print(ret.__dict__)
