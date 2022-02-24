# -*- coding: utf-8 -*-
"""
@Time ： 2021/9/7 13:55
@Auth ： 吕伟康
@File ：ReadQss.py
"""


class ReadQss:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()

    @staticmethod
    def notepadqss():
        return ReadQss.readQss('./static/notepad.qss')
