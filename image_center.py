from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPixmap
from methods.opencv_engine import OpencvEngine
from PIL.ImageQt import ImageQt
from PIL import Image
import numpy as np
import logging

class LabelMouseController(object):
    def __init__(self, image_center):
        self.image_center = image_center
        self.ui = self.image_center.ui
        # self.ui.label_img.mousePressEvent = self.mouse_press_event
        # self.ui.label_img.mouseReleaseEvent = self.mouse_release_event
        # self.ui.label_img.mouseMoveEvent = self.mouse_moving_event

    def mouse_press_event(self, event):
        msg = f'{event.x()=}, {event.y()=}, {event.button()=}'
        x = event.x()
        y = event.y()
        norm_x = x/self.image_center.qpixmap.width()
        norm_y = y/self.image_center.qpixmap.height()
        real_x = int(norm_x*self.image_center.origin_img_width)
        real_y = int(norm_y*self.image_center.origin_img_height)
        self.ui.label_click_pos.setText(f'Clicked position = ({x}, {y})')
        self.ui.label_norm_pos.setText(f'Normalized position = ({norm_x:.3f}, {norm_y:.3f})')
        self.ui.label_real_pos.setText(f'Real position = ({real_x}, {real_y})')

    def mouse_release_event(self, event):
        msg = f'{event.x()=}, {event.y()=}, {event.button()=}'

    def mouse_moving_event(self, event):
        msg = f'{event.x()=}, {event.y()=}, {event.button()=}'


class ImageCenter(object):
    def __init__(self, img_path, ui):
        self.img_path = img_path
        self.ui = ui
        self.label_mouse_controller = LabelMouseController(self)
        self.zoom_value = 1
        self.read_file_and_init()

    def read_file_and_init(self):
        try:
            self.origin_img = OpencvEngine.read_image(self.img_path)  # if cancel, no error !!!!
            self.origin_img_height, self.origin_img_width, self.origin_img_channel = self.origin_img.shape  # need this to make error !!!
        except:
            self.origin_img = OpencvEngine.read_image('camera.png')
            self.origin_img_height, self.origin_img_width, self.origin_img_channel = self.origin_img.shape

        self.display_img = np.copy(self.origin_img)  # make a clone
        self.update_label_img()

    def update_img(self, img):
        self.display_img = img # default = not change, like zoom
        self.update_label_img()


    def resize_img(self):
        scaled_pixmap = self.qpixmap.scaledToHeight(self.qpixmap_height)
        self.ui.label_img.setPixmap(scaled_pixmap)

    def update_label_img(self):
        bytesPerline = 3 * self.origin_img_width
        qimg = QImage(np.array(self.display_img), self.origin_img_width, self.origin_img_height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap = QPixmap.fromImage(qimg)
        self.qpixmap_height = self.qpixmap.height()
        self.ui.label_img.setPixmap(QPixmap.fromImage(qimg))
        self.resize_img()
        self.ui.label_img.setPixmap(self.qpixmap)
        self.ui.label_img.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)