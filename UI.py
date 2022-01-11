# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1438, 857)
        MainWindow.setMaximumSize(QtCore.QSize(1438, 857))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_open_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_file.setGeometry(QtCore.QRect(20, 590, 111, 31))
        self.btn_open_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_open_file.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"background-color: #dcdcdc;\n"
"border-color: 1px rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-style: outset;")
        self.btn_open_file.setAutoDefault(False)
        self.btn_open_file.setObjectName("btn_open_file")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 29, 691, 541))
        self.widget.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.widget.setObjectName("widget")
        self.label_img = QtWidgets.QLabel(self.widget)
        self.label_img.setGeometry(QtCore.QRect(9, 14, 671, 521))
        self.label_img.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_img.setText("")
        self.label_img.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img.setObjectName("label_img")
        self.label_adjustments = QtWidgets.QLabel(self.centralwidget)
        self.label_adjustments.setGeometry(QtCore.QRect(740, 30, 301, 31))
        self.label_adjustments.setStyleSheet("font:10pt \"微軟正黑體\";\n"
"color: rgb(255, 170, 0);\n"
"font-weight: bold;")
        self.label_adjustments.setObjectName("label_adjustments")
        self.label_color_balance = QtWidgets.QLabel(self.centralwidget)
        self.label_color_balance.setGeometry(QtCore.QRect(740, 370, 301, 31))
        self.label_color_balance.setStyleSheet("font:10pt \"微軟正黑體\";\n"
"color: rgb(255, 170, 0);\n"
"font-weight: bold;")
        self.label_color_balance.setObjectName("label_color_balance")
        self.label_denoising = QtWidgets.QLabel(self.centralwidget)
        self.label_denoising.setGeometry(QtCore.QRect(740, 90, 131, 21))
        self.label_denoising.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"color: rgb(255, 255, 255);")
        self.label_denoising.setTextFormat(QtCore.Qt.AutoText)
        self.label_denoising.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_denoising.setObjectName("label_denoising")
        self.label_white = QtWidgets.QLabel(self.centralwidget)
        self.label_white.setGeometry(QtCore.QRect(1100, 90, 121, 21))
        self.label_white.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"color: rgb(255, 255, 255);")
        self.label_white.setTextFormat(QtCore.Qt.AutoText)
        self.label_white.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_white.setObjectName("label_white")
        self.label_Brightness = QtWidgets.QLabel(self.centralwidget)
        self.label_Brightness.setGeometry(QtCore.QRect(740, 140, 131, 21))
        self.label_Brightness.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"color: rgb(255, 255, 255);")
        self.label_Brightness.setTextFormat(QtCore.Qt.AutoText)
        self.label_Brightness.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Brightness.setObjectName("label_Brightness")
        self.label_Contrast = QtWidgets.QLabel(self.centralwidget)
        self.label_Contrast.setGeometry(QtCore.QRect(740, 190, 131, 21))
        self.label_Contrast.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"color: rgb(255, 255, 255);")
        self.label_Contrast.setTextFormat(QtCore.Qt.AutoText)
        self.label_Contrast.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Contrast.setObjectName("label_Contrast")
        self.label_Saturation = QtWidgets.QLabel(self.centralwidget)
        self.label_Saturation.setGeometry(QtCore.QRect(740, 240, 131, 21))
        self.label_Saturation.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"color: rgb(255, 255, 255);")
        self.label_Saturation.setTextFormat(QtCore.Qt.AutoText)
        self.label_Saturation.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Saturation.setObjectName("label_Saturation")
        self.label_RValue = QtWidgets.QLabel(self.centralwidget)
        self.label_RValue.setGeometry(QtCore.QRect(740, 430, 131, 21))
        self.label_RValue.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"color: rgb(255, 255, 255);")
        self.label_RValue.setTextFormat(QtCore.Qt.AutoText)
        self.label_RValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_RValue.setObjectName("label_RValue")
        self.label_GValue = QtWidgets.QLabel(self.centralwidget)
        self.label_GValue.setGeometry(QtCore.QRect(740, 480, 131, 21))
        self.label_GValue.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"color: rgb(255, 255, 255);")
        self.label_GValue.setTextFormat(QtCore.Qt.AutoText)
        self.label_GValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_GValue.setObjectName("label_GValue")
        self.label_BValue = QtWidgets.QLabel(self.centralwidget)
        self.label_BValue.setGeometry(QtCore.QRect(740, 530, 131, 21))
        self.label_BValue.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"color: rgb(255, 255, 255);")
        self.label_BValue.setTextFormat(QtCore.Qt.AutoText)
        self.label_BValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_BValue.setObjectName("label_BValue")
        self.horizontalSlider_denoising = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_denoising.setGeometry(QtCore.QRect(890, 90, 160, 22))
        self.horizontalSlider_denoising.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_denoising.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #151414;\n"
