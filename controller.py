from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os

from UI import Ui_MainWindow
from image_center import ImageCenter
from methods.methods_by_slider import *
from methods.methods_by_button import *



class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_init_ui()


    def set_init_ui(self):
        self.ui.btn_open_file.clicked.connect(self.open_file)

    def image_wait_for_trigger(self):
        self.methods_library = MethodsLibrary(self.ui, self.image_center)

    def open_file(self):
        fileName, fileType = QFileDialog.getOpenFileName(self, 'Open file Window', './')  # start path
        self.ui.label_filepath.setText(f'File path = {fileName}')
        self.image_center = ImageCenter(fileName, self.ui)
        self.image_wait_for_trigger()


class MethodsLibrary(object):
    def __init__(self, ui, image_center):
        self.ui = ui
        self.image_center = image_center
        # Adjustments
        self.method_denoising = MethodDenoising(self.ui.horizontalSlider_denoising, self.ui.label_denoising, self.image_center)
        self.method_brightness = MethodBrightness(self.ui.horizontalSlider_brightness, self.ui.label_Brightness, self.image_center)
        self.method_contrast = MethodContrast(self.ui.horizontalSlider_contrast, self.ui.label_Contrast, self.image_center)
        self.method_saturation = MethodSaturation(self.ui.horizontalSlider_saturation, self.ui.label_Saturation, self.image_center)
        self.method_sharpness = MethodSharpness(self.ui.horizontalSlider_sharpness, self.ui.label_Sharpness, self.image_center)

        # RGB
        self.method_R = MethodR(self.ui.horizontalSlider_RValue, self.ui.label_RValue, self.image_center)
        self.method_G = MethodG(self.ui.horizontalSlider_GValue, self.ui.label_GValue, self.image_center)
        self.method_B = MethodB(self.ui.horizontalSlider_BValue, self.ui.label_BValue, self.image_center)

        # Face
        self.method_white = MethodWhite(self.ui.horizontalSlider_white, self.ui.label_white, self.image_center)
        # self.method_lipstick = MethodLipstick(self.ui.horizontalSlider_lipstick, self.ui.label_lipstick, self.image_center)
        # self.method_thin_right = MethodThinRight(self.ui.horizontalSlider_thin_right, self.ui.label_thin_right, self.image_center)
        # self.method_thin_left = MethodThinLeft(self.ui.horizontalSlider_thin_left, self.ui.label_thin_left, self.image_center)
        # self.method_bigeye_right = MethodBigeyeRight(self.ui.horizontalSlider_bigeye_right, self.ui.label_bigeye_right, self.image_center)
        # self.method_bigeye_left = MethodBigeyeLeft(self.ui.horizontalSlider_bigeye_left, self.ui.label_bigeye_left, self.image_center)

        # Filter
    #     self.nostalgic_btn_click = 0
    #     self.pencil_btn_click = 0
    #     self.cartoon_btn_click = 0
    #     self.ui.btn_nostalgic.clicked.connect(self.click_button('nostalgic'))
    #     self.ui.btn_pencil.clicked.connect(self.click_button('pencil'))
    #     self.ui.btn_cartoon.clicked.connect(self.click_button('cartoon'))
    #
    # def click_button(self, mode):
    #     if mode == 'nostalgic':
    #         self.nostalgic_btn_click += 1
    #
    #     elif mode == 'pencil':
    #         self.pencil_btn_click += 1
    #     elif mode == 'cartoon':
    #         self.cartoon_btn_click += 1