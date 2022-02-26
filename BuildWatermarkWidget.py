# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/24 9:42
@Auth ： 吕伟康
@File ：BuildWatermarkWidget.py
"""
import os

from PyQt5.QtCore import QSize, pyqtSignal, QThread
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QFileDialog
from blind_watermark.recover import recover_crop2, recover_crop1

from BulidWaterMark import Thread, BulidWaterMark
from func import readallpics
from ui.build_watermark_ui import Ui_build_watermark


class BuildWatermarkWidget(QWidget, Ui_build_watermark):
    def __init__(self,parent = None):
        super(BuildWatermarkWidget, self).__init__(parent)
        self.setupUi(self)
        choose_dir_icon = QIcon('static/icon/choosedir.png')
        self.toolButton_oripath.setIcon(choose_dir_icon)
        self.toolButton_sypath.setIcon(choose_dir_icon)
        self.toolButton_outpath.setIcon(choose_dir_icon)
        self.toolButton_rec.setIcon(choose_dir_icon)
        self.toolButton_rec_2.setIcon(choose_dir_icon)

        self.toolButton_tq.setIcon(choose_dir_icon)
        start_icon = QIcon('static/icon/start.png')
        self.pushButton_start.setIcon(start_icon)
        self.pushButton_rec.setIcon(start_icon)
        stop_icon = QIcon('static/icon/stop.png')
        self.pushButton_stop.setIcon(stop_icon)


        self.toolButton_oripath.clicked.connect(self.choose_oris_path)
        self.toolButton_sypath.clicked.connect(self.choose_sys_path)
        self.toolButton_outpath.clicked.connect(self.choose_out_path)
        self.toolButton_tq.clicked.connect(self.choose_out_pic)

        self.toolButton_rec.clicked.connect(self.choose_rec_ori)
        self.toolButton_rec_2.clicked.connect(self.choose_rec_ori_2)
        self.pushButton_rec.clicked.connect(self.rec)


        self.Thread = Thread(self)
        self.Thread.sinOut.connect(self.showinfo)
        self.pushButton_start.clicked.connect(self.start_bulid)
        self.pushButton_stop.clicked.connect(self.stop_bulid)
        self.allpics = None
        self.allsys = None

    def choose_rec_ori(self):
        path = QFileDialog.getOpenFileName(self, "选择图片文件", '*')[0]
        if path != '':
            self.lineEdit_rec.setText(path)

    def choose_rec_ori_2(self):
        path = QFileDialog.getOpenFileName(self, "选择图片文件", '*')[0]
        if path != '':
            self.lineEdit_rec_2.setText(path)

    def rec(self):
        if self.checkBox_rec.isChecked():
            recover_crop2(self.lineEdit_rec.text(),self.lineEdit_rec_2.text(), 'outpic.png')
        else:
            recover_crop1(self.lineEdit_rec.text(),self.lineEdit_rec_2.text(), 'outpic.png')




    def showinfo(self, process , info):
        self.textBrowser.append(info)

    def choose_out_pic(self):
        path = QFileDialog.getOpenFileName(self, "选择图片文件", '*')[0]
        if path != '':
            self.lineEdit_tq.setText(path)
            bwm1 = BulidWaterMark(password_wm=self.spinBox_password1_2.value(), password_img=self.spinBox_password2_2.value())
            bwm1.extract(path, (self.spinBox_shapew.value(),self.spinBox_shapeh.value()), './out.png')
            self.label_outwm.setPixmap(QPixmap('./out.png'))


    def stop_bulid(self):
        self.Thread.stop = True
    def start_bulid(self):
        if self.allsys is not None and self.allpics is not None:
            self.Thread.pic_path_list = self.allpics
            self.Thread.ab_path_list = self.allsys
            self.Thread.out_dir_path = self.lineEdit_outpath.text()
            self.Thread.key_one = self.spinBox_password1.value()
            self.Thread.key_two = self.spinBox_password2.value()
            self.Thread.stop = False
            self.Thread.start()

    def choose_oris_path(self):
        path = QFileDialog.getExistingDirectory(self, "选择需要打标的图片所在文件夹！", "./")
        if not path == '':
            self.lineEdit_oripath.setText(path)
            self.allpics = readallpics(path)
            self.lineEdit_oris.setText(str(len(self.allpics)))

    def choose_sys_path(self):
        path = QFileDialog.getExistingDirectory(self, "选择需要水印所在文件夹！", "./")
        if not path == '':
            self.lineEdit_sypath.setText(path)
            self.allsys = readallpics(path)
            self.lineEdit_sys.setText(str(len(self.allsys)))

    def choose_out_path(self):
        path = QFileDialog.getExistingDirectory(self, "选择出图文件夹！", "./")
        if not path == '':
            self.lineEdit_outpath.setText(path)


