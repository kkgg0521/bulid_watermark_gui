# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'build_watermark.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_build_watermark(object):
    def setupUi(self, build_watermark):
        build_watermark.setObjectName("build_watermark")
        build_watermark.resize(732, 519)
        self.verticalLayout = QtWidgets.QVBoxLayout(build_watermark)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(build_watermark)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(build_watermark)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.spinBox_password1 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_password1.setMinimum(1)
        self.spinBox_password1.setMaximum(9999)
        self.spinBox_password1.setObjectName("spinBox_password1")
        self.horizontalLayout.addWidget(self.spinBox_password1)
        self.spinBox_password2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_password2.setMinimum(1)
        self.spinBox_password2.setMaximum(9999)
        self.spinBox_password2.setObjectName("spinBox_password2")
        self.horizontalLayout.addWidget(self.spinBox_password2)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_5.addWidget(self.textBrowser, 3, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_start = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout_4.addWidget(self.pushButton_start, 0, 0, 1, 1)
        self.pushButton_stop = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.gridLayout_4.addWidget(self.pushButton_stop, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 1, 0, 1, 1)
        self.lineEdit_sys = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_sys.setReadOnly(True)
        self.lineEdit_sys.setObjectName("lineEdit_sys")
        self.gridLayout_6.addWidget(self.lineEdit_sys, 1, 1, 1, 1)
        self.lineEdit_oris = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_oris.setReadOnly(True)
        self.lineEdit_oris.setObjectName("lineEdit_oris")
        self.gridLayout_6.addWidget(self.lineEdit_oris, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_4, 0, 3, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_oripath = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_oripath.setReadOnly(True)
        self.lineEdit_oripath.setObjectName("lineEdit_oripath")
        self.gridLayout.addWidget(self.lineEdit_oripath, 0, 1, 1, 1)
        self.toolButton_oripath = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_oripath.setText("")
        self.toolButton_oripath.setObjectName("toolButton_oripath")
        self.gridLayout.addWidget(self.toolButton_oripath, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_sypath = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_sypath.setReadOnly(True)
        self.lineEdit_sypath.setObjectName("lineEdit_sypath")
        self.gridLayout.addWidget(self.lineEdit_sypath, 1, 1, 1, 1)
        self.toolButton_sypath = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_sypath.setText("")
        self.toolButton_sypath.setObjectName("toolButton_sypath")
        self.gridLayout.addWidget(self.toolButton_sypath, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_outpath = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_outpath.setReadOnly(True)
        self.lineEdit_outpath.setObjectName("lineEdit_outpath")
        self.gridLayout.addWidget(self.lineEdit_outpath, 2, 1, 1, 1)
        self.toolButton_outpath = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_outpath.setText("")
        self.toolButton_outpath.setObjectName("toolButton_outpath")
        self.gridLayout.addWidget(self.toolButton_outpath, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 3)
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setObjectName("tableView")
        self.gridLayout_5.addWidget(self.tableView, 1, 2, 3, 2)
        self.gridLayout_5.setColumnStretch(0, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_outwm = QtWidgets.QLabel(self.tab_2)
        self.label_outwm.setGeometry(QtCore.QRect(40, 180, 151, 161))
        self.label_outwm.setObjectName("label_outwm")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(400, 170, 251, 131))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setOpenExternalLinks(True)
        self.label_10.setObjectName("label_10")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(20, 20, 681, 84))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.spinBox_password1_2 = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox_password1_2.setMinimum(1)
        self.spinBox_password1_2.setMaximum(9999)
        self.spinBox_password1_2.setObjectName("spinBox_password1_2")
        self.horizontalLayout_2.addWidget(self.spinBox_password1_2)
        self.spinBox_password2_2 = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox_password2_2.setMinimum(1)
        self.spinBox_password2_2.setMaximum(9999)
        self.spinBox_password2_2.setObjectName("spinBox_password2_2")
        self.horizontalLayout_2.addWidget(self.spinBox_password2_2)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.spinBox_shapew = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox_shapew.setMinimum(1)
        self.spinBox_shapew.setMaximum(9999)
        self.spinBox_shapew.setObjectName("spinBox_shapew")
        self.horizontalLayout_5.addWidget(self.spinBox_shapew)
        self.spinBox_shapeh = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox_shapeh.setMinimum(1)
        self.spinBox_shapeh.setMaximum(9999)
        self.spinBox_shapeh.setObjectName("spinBox_shapeh")
        self.horizontalLayout_5.addWidget(self.spinBox_shapeh)
        self.gridLayout_7.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.groupBox_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.lineEdit_tq = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_tq.setReadOnly(True)
        self.lineEdit_tq.setObjectName("lineEdit_tq")
        self.horizontalLayout_3.addWidget(self.lineEdit_tq)
        self.toolButton_tq = QtWidgets.QToolButton(self.widget)
        self.toolButton_tq.setText("")
        self.toolButton_tq.setObjectName("toolButton_tq")
        self.horizontalLayout_3.addWidget(self.toolButton_tq)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(build_watermark)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(build_watermark)

    def retranslateUi(self, build_watermark):
        _translate = QtCore.QCoreApplication.translate
        build_watermark.setWindowTitle(_translate("build_watermark", "build_watermark"))
        self.label.setText(_translate("build_watermark", "<a href=\"https://github.com/kkgg0521/bulid_watermark_gui\">批量图片盲水印 提取无需原图(点击进入项目地址)</a>"))
        self.groupBox_2.setTitle(_translate("build_watermark", "设置参数"))
        self.label_5.setText(_translate("build_watermark", "密钥："))
        self.groupBox_3.setTitle(_translate("build_watermark", "操作按钮"))
        self.pushButton_start.setText(_translate("build_watermark", "开始"))
        self.pushButton_stop.setText(_translate("build_watermark", "强制终止"))
        self.groupBox_4.setTitle(_translate("build_watermark", "基本信息"))
        self.label_6.setText(_translate("build_watermark", "图片总数量："))
        self.label_7.setText(_translate("build_watermark", "水印总数量："))
        self.groupBox.setTitle(_translate("build_watermark", "选择文件"))
        self.label_2.setText(_translate("build_watermark", "原图文件夹:"))
        self.label_3.setText(_translate("build_watermark", "水印文件夹:"))
        self.label_4.setText(_translate("build_watermark", "出图文件夹:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("build_watermark", "嵌入盲水印"))
        self.label_outwm.setText(_translate("build_watermark", "输出位置"))
        self.label_10.setText(_translate("build_watermark", "<a href=\"https://github.com/kkgg0521/bulid_watermark_gui\">点击此处获取源代码</a>"))
        self.groupBox_5.setTitle(_translate("build_watermark", "输入参数"))
        self.label_8.setText(_translate("build_watermark", "密钥    ："))
        self.label_11.setText(_translate("build_watermark", "水印形状："))
        self.label_9.setText(_translate("build_watermark", "选择图片文件："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("build_watermark", "提取盲水印"))