"    height: 1px; \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #151414, stop:1 #151414);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #ffffff);\n"
"    border: 1px solid #8f8f8f;\n"
"    width: 15px;\n"
"    margin: -8px 0; \n"
"    border-radius: 8px;\n"
"}")
        self.horizontalSlider_denoising.setMinimum(100)
        self.horizontalSlider_denoising.setMaximum(1000)
        self.horizontalSlider_denoising.setSingleStep(100)
        self.horizontalSlider_denoising.setPageStep(100)
        self.horizontalSlider_denoising.setProperty("value", 100)
        self.horizontalSlider_denoising.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_denoising.setObjectName("horizontalSlider_denoising")
        self.horizontalSlider_white = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_white.setGeometry(QtCore.QRect(1240, 90, 160, 22))
        self.horizontalSlider_white.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_white.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #151414;\n"
"    height: 1px; \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #151414, stop:1 #151414);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #ffffff);\n"
"    border: 1px solid #8f8f8f;\n"
"    width: 15px;\n"
"    margin: -8px 0; \n"
"    border-radius: 8px;\n"
"}")
        self.horizontalSlider_white.setMinimum(100)
        self.horizontalSlider_white.setMaximum(1000)
        self.horizontalSlider_white.setSliderPosition(100)
        self.horizontalSlider_white.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_white.setObjectName("horizontalSlider_white")
        self.horizontalSlider_brightness = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_brightness.setGeometry(QtCore.QRect(890, 140, 160, 22))
        self.horizontalSlider_brightness.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_brightness.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #151414;\n"
"    height: 1px; \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #151414, stop:1 #151414);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #ffffff);\n"
"    border: 1px solid #8f8f8f;\n"
"    width: 15px;\n"
"    margin: -8px 0; \n"
"    border-radius: 8px;\n"
"}")
        self.horizontalSlider_brightness.setMaximum(200)
        self.horizontalSlider_brightness.setSingleStep(0)
        self.horizontalSlider_brightness.setProperty("value", 100)
        self.horizontalSlider_brightness.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_brightness.setObjectName("horizontalSlider_brightness")
        self.horizontalSlider_contrast = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_contrast.setGeometry(QtCore.QRect(890, 190, 160, 22))
        self.horizontalSlider_contrast.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_contrast.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #151414;\n"
"    height: 1px; \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #151414, stop:1 #151414);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #ffffff);\n"
"    border: 1px solid #8f8f8f;\n"
"    width: 15px;\n"
"    margin: -8px 0; \n"
"    border-radius: 8px;\n"
"}")
        self.horizontalSlider_contrast.setSliderPosition(49)
        self.horizontalSlider_contrast.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_contrast.setObjectName("horizontalSlider_contrast")
        self.horizontalSlider_saturation = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_saturation.setGeometry(QtCore.QRect(890, 240, 160, 22))
        self.horizontalSlider_saturation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_saturation.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #151414;\n"
"    height: 1px; \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #151414, stop:1 #151414);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #ffffff);\n"
"    border: 1px solid #8f8f8f;\n"
"    width: 15px;\n"
"    margin: -8px 0; \n"
"    border-radius: 8px;\n"
"}")
        self.horizontalSlider_saturation.setSliderPosition(49)
        self.horizontalSlider_saturation.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_saturation.setObjectName("horizontalSlider_saturation")
        self.horizontalSlider_RValue = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_RValue.setGeometry(QtCore.QRect(890, 430, 160, 22))
        self.horizontalSlider_RValue.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_RValue.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #151414;\n"
"    height: 1px; \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #151414, stop:1 #151414);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #ffffff);\n"
"    border: 1px solid #8f8f8f;\n"
"    width: 15px;\n"
"    margin: -8px 0; \n"
"    border-radius: 8px;\n"
"}")
        self.horizontalSlider_RValue.setSliderPosition(49)
        self.horizontalSlider_RValue.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_RValue.setObjectName("horizontalSlider_RValue")
        self.horizontalSlider_GValue = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_GValue.setGeometry(QtCore.QRect(890, 480, 160, 22))
        self.horizontalSlider_GValue.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_GValue.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #151414;\n"
"    height: 1px; \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #151414, stop:1 #151414);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #ffffff);\n"
"    border: 1px solid #8f8f8f;\n"
"    width: 15px;\n"
"    margin: -8px 0; \n"
"    border-radius: 8px;\n"
"}")
        self.horizontalSlider_GValue.setSliderPosition(49)
        self.horizontalSlider_GValue.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_GValue.setObjectName("horizontalSlider_GValue")
        self.horizontalSlider_BValue = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_BValue.setGeometry(QtCore.QRect(890, 530, 160, 22))
        self.horizontalSlider_BValue.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_BValue.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #151414;\n"
"    height: 1px; \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #151414, stop:1 #151414);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #ffffff);\n"
"    border: 1px solid #8f8f8f;\n"
"    width: 15px;\n"
"    margin: -8px 0; \n"
"    border-radius: 8px;\n"
"}")
        self.horizontalSlider_BValue.setSliderPosition(49)
        self.horizontalSlider_BValue.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_BValue.setObjectName("horizontalSlider_BValue")
        self.label_filepath = QtWidgets.QLabel(self.centralwidget)
        self.label_filepath.setGeometry(QtCore.QRect(30, 810, 681, 21))
        self.label_filepath.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.label_filepath.setObjectName("label_filepath")
        self.label_skin = QtWidgets.QLabel(self.centralwidget)
        self.label_skin.setGeometry(QtCore.QRect(1090, 30, 321, 31))
        self.label_skin.setStyleSheet("font:10pt \"微軟正黑體\";\n"
"color: rgb(255, 170, 0);\n"
"font-weight: bold;")
        self.label_skin.setObjectName("label_skin")
        self.label_lipstick = QtWidgets.QLabel(self.centralwidget)
        self.label_lipstick.setGeometry(QtCore.QRect(1100, 140, 121, 21))
        self.label_lipstick.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"color: rgb(255, 255, 255);")
        self.label_lipstick.setTextFormat(QtCore.Qt.AutoText)
        self.label_lipstick.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_lipstick.setObjectName("label_lipstick")
        self.horizontalSlider_sharpness = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_sharpness.setGeometry(QtCore.QRect(890, 290, 160, 22))
        self.horizontalSlider_sharpness.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_sharpness.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #151414;\n"
