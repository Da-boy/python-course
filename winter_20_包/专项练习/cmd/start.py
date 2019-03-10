#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 0025 下午 4:12
# @Author  : Aries
# @Site    : 
# @File    : start.py
# @Software: PyCharm Community Edition


import sys
print(__file__)
ret = __file__.split('/')
print(ret)
base_path = '/'.join(ret[:-2])
print(base_path)
sys.path.append(base_path)
print(sys.path)
from api import policy
policy.get()
from db import models
models.register_models(123)
