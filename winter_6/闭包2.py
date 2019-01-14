#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 0014 下午 3:52
# @Author  : Aries
# @Site    : 
# @File    : 闭包1.py
# @Software: PyCharm Community Edition


from urllib.request import urlopen


def but():
    content = urlopen("http://yjs.cueb.edu.cn/").read()

    def inner():
        return content

    print(inner.__closure__)  # 检测是否为闭包
    return inner


fn = but()

content1 = fn()
print(content1)

content2 = fn()

print(content2)
