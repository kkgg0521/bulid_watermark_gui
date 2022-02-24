# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/24 11:28
@Auth ： 吕伟康
@File ：BulidWaterMark.py
"""
import os

import cv2
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal
from blind_watermark import WaterMarkCore


class BulidWaterMark:
    def __init__(self, password_wm=1, password_img=1, block_shape=(4, 4), mode='common', processes=None):

        self.bwm_core = WaterMarkCore(password_img=password_img, mode=mode, processes=processes)

        self.password_wm = password_wm

        self.alpha = None  # 用于处理透明图

    def read_img(self, filename):
        # 读入图片
        img = cv2.imread(filename, flags=cv2.IMREAD_UNCHANGED)
        if img is None:
            raise IOError("image file '{filename}' not read".format(filename=filename))

        # 处理透明图
        self.alpha = None
        if img.shape[2] == 4:
            if img[:, :, 3].min() < 255:
                self.alpha = img[:, :, 3]
                img = img[:, :, :3]

        self.bwm_core.read_img_arr(img=img)
        return img

    def read_img_wm(self, filename):
        wm = cv2.imread(filename)
        if wm is None:
            raise IOError("file '{filename}' not read".format(filename=filename))

        # 读入图片格式的水印，并转为一维 bit 格式
        self.wm = wm[:, :, 0]
        # 加密信息只用bit类，抛弃灰度级别
        self.wm_bit = self.wm.flatten() > 128

    def read_wm(self, wm_content, mode='img'):
        if mode == 'img':
            self.read_img_wm(filename=wm_content)
        elif mode == 'str':
            byte = bin(int(wm_content.encode('utf-8').hex(), base=16))[2:]
            self.wm_bit = (np.array(list(byte)) == '1')
        else:
            self.wm_bit = np.array(wm_content)

        self.wm_size = self.wm_bit.size

        # 水印加密:
        np.random.RandomState(self.password_wm).shuffle(self.wm_bit)

        self.bwm_core.read_wm(self.wm_bit)

    def embed(self, filename):
        embed_img = self.bwm_core.embed()
        if self.alpha is not None:
            embed_img = cv2.merge([embed_img.astype(np.uint8), self.alpha])

        cv2.imwrite(filename, embed_img)
        return embed_img

    def extract_decrypt(self, wm_avg):
        wm_index = np.arange(self.wm_size)
        np.random.RandomState(self.password_wm).shuffle(wm_index)
        wm_avg[wm_index] = wm_avg.copy()
        return wm_avg

    def extract(self, filename, wm_shape, out_wm_name=None, mode='img'):
        img = cv2.imread(filename, flags=cv2.IMREAD_COLOR)

        self.wm_size = np.array(wm_shape).prod()

        if mode in ('str', 'bit'):
            wm_avg = self.bwm_core.extract_with_kmeans(img=img, wm_shape=wm_shape)
        else:
            wm_avg = self.bwm_core.extract(img=img, wm_shape=wm_shape)

        # 解密：
        wm = self.extract_decrypt(wm_avg=wm_avg)

        # 转化为指定格式：
        if mode == 'img':
            cv2.imwrite(out_wm_name, 255 * wm.reshape(wm_shape[0], wm_shape[1]))
        elif mode == 'str':
            byte = ''.join((np.round(wm)).astype(np.int).astype(np.str))
            wm = bytes.fromhex(hex(int(byte, base=2))[2:]).decode('utf-8', errors='replace')

        return wm


class Thread(QThread):
    sinOut = pyqtSignal(str, str, str)
    def __init__(self, parent=None):
        super(Thread, self).__init__(parent)
        self.pic_path_list = []
        self.ab_path_list = []
        self.out_dir_path =''
        self.key_one = 1
        self.key_two = 2

    def run(self) -> None:
        for pic_path in self.pic_path_list:
            for abpath in self.ab_path_list:
                bwm1 = BulidWaterMark(password_wm=self.key_one, password_img=self.key_two)
                bwm1.read_img(pic_path)
                bwm1.read_wm(abpath)
                bwm1.embed('{}/{}'.format(self.out_dir_path, os.path.basename(pic_path)))

        self.sinOut.emit('所有图片', '所有水印', '全部结束')