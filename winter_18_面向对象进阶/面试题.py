#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 0023 下午 3:52
# @Author  : Aries
# @Site    : 
# @File    : 面试题.py
# @Software: PyCharm Community Edition

# 题目：员工管理系统  姓名 性别 年龄 部门
# 1000名员工如果几个员工的姓名和性别相同，这是一个人
class Employee:
    def __init__(self, name, age, sex, dep):
        self.name = name
        self.age = age
        self.sex = sex
        self.dep = dep

    def __hash__(self):
        return hash('%s %s' % (self.name, self.sex))

    def __eq__(self, other):
        if self.name == other.name and self.sex == other.sex:
            return True


employ_lst = []
for i in range(200):
    employ_lst.append(Employee('jia', i, 'male', 'python'))
for i in range(200):
    employ_lst.append(Employee('wang', i, 'female', 'python'))
for i in range(200):
    employ_lst.append(Employee('li', i, 'male', 'python'))
for i in range(200):
    employ_lst.append(Employee('wu', i, 'female', 'python'))
for i in range(200):
    employ_lst.append(Employee('haha', i, 'male', 'python'))

se = set(employ_lst)
for person in se:
    print(person.__dict__)

