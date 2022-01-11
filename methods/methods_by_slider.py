from .methods_interface import SliderMethodInterface
from .opencv_engine import OpencvEngine


class MethodDenoising(SliderMethodInterface):
    def __init__(self, slider, label, image_cetner):
        super().__init__(slider, label, image_cetner)
        self.prefix = 'Denoising: '
        self.slider.setRange(100, 1000)
        self.slider.setProperty('value', 100)
        self.updateImg()

    def setImage(self, img):
        return OpencvEngine.modify_denoising(img, value1=int('{:.0f}'.format(self.slider.value()/100)), value2=1)

    def updateImg(self):
        img = self.setImage(self.tmp_origin_img)
        self.image_center.update_img(img)

    def setSliderLabel(self):
        self.label.setText('{}+{:.0f}'.format(self.prefix, int(self.slider.value()/100)))
        self.updateImg()


class MethodBrightness(SliderMethodInterface):
    def __init__(self, slider, label, image_cetner):
        super().__init__(slider, label, image_cetner)
        self.prefix = 'Brightness: '
        self.slider.setRange(0, 200)
        self.slider.setProperty('value', 100)
        self.updateImg()

    def setImage(self, img):
        return OpencvEngine.modify_brightness(img, brightness=float('{:.1f}'.format(self.slider.value()/100)))

    def updateImg(self):
        img = self.setImage(self.tmp_origin_img)
        self.image_center.update_img(img)

    def setSliderLabel(self):
        self.label.setText('{}+{:.1f}'.format(self.prefix, float(self.slider.value()/100)))
        self.updateImg()


class MethodContrast(SliderMethodInterface):
    def __init__(self, slider, label, image_cetner):
        super().__init__(slider, label, image_cetner)
        self.prefix = 'Contrast: '
        self.slider.setRange(0, 200)
        self.slider.setProperty('value', 100)
        self.updateImg()

    def setImage(self, img):
        return OpencvEngine.modify_contrast(img, contrast=float('{:.1f}'.format(self.slider.value()/100)))

    def updateImg(self):
        img = self.setImage(self.tmp_origin_img)
        self.image_center.update_img(img)

    def setSliderLabel(self):
        self.label.setText('{}+{:.1f}'.format(self.prefix, float(self.slider.value()/100)))
        self.updateImg()

class MethodSaturation(SliderMethodInterface):
    def __init__(self, slider, label, image_cetner):
        super().__init__(slider, label, image_cetner)
        self.prefix = 'Saturation: '
        self.slider.setRange(0, 200)
        self.slider.setProperty('value', 100)
        self.updateImg()

    def setImage(self, img):
        return OpencvEngine.modify_color(img, color=float('{:.1f}'.format(self.slider.value()/100)))

    def updateImg(self):
        img = self.setImage(self.tmp_origin_img)
        self.image_center.update_img(img)

    def setSliderLabel(self):
        self.label.setText('{}+{:.1f}'.format(self.prefix, float(self.slider.value()/100)))
        self.updateImg()


class MethodSharpness(SliderMethodInterface):
    def __init__(self, slider, label, image_cetner):
        super().__init__(slider, label, image_cetner)
        self.prefix = 'Sharpness: '
        self.slider.setRange(0, 200)
        self.slider.setProperty('value', 100)
        self.updateImg()

    def setImage(self, img):
        return OpencvEngine.modify_sharpness(img, sharpness=float('{:.1f}'.format(self.slider.value()/100)))

    def updateImg(self):
        img = self.setImage(self.tmp_origin_img)
        self.image_center.update_img(img)

    def setSliderLabel(self):
        self.label.setText('{}+{:.1f}'.format(self.prefix, float(self.slider.value()/100)))
        self.updateImg()


class MethodR(SliderMethodInterface):
    def __init__(self, slider, label, image_cetner):
        super().__init__(slider, label, image_cetner)
        self.prefix = 'R Value: '
        self.slider.setRange(0, 200)
        self.slider.setProperty('value', 100)
        self.updateImg()

    def setImage(self, img):
        return OpencvEngine.modify_rgb(img, r=float('{:.1f}'.format(self.slider.value()/100)), g=0, b=0)

    def updateImg(self):
        img = self.setImage(self.tmp_origin_img)
        self.image_center.update_img(img)

    def setSliderLabel(self):
        self.label.setText('{}+{:.1f}'.format(self.prefix, float(self.slider.value()/100)))
        self.updateImg()


class MethodG(SliderMethodInterface):
    def __init__(self, slider, label, image_cetner):
        super().__init__(slider, label, image_cetner)
        self.prefix = 'G Value: '
        self.slider.setRange(0, 200)
        self.slider.setProperty('value', 100)
        self.updateImg()

    def setImage(self, img):
        return OpencvEngine.modify_rgb(img, r=0, g=float('{:.1f}'.format(self.slider.value()/100)), b=0)

    def updateImg(self):
        img = self.setImage(self.tmp_origin_img)
        self.image_center.update_img(img)

    def setSliderLabel(self):
        self.label.setText('{}+{:.1f}'.format(self.prefix, float(self.slider.value()/100)))
        self.updateImg()


