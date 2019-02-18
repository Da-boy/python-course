#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 0017 上午 11:44
# @Author  : Aries
# @Site    : 
# @File    : 归一化设计.py
# @Software: PyCharm Community Edition


from abc import ABCMeta, abstractmethod

 # 强制制定一个规范，凡是继承我的类中必须有pay方法，如果没有，实例化对象的时候就会报错
class Payment(metaclass=ABCMeta):# 抽象类（接口类）
    @abstractmethod
    def pay(self): #制定了一个规范
        pass


class Alipay(Payment):
    def __init__(self, money):
        self.money = money

    def pay(self):
        print('阿里支付%s' % self.money)


class Jdpay(Payment):
    def __init__(self, money):
        self.money = money

    def pay(self):
        print('京东支付%s' % self.money)


class Wechatpay(Payment):
    def __init__(self, money):
        self.money = money

    def pay(self):
        print('微信支付%s' % self.money)


def pay(obj):
    obj.pay()


a1 = Alipay(200)
j1 = Jdpay(100)
w1 = Wechatpay(500)

pay(a1)  # 归一化设计
pay(j1)
pay(w1)
