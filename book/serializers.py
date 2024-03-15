#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2024/3/10 23:40
# @Author  : pangcw
# @File    : serializers.py
# @Software: PyCharm

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : p9019 at 2024/3/8
# @File       : serializers.py
# @Project    : DjangoCBV
# Description :
__author__ = 'pangzhaowen'

from rest_framework import serializers
from .models import BookInfo


# 针对模型设计的序列化器
class BookSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=32)
    price = serializers.IntegerField()
    pub_date = serializers.DateField()


# BookSerializers(instance,data)

if __name__ == '__main__':
    print('Python')
