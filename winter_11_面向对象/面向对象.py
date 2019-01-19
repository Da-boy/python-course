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

    def work(self):
        print('人类会工作')

    def shop(self):
        print('people can shop')


'''
类名的角度：
	类中的静态变量获取方法：
	1、Person.__dict__ 查询类中的所有内容(不能进行增删改操作)
        print (Person.__dict__)
        print (Person.__dict__[faith])
	2、万能的“.”
        print(Person.mind)
        Person.money = 'dollar' 增
        print(Person.money)
        Person.mind = 'unmind' 改
        print(Person.__dict__)
        del Person.animal
        print(Person.__dict__)
		
'''
print(Person.mind)
Person.money = 'dollar'
print(Person.money)

Person.mind = 'unmind'
print(Person.__dict__)

del Person.animal
print(Person.__dict__)