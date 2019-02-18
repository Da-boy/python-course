#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 0017 上午 11:44
# @Author  : Aries
# @Site    : 
# @File    : 归一化设计.py
# @Software: PyCharm Community Edition


class Alipay:
    def __init__(self, money):
        self.money = money

    def pay(self):
        print('阿里支付%s' % self.money)


class Jdpay:
    def __init__(self, money):
        self.money = money

    def pay(self):
        print('京东支付%s' % self.money)


def pay(obj):
    obj.pay()


a1 = Alipay(200)
j1 = Jdpay(100)
a1.pay()
j1.pay()

pay(a1)  # 归一化设计
pay(j1)
