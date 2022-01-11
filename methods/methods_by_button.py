import numpy as np

from .methods_interface import ButtonMethodInterface
from .opencv_engine import OpencvEngine


def setImage(click, img):
    if click % 2 == 0:
        return img
    else:
        return OpencvEngine.old_pic(img)
