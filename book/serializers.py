#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : p9019 at 2024/3/8
# @File       : serializers.py
# @Project    : DjangoCBV
# Description :
__author__ = 'pangzhaowen'

from rest_framework import serializers
from .models import BookInfo, PublishInfo, AuthorInfo


# 针对模型设计的序列化器
# class BookSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=32)
#     price = serializers.IntegerField()
#     pub_date = serializers.DateField()
#     date = serializers.DateField(source="pub_date") # 指定别名
#     def create(self, validated_data):
#         new_book = BookInfo.objects.create(**self.validated_data)
#         return new_book
#
#
#     def update(self, instance, validated_data):
#         print(456)
#         BookInfo.objects.filter(pk=instance.pk).update(**validated_data)
#         updated_book = BookInfo.objects.get(pk=instance.pk)
#         return updated_book


# 针对模型设计的序列化器
# class BookSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = BookInfo


# 针对模型设计的序列化器
class BaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = ["title", "price", "pub_date", "is_delete", "readcount", "commentcount", "auth", "category"]
        # fields = "__all__"

    def create(self, validated_data):
        """ModelSerializer自己已经有create方法"""
        print(123)
        new_book = BookInfo.objects.create(**self.validated_data)
        return new_book


class BookSerializers(serializers.ModelSerializer):
    """根据当前行政区划查询详情并把子行政区划查询出来"""
    # 这里subs就是原来的area_set,只是因为当前表关联自身，所以为了避免出现无限嵌套，所以修改名字
    date = serializers.DateField(source="pub_date")  # 指定别名
    subs = BaseSerializers(many=True, read_only=True)

    class Meta:
        model = BookInfo
        fields = ["id", "title", "price", "date", "subs"]
        # exclude = ["price"] 排除


class BookUpdateSerializers(serializers.ModelSerializer):
    """根据当前行政区划查询详情并把子行政区划查询出来"""
    # 这里subs就是原来的area_set,只是因为当前表关联自身，所以为了避免出现无限嵌套，所以修改名字
    subs = BaseSerializers(many=True, read_only=True)

    class Meta:
        model = BookInfo
        fields = ["title", "price", "subs"]

    def update(self, instance, validated_data):
        print(456)
        BookInfo.objects.filter(pk=instance.pk).update(**validated_data)
        updated_book = BookInfo.objects.get(pk=instance.pk)
        return updated_book


class BookSerializersModelSerializer(serializers.ModelSerializer):
    """根据当前行政区划查询详情并把子行政区划查询出来"""
    class Meta:
        model = BookInfo
        fields = "__all__"


class PublishSerializersModelSerializer(serializers.ModelSerializer):
    """根据当前行政区划查询详情并把子行政区划查询出来"""
    class Meta:
        model = PublishInfo
        fields = "__all__"


class AuthorSerializersModelSerializer(serializers.ModelSerializer):
    """根据当前行政区划查询详情并把子行政区划查询出来"""
    class Meta:
        model = AuthorInfo
        fields = "__all__"



if __name__ == "__main__":
    pass