class MethodB(SliderMethodInterface):
    def __init__(self, slider, label, image_cetner):
        super().__init__(slider, label, image_cetner)
        self.prefix = 'B Value: '
        self.slider.setRange(0, 200)
        self.slider.setProperty('value', 100)
        self.updateImg()

    def setImage(self, img):
        return OpencvEngine.modify_rgb(img, r=0, g=0, b=float('{:.1f}'.format(self.slider.value()/100)))

    def updateImg(self):
        img = self.setImage(self.tmp_origin_img)
        self.image_center.update_img(img)

    def setSliderLabel(self):
        self.label.setText('{}+{:.1f}'.format(self.prefix, float(self.slider.value()/100)))
        self.updateImg()


class MethodWhite(SliderMethodInterface):
    def __init__(self, slider, label, image_cetner):
        super().__init__(slider, label, image_cetner)
        self.prefix = 'White: '
        self.slider.setRange(100, 1000)
        self.slider.setProperty('value', 100)
        self.updateImg()

    def setImage(self, img):
        return OpencvEngine.modify_white(img, value1=1, value2=int('{:.0f}'.format(self.slider.value()/100)))

    def updateImg(self):
        img = self.setImage(self.tmp_origin_img)
        self.image_center.update_img(img)

    def setSliderLabel(self):
        self.label.setText('{}+{:.0f}'.format(self.prefix, int(self.slider.value()/100)))
        self.updateImg()


class MethodLipstick(SliderMethodInterface):
    def __init__(self, slider, label, image_cetner):
        super().__init__(slider, label, image_cetner)
        self.prefix = 'Lipstick: '
        self.slider.setRange(1, 255)
        self.slider.setProperty('value', 200)
        self.updateImg()

    def setImage(self, img):
        return OpencvEngine.modify_lipstick(img, r=int('{:.0f}'.format(self.slider.value())))

    def updateImg(self):
        img = self.setImage(self.tmp_origin_img)
        self.image_center.update_img(img)

    def setSliderLabel(self):
        self.label.setText('{}+{:.0f}'.format(self.prefix, int(self.slider.value())))
        self.updateImg()


class MethodThinRight(SliderMethodInterface):
    def __init__(self, slider, label, image_cetner):
        super().__init__(slider, label, image_cetner)
        self.prefix = 'Right: '
        self.slider.setRange(0, 200)
        self.slider.setProperty('value', 0)
        self.updateImg()

    def setImage(self, img):
        return OpencvEngine.modify_thin(img, right=int('{:.0f}'.format(self.slider.value())), left=0)

    def updateImg(self):
        img = self.setImage(self.tmp_origin_img)
        self.image_center.update_img(img)

    def setSliderLabel(self):
        self.label.setText('{}+{:.0f}'.format(self.prefix, int(self.slider.value())))
        self.updateImg()



class MethodThinLeft(SliderMethodInterface):
    def __init__(self, slider, label, image_cetner):
        super().__init__(slider, label, image_cetner)
        self.prefix = 'Left: '
        self.slider.setRange(0, 200)
        self.slider.setProperty('value', 0)
        self.updateImg()

    def setImage(self, img):
        return OpencvEngine.modify_thin(img, right=0, left=int('{:.0f}'.format(self.slider.value())))

    def updateImg(self):
        img = self.setImage(self.tmp_origin_img)
        self.image_center.update_img(img)

    def setSliderLabel(self):
        self.label.setText('{}+{:.0f}'.format(self.prefix, int(self.slider.value())))
        self.updateImg()

class MethodBigeyeRight(SliderMethodInterface):
    def __init__(self, slider, label, image_cetner):
        super().__init__(slider, label, image_cetner)
        self.prefix = 'Right: '
        self.slider.setRange(0, 200)
        self.slider.setProperty('value', 0)
        self.updateImg()

    def setImage(self, img):
        return OpencvEngine.modify_bigeye(img, right=int('{:.0f}'.format(self.slider.value())), left=0)

    def updateImg(self):
        img = self.setImage(self.tmp_origin_img)
        self.image_center.update_img(img)

    def setSliderLabel(self):
        self.label.setText('{}+{:.0f}'.format(self.prefix, int(self.slider.value())))
        self.updateImg()



class MethodBigeyeLeft(SliderMethodInterface):
    def __init__(self, slider, label, image_cetner):
        super().__init__(slider, label, image_cetner)
        self.prefix = 'Left: '
        self.slider.setRange(0, 200)
        self.slider.setProperty('value', 0)
        self.updateImg()

    def setImage(self, img):
        return OpencvEngine.modify_bigeye(img, right=0, left=int('{:.0f}'.format(self.slider.value())))

    def updateImg(self):
        img = self.setImage(self.tmp_origin_img)
        self.image_center.update_img(img)

    def setSliderLabel(self):
        self.label.setText('{}+{:.0f}'.format(self.prefix, int(self.slider.value())))
        self.updateImg()