#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 0025 下午 8:59
# @Author  : Aries
# @Site    : 
# @File    : main.py
# @Software: PyCharm Community Edition

import sys
from core import auth
from core import manager
from core import student
def entry_point():
    print('欢迎登录学生选课系统')
    print('请输入你的账号和密码')
    user,role = auth.login()
    file = sys.modules['__main__']
    print(file)
    print(__file__)
    cls = getattr(__file__, role)  # getattr(当前文件，'Manager')
    obj = cls(user)
    operate_dic = cls.OPERATE_DIC
    # print(operate_dic)
    while True:
        for num, i in enumerate(operate_dic, 1):
            print(num, i[0])
        choice = int(input('num:'))
        choice_item = operate_dic[choice - 1]
        getattr(obj, choice_item[1])()


if __name__ == '__main__':
    entry_point()
