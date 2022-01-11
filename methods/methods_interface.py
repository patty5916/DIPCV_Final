import abc

class MethodInterface(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        return NotImplemented

    # @abc.abstractmethod
    # def update_img(self):
    #     return NotImplemented

class SliderMethodInterface(MethodInterface):
    def __init__(self, slider, label, image_center):
        self.label = label
        self.slider = slider
        self.image_center = image_center
        self.tmp_origin_img = self.image_center.display_img
        self.slider.setRange(-100, 100)
        self.slider.setProperty('value', 0)
        self.slider.valueChanged.connect(self.setSliderLabel)
        self.slider.sliderPressed.connect(self.slider_press_event)
        self.slider.sliderReleased.connect(self.slider_release_event)

    # get first picture snapshot
    def slider_press_event(self):
        self.tmp_origin_img = self.image_center.display_img

    # final update back to image center (for double check)
    def slider_release_event(self):
        img = self.setImage(self.tmp_origin_img)
        self.image_center.update_img(img)

    # image do the method
    def setImage(self, img):
        return img

    @property
    def getSliderValue(self):
        return self.slider.value()

    # get signal
    def setSliderLabel(self):
        self.label.setText(f'{self.prefix}{self.slider.value():+}')
        self.updateImg()

    def updateImg(self):
        self.image_center.update_img(self.tmp_origin_img)



class ButtonMethodInterface(MethodInterface):
    def __init__(self, button, image_center):
        self.button = button
        self.image_center = image_center
        self.tmp_origin_img = self.image_center.display_img
        self.button_click = 0

    # image do the method
    def setImage(self, img):
            return img

    def clickButton(self):
        self.button_click += 1

    def updateImg(self):
        self.image_center.update_img(self.tmp_origin_img)