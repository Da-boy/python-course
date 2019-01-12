#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 0012 下午 4:03
# @Author  : Aries
# @Site    : 
# @File    : function3.py
# @Software: PyCharm Community Edition


def gn(id, sex, name, age, hobby):
    print('id:%s , sex:%s , name:%s, hobby:%s, age:%s' % (id, sex, name, hobby, age))


gn(1, 'boy', 'libai', 19, 'football')

gn(id=2, sex='girl', name='wang', age=10, hobby='ball')

gn(3, 'girl', age=18, name='wangyang', hobby='tt')
