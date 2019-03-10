#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 0025 下午 8:59
# @Author  : Aries
# @Site    : 
# @File    : student.py
# @Software: PyCharm Community Edition


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