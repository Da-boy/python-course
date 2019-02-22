# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 0019 上午 10:39
# @Author  : Aries
# @Site    : 
# @File    : 反射.py
# @Software: PyCharm Community Edition

# eval 不能用

class Student:
    role = 'students'

    @classmethod
    def check_course(cls):
        print('已查看课程')

    @staticmethod
    def login():
        print('登录系统')


# 反射查看属性
print(Student.role)
print(getattr(Student, 'role'))

# 反射调用方法
print(getattr(Student, 'check_course'))
getattr(Student, 'check_course')()

# 反射调用静态方法

print(getattr(Student, 'login'))
getattr(Student, 'login')()

num = input('>>>')
if hasattr(Student, num):  # hasattr查看你输入的字符串是否能在命名空间能找到,找到返回True,找不到返回False
    getattr(Student, num)()
