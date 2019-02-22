#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 0020 下午 3:25
# @Author  : Aries
# @Site    : 
# @File    : 反射应用.py
# @Software: PyCharm Community Edition


# 判断身份，并且根据身份实例化。根据每个身份对应的类，让用户选择能够做的事情
class Student:
    OPERATE_DIC = [
        ('查看所有课程', 'check_course'),
        ('查看个人信息', 'check_student_info'),
    ]

    def __init__(self, name):
        self.name = name

    def check_course(self):
        print('查看所有课程')

    def check_student_info(self):
        print('查看个人信息')


class Manager:
    OPERATE_DIC = [
        ('创建学生账号', 'create_student'),
        ('创建课程', 'create_course'),
        ('查看学生信息', 'check_student_info'),
    ]

    def __init__(self, name):
        self.name = name

    def create_student(self):
        print('创建学生账号')

    def create_course(self):
        print('创建课程')

    def check_student_info(self):
        print('查看学生信息')


class Teacher:
    OPERATE_DIC = [
        ('查看课程', 'see_course'),
        ('查看学生信息', 'check_student_info'),
    ]

    def __init__(self, name):
        self.name = name

    def see_course(self):
        print('查看课程')

    def check_student_info(self):
        print('查看学生信息')


def login():
    username = input('user:')
    password = input('passwork:')
    with open('user') as f:
        for line in f:
            user, pwd, role = line.strip().split('|')
            if user == username and pwd == password:
                print('%s %s 登陆成功' % (username, role))
                return username, role


import sys


def main():
    user, role = login()
    file = sys.modules['__main__']
    cls = getattr(file, role)  # getattr(当前文件，'Manager')
    obj = cls(user)
    operate_dic = cls.OPERATE_DIC
    # print(operate_dic)
    while True:
        for num,i in enumerate(operate_dic,1):
            print(num,i[0])
        choice = int(input('num:'))
        choice_item = operate_dic[choice-1]
        getattr(obj,choice_item[1])()

main()
