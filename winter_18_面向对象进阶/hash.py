#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 0023 下午 1:30
# @Author  : Aries
# @Site    : 
# @File    : hash.py
# @Software: PyCharm Community Edition


# 底层数据结构基于hash值寻址优化操作
# hash算法:把某个要存在内存里的值通过一系列计算，保证不同值的hash结果不一样
# 对同一个值 在多次执行python代码的时候hash值不同
# 对同一个值 在同一次执行python代码的时候hash值永远不变
print(hash('asa'))
print(hash('asa'))
print(hash('asa'))
print(hash('asa'))
# 字典寻址（比列表寻址快）
# set集合,去重(hash值去重)
se = {1, 2, 3, 4, 4, 'asd', 'ad'}
print(se)
# hash(obj) obj内部必须实现了__hash__方法