"    height: 1px; \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #151414, stop:1 #151414);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #ffffff);\n"
"    border: 1px solid #8f8f8f;\n"
"    width: 15px;\n"
"    margin: -8px 0; \n"
"    border-radius: 8px;\n"
"}")
        self.horizontalSlider_sharpness.setSliderPosition(49)
        self.horizontalSlider_sharpness.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_sharpness.setObjectName("horizontalSlider_sharpness")
        self.label_Sharpness = QtWidgets.QLabel(self.centralwidget)
        self.label_Sharpness.setGeometry(QtCore.QRect(740, 290, 131, 21))
        self.label_Sharpness.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"color: rgb(255, 255, 255);")
        self.label_Sharpness.setTextFormat(QtCore.Qt.AutoText)
        self.label_Sharpness.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Sharpness.setObjectName("label_Sharpness")
        self.horizontalSlider_lipstick = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_lipstick.setGeometry(QtCore.QRect(1240, 140, 160, 22))
        self.horizontalSlider_lipstick.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_lipstick.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #151414;\n"
"    height: 1px; \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #151414, stop:1 #151414);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #ffffff);\n"
"    border: 1px solid #8f8f8f;\n"
"    width: 15px;\n"
"    margin: -8px 0; \n"
"    border-radius: 8px;\n"
"}")
        self.horizontalSlider_lipstick.setMinimum(1)
        self.horizontalSlider_lipstick.setMaximum(255)
        self.horizontalSlider_lipstick.setProperty("value", 1)
        self.horizontalSlider_lipstick.setSliderPosition(1)
        self.horizontalSlider_lipstick.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_lipstick.setObjectName("horizontalSlider_lipstick")
        self.label_filter = QtWidgets.QLabel(self.centralwidget)
        self.label_filter.setGeometry(QtCore.QRect(1090, 460, 331, 31))
        self.label_filter.setStyleSheet("font:10pt \"微軟正黑體\";\n"
"color: rgb(255, 170, 0);\n"
"font-weight: bold;")
        self.label_filter.setObjectName("label_filter")
        self.btn_nostalgic = QtWidgets.QPushButton(self.centralwidget)
        self.btn_nostalgic.setGeometry(QtCore.QRect(1120, 520, 91, 31))
        self.btn_nostalgic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_nostalgic.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"background-color: #dcdcdc;\n"
"border-color: 1px rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-style: outset;")
        self.btn_nostalgic.setAutoDefault(False)
        self.btn_nostalgic.setObjectName("btn_nostalgic")
        self.btn_pencil = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pencil.setGeometry(QtCore.QRect(1230, 520, 81, 31))
        self.btn_pencil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_pencil.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"background-color: #dcdcdc;\n"
"border-color: 1px rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-style: outset;")
        self.btn_pencil.setAutoDefault(False)
        self.btn_pencil.setObjectName("btn_pencil")
        self.btn_cartoon = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cartoon.setGeometry(QtCore.QRect(1330, 520, 81, 31))
        self.btn_cartoon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cartoon.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"background-color: #dcdcdc;\n"
"border-color: 1px rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-style: outset;")
        self.btn_cartoon.setAutoDefault(False)
        self.btn_cartoon.setObjectName("btn_cartoon")
        self.btn_save_img = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save_img.setGeometry(QtCore.QRect(150, 590, 111, 31))
        self.btn_save_img.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save_img.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"background-color: #dcdcdc;\n"
"border-color: 1px rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-style: outset;")
        self.btn_save_img.setAutoDefault(False)
        self.btn_save_img.setObjectName("btn_save_img")
        self.label_thin_right = QtWidgets.QLabel(self.centralwidget)
        self.label_thin_right.setGeometry(QtCore.QRect(1120, 230, 101, 21))
        self.label_thin_right.setStyleSheet("font: 8pt \"微軟正黑體\";\n"
"color: rgb(255, 255, 255);")
        self.label_thin_right.setTextFormat(QtCore.Qt.AutoText)
        self.label_thin_right.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_thin_right.setObjectName("label_thin_right")
        self.horizontalSlider_thin_left = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_thin_left.setGeometry(QtCore.QRect(1240, 270, 160, 22))
        self.horizontalSlider_thin_left.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_thin_left.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #151414;\n"
