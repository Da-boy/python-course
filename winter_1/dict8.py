#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 0008 上午 11:07
# @Author  : Aries
# @Site    : 
# @File    : dict3.py
# @Software: PyCharm Community Edition

dic = {
    'key1': '1g',
    'key2': 2,
    'key3': {
        "name": "hello",
        "age": 18
    },
    'key4': '4',
    'key5': [
        {
            'name':'first',
            'age': 18
         },
        {
            'name':'two',
            'age': 10
         }
    ]
}
print(dic.get('key3').get('name'))
print(dic['key5'][1]['age'])