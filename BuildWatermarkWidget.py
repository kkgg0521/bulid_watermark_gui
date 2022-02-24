# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/24 9:42
@Auth ： 吕伟康
@File ：BuildWatermarkWidget.py
"""
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QFileDialog

from func import readallpics
from ui.build_watermark_ui import Ui_build_watermark

# import blind_watermark
class BuildWatermarkWidget(QWidget, Ui_build_watermark):
    def __init__(self,parent = None):
        super(BuildWatermarkWidget, self).__init__(parent)
        self.setupUi(self)
        choose_dir_icon = QIcon('static/icon/choosedir.png')
        self.toolButton_oripath.setIcon(choose_dir_icon)
        self.toolButton_sypath.setIcon(choose_dir_icon)
        self.toolButton_outpath.setIcon(choose_dir_icon)
        start_icon = QIcon('static/icon/start.png')
        self.pushButton_start.setIcon(start_icon)
        stop_icon = QIcon('static/icon/stop.png')
        self.pushButton_stop.setIcon(stop_icon)


        self.toolButton_oripath.clicked.connect(self.choose_oris_path)
        self.toolButton_sypath.clicked.connect(self.choose_sys_path)
        self.toolButton_outpath.clicked.connect(self.choose_out_path)
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