"    height: 1px; \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #151414, stop:1 #151414);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #ffffff);\n"
"    border: 1px solid #8f8f8f;\n"
"    width: 15px;\n"
"    margin: -8px 0; \n"
"    border-radius: 8px;\n"
"}")
        self.horizontalSlider_thin_left.setMaximum(200)
        self.horizontalSlider_thin_left.setSingleStep(10)
        self.horizontalSlider_thin_left.setProperty("value", 0)
        self.horizontalSlider_thin_left.setSliderPosition(0)
        self.horizontalSlider_thin_left.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_thin_left.setObjectName("horizontalSlider_thin_left")
        self.horizontalSlider_thin_right = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_thin_right.setGeometry(QtCore.QRect(1240, 230, 160, 22))
        self.horizontalSlider_thin_right.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_thin_right.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #151414;\n"
"    height: 1px; \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #151414, stop:1 #151414);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #ffffff);\n"
"    border: 1px solid #8f8f8f;\n"
"    width: 15px;\n"
"    margin: -8px 0; \n"
"    border-radius: 8px;\n"
"}")
        self.horizontalSlider_thin_right.setMaximum(200)
        self.horizontalSlider_thin_right.setSingleStep(10)
        self.horizontalSlider_thin_right.setProperty("value", 0)
        self.horizontalSlider_thin_right.setSliderPosition(0)
        self.horizontalSlider_thin_right.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_thin_right.setObjectName("horizontalSlider_thin_right")
        self.label_thin_left = QtWidgets.QLabel(self.centralwidget)
        self.label_thin_left.setGeometry(QtCore.QRect(1120, 270, 101, 21))
        self.label_thin_left.setStyleSheet("font: 8pt \"微軟正黑體\";\n"
"color: rgb(255, 255, 255);")
        self.label_thin_left.setTextFormat(QtCore.Qt.AutoText)
        self.label_thin_left.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_thin_left.setObjectName("label_thin_left")
        self.label_thin = QtWidgets.QLabel(self.centralwidget)
        self.label_thin.setGeometry(QtCore.QRect(1120, 190, 101, 21))
        self.label_thin.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"color: rgb(255, 255, 255);")
        self.label_thin.setTextFormat(QtCore.Qt.AutoText)
        self.label_thin.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_thin.setObjectName("label_thin")
        self.label_bigeye_right = QtWidgets.QLabel(self.centralwidget)
        self.label_bigeye_right.setGeometry(QtCore.QRect(1120, 360, 101, 21))
        self.label_bigeye_right.setStyleSheet("font: 8pt \"微軟正黑體\";\n"
"color: rgb(255, 255, 255);")
        self.label_bigeye_right.setTextFormat(QtCore.Qt.AutoText)
        self.label_bigeye_right.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_bigeye_right.setObjectName("label_bigeye_right")
        self.label_bigeye = QtWidgets.QLabel(self.centralwidget)
        self.label_bigeye.setGeometry(QtCore.QRect(1120, 320, 101, 21))
        self.label_bigeye.setStyleSheet("font: 9pt \"微軟正黑體\";\n"
"color: rgb(255, 255, 255);")
        self.label_bigeye.setTextFormat(QtCore.Qt.AutoText)
        self.label_bigeye.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_bigeye.setObjectName("label_bigeye")
        self.label_bigeye_left = QtWidgets.QLabel(self.centralwidget)
        self.label_bigeye_left.setGeometry(QtCore.QRect(1120, 400, 101, 21))
        self.label_bigeye_left.setStyleSheet("font: 8pt \"微軟正黑體\";\n"
"color: rgb(255, 255, 255);")
        self.label_bigeye_left.setTextFormat(QtCore.Qt.AutoText)
        self.label_bigeye_left.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_bigeye_left.setObjectName("label_bigeye_left")
        self.horizontalSlider_bigeye_right = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_bigeye_right.setGeometry(QtCore.QRect(1240, 360, 160, 22))
        self.horizontalSlider_bigeye_right.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_bigeye_right.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #151414;\n"
"    height: 1px; \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #151414, stop:1 #151414);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #ffffff);\n"
"    border: 1px solid #8f8f8f;\n"
"    width: 15px;\n"
"    margin: -8px 0; \n"
"    border-radius: 8px;\n"
"}")
        self.horizontalSlider_bigeye_right.setMaximum(200)
        self.horizontalSlider_bigeye_right.setSingleStep(10)
        self.horizontalSlider_bigeye_right.setProperty("value", 0)
        self.horizontalSlider_bigeye_right.setSliderPosition(0)
        self.horizontalSlider_bigeye_right.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_bigeye_right.setObjectName("horizontalSlider_bigeye_right")
        self.horizontalSlider_bigeye_left = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_bigeye_left.setGeometry(QtCore.QRect(1240, 400, 160, 22))
        self.horizontalSlider_bigeye_left.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_bigeye_left.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #151414;\n"
"    height: 1px; \n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #151414, stop:1 #151414);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #ffffff);\n"
"    border: 1px solid #8f8f8f;\n"
"    width: 15px;\n"
"    margin: -8px 0; \n"
"    border-radius: 8px;\n"
"}")
        self.horizontalSlider_bigeye_left.setMaximum(200)
        self.horizontalSlider_bigeye_left.setSingleStep(10)
        self.horizontalSlider_bigeye_left.setProperty("value", 0)
        self.horizontalSlider_bigeye_left.setSliderPosition(0)
        self.horizontalSlider_bigeye_left.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_bigeye_left.setObjectName("horizontalSlider_bigeye_left")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1438, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Beauty Camera"))
        self.btn_open_file.setText(_translate("MainWindow", "Open File"))
        self.label_adjustments.setText(_translate("MainWindow", "Adjustments"))
        self.label_color_balance.setText(_translate("MainWindow", "Color Balance"))
        self.label_denoising.setText(_translate("MainWindow", "Denoising: +0"))
        self.label_white.setText(_translate("MainWindow", "White: +0"))
        self.label_Brightness.setText(_translate("MainWindow", "Brightness: +0"))
        self.label_Contrast.setText(_translate("MainWindow", "Contrast: +0"))
        self.label_Saturation.setText(_translate("MainWindow", "Saturation: +0"))
        self.label_RValue.setText(_translate("MainWindow", "R Value: +0"))
        self.label_GValue.setText(_translate("MainWindow", "G Value: +0"))
        self.label_BValue.setText(_translate("MainWindow", "B Value: +0"))
        self.label_filepath.setText(_translate("MainWindow", "File Path = "))
        self.label_skin.setText(_translate("MainWindow", "Face"))
        self.label_lipstick.setText(_translate("MainWindow", "Lipstick: +0"))
        self.label_Sharpness.setText(_translate("MainWindow", "Sharpness: +0"))
        self.label_filter.setText(_translate("MainWindow", "Filter"))
        self.btn_nostalgic.setText(_translate("MainWindow", "Nostalgic"))
        self.btn_pencil.setText(_translate("MainWindow", "Pencil"))
        self.btn_cartoon.setText(_translate("MainWindow", "Cartoon"))
        self.btn_save_img.setText(_translate("MainWindow", "Save Image"))
        self.label_thin_right.setText(_translate("MainWindow", "Right: +0"))
        self.label_thin_left.setText(_translate("MainWindow", "Left: +0"))
        self.label_thin.setText(_translate("MainWindow", "Thin"))
        self.label_bigeye_right.setText(_translate("MainWindow", "Right: +0"))
        self.label_bigeye.setText(_translate("MainWindow", "Big-eye"))
        self.label_bigeye_left.setText(_translate("MainWindow", "Left: +0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

