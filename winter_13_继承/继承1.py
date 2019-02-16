#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 0013 下午 7:42
# @Author  : Aries
# @Site    : 
# @File    : 继承.py
# @Software: PyCharm Community Edition

class Animal:
    def eat(self):
        print('eat')

    def drink(self):
        print('drink')

    def pull(self):
        print('pull')


class Dog(Animal):
    def run(self):
        print('run')

Dog.pull(0)