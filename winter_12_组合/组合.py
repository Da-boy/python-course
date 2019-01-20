#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/20 0020 下午 7:52
# @Author  : Aries
# @Site    : 
# @File    : 组合.py
# @Software: PyCharm Community Edition

'''
（1）创建一个Game_role的类
（2）构造方法中给对象封装name,ad(攻击力)，hp，三个属性
（3）创建一个attack方法，此方法是实例化两个对象，互相攻击的功能：
    此方法要完成‘谁攻击谁，谁掉了多少血，还剩多少血’
'''


class Game_role:
    def __init__(self, name, ad, hp):
        self.name = name
        self.ad = ad
        self.hp = hp

    def attack(self, p):
        p.hp = int(p.hp) - int(self.ad)
        print('%s attacked %s , %s loss %d blood ,remain %d blood' % (self.name, p.name, p.name, int(self.ad), p.hp))


p1 = Game_role('盖伦', 10, 100)
p2 = Game_role('剑豪', 20, 80)
p1.attack(p2)
print(p2.hp)
