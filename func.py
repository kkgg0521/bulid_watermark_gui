# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/24 11:00
@Auth ： 吕伟康
@File ：func.py
"""
import os


def readallpics(path):
    lis = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] in ['.png', '.jpg', '.PNG', '.JPG']:
            lis.append(path +'/'+ file)
    return lis