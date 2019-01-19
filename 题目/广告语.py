#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 0019 上午 9:08
# @Author  : Aries
# @Site    : 
# @File    : 广告语.py
# @Software: PyCharm Community Edition

ad = input('请输入你的广告语：')
if '最' in ad or '国家级' in ad or '第一' in ad or '稀缺' in ad:
    print('不合法')
else:
    print('合法')
