#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 0022 下午 7:00
# @Author  : Aries
# @Site    : 
# @File    : __repr__.py
# @Software: PyCharm Community Edition

# __repr__:repr(obj),%r
# __repr__是__str__的备胎，如果有__str__方法，那么print %s str 都优先执行__str__方法，并且使用__str__的返回值
# 如果没有__str__，那么print %s str 执行__repr__。repr（），%r
# __repr__是比__str__更好的解决方案
class A:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '**%s**' % self.name

    def __repr__(self):
        return self.name


class B(A):
    # def __str__(self):
    #     return '//**%s**//' % self.name

    def __repr__(self):
        return '***'


a = B('all')
print(a)
print(str(a), repr(a))
print('%s | %r' % (a, a))

# 在子类中使用__str__,先找子类的__str__，没有的话向上找，只要父类不是object就执行父类的__str__
# 如果出了父类之外都没有__str__方法，就执行子类的__repr__方法，如果子类没有__repr__方法，就向上找父类的__repr__方法
# 如果一直找不到就执行object类中的__str__方法















