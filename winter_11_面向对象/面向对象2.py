#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/20 0020 上午 10:53
# @Author  : Aries
# @Site    : 
# @File    : 面向对象2.py
# @Software: PyCharm Community Edition


class Person:
    animal = '高级动物'
    soul = '灵魂'
    language = '语言'

    def __init__(self, country, name, sex, age, high):
        self.country = country
        self.name = name
        self.sex = sex
        self.age = age
        self.high = high

    def eat(self):
        print('%s is eating' % self.name)

    def sleep(self):
        print('%s is sleep' % self.name)

    def work(self):
        pass


p1 = Person('中国', 'alex', '未知', 42, 175)
p2 = Person('美国', '大朗', 'boy', 32, 185)
p3 = Person('泰国', 'liu', 'girl', 22, 165)
p4 = Person(p1.country, p2.name, p3.sex, p2.age, p1.high)

p1.eat()
p2.eat()
p3.sleep()
p4.sleep()
print(p1.animal)
print(p2.soul)
print(p4.language)