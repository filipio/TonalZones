from FiltersEnum import Filter
import cv2 as cv
def BorderType(border_name):
    if border_name=='BORDER_CONSTANT':
        return cv.BORDER_CONSTANT
    if border_name=='BORDER_REPLICATE':
        return cv.BORDER_REPLICATE
    if border_name=='BORDER_REFLECT':
        return cv.BORDER_REFLECT
    if border_name=='BORDER_WRAP':
        return cv.BORDER_WRAP
    if border_name=='BORDER_REFLECT_101':
        return cv.BORDER_REFLECT_101
    if border_name=='BORDER_TRANSPARENT':
        return cv.BORDER_TRANSPARENT
    if border_name=='BORDER_REFLECT101':
        return cv.BORDER_REFLECT101
    if border_name=='BORDER_DEFAULT':
        return cv.BORDER_DEFAULT
    if border_name=='BORDER_ISOLATED':
        return cv.BORDER_ISOLATED
class ParamsFactory:
    """class that returns data from gui"""
    def __init__(self,gui):
        self.gui=gui
    def set_slider_mask_params(self, m_min, m_max, m_tol):
        if m_min == None:
            m_min = 0
        if m_max == None:
            m_max = 0
        self.gui.mask_min_slider.setValue(m_min)
        self.gui.mask_max_slider.setValue(m_max)
        self.gui.mask_tolerance_slider.setValue(m_tol)
        self.gui.mask_min_label.setText(str(m_min))
        self.gui.mask_max_label.setText(str(m_max))
        self.gui.mask_tolerance_label.setText(str(m_tol))

    def set_pixel_mask_params(self, m_tol):
        self.gui.pixel_tolerance_slider.setValue(m_tol)
        self.gui.pixel_tolerance_label.setText(str(m_tol))

    def set_data_from_mask(self, mask):
        print("data from mask was set : ", mask.slider_min, mask.slider_max, mask.slider_tol)
        self.set_slider_mask_params(mask.slider_min, mask.slider_max, mask.slider_tol)
        self.set_pixel_mask_params(mask.pixels_tol)