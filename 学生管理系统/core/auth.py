#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 0025 下午 8:59
# @Author  : Aries
# @Site    : 
# @File    : auth.py
# @Software: PyCharm Community Edition


def login():
    username = input('user:')
    password = input('passwork:')
    with open('user') as f:
        for line in f:
            user, pwd, role = line.strip().split('|')
            if user == username and pwd == password:
                print('%s %s 登陆成功' % (username, role))
                return username, role

if __name__ == '__main__':
    login()
