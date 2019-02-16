#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/20 0020 下午 7:52
# @Author  : Aries
# @Site    : 
# @File    : 组合.py
# @Software: PyCharm Community Edition

# 版本二


class Game_role:
    def __init__(self, name, ad, hp):
        self.name = name
        self.ad = ad
        self.hp = hp

    def attack(self, p):
        p.hp = int(p.hp) - int(self.ad)
        print('%s attacked %s , %s loss %d blood ,remain %d blood' % (self.name, p.name, p.name, int(self.ad), p.hp))

    def equipment_weapon(self, wea):
        self.wea = wea


# 添加武器类
class Weapon:
    def __init__(self, name, ad):
        self.name = name
        self.ad = ad

    def fight(self, p1, p2):
        p2.hp = p2.hp - self.ad
        print('%s attacked %s , %s loss %s blood ,remain %s blood' % (p1.name, self.name, p2.name, self.ad, p2.hp))


p1 = Game_role('盖伦', 10, 100)
p2 = Game_role('剑豪', 20, 80)

axe = Weapon('斧头', 50)
bigsword = Weapon('宝剑', 40)

p1.equipment_weapon(axe)

print(axe)
print(p1.wea)