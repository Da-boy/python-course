#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 0013 下午 7:42
# @Author  : Aries
# @Site    : 
# @File    : 继承.py
# @Software: PyCharm Community Edition


class Animal:
    breath = 'wang'

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def eat(self):
        print('999')
        return '666'


class Person(Animal):  # 括号里的为父类，基类 括号外的叫子类
    pass


p1 = Person('jia', 'lady', 10)
print(p1.__dict__)

print(Person.breath)
print(Person.eat(0))

p1.eat()
# 继承： 子类以及子类实例化的对象 可以访问父类的任何方法或变量
# 类名可以访问父类所有内容
# 子类实例化的对象可以访问父类所有内容
