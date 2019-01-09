#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 0007 下午 10:15
# @Author  : Aries
# @Site    : 
# @File    : list.py
# @Software: PyCharm Community Edition
'''

把班级学生数学成绩录入到一个列表中：并求平均值。
 要求：录入的时候要带着人名录入。例如：张三 44

'''

lst = []
while 1:
    stu = input("input student name and grade,input Q esc:")
    if stu.upper() == "Q":
        break
    lst.append(stu)

sum = 0
for el in lst:
    li = el.split(" ")
    sum += int(li[1])
print(sum/len(lst))

