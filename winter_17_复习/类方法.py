#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 0022 上午 10:26
# @Author  : Aries
# @Site    : 
# @File    : 类方法.py
# @Software: PyCharm Community Edition

# 商品程序，价格+折扣
class Goods:
    __discount = 0.8  # 设定当前折扣为8折

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price * self.__discount # 以类的折扣为基准

    @classmethod
    def chang_discount(cls, discount):
        cls.__discount = discount # 只用class中的资源

Goods.chang_discount(1)
apple = Goods(10)
print(apple.price)
Goods.chang_discount(0.9)
print(apple.price)