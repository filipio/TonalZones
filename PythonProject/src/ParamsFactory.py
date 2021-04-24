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
    def get_fparams(self,filter_name):
        """return params to given filter"""
        if filter_name==Filter.AVARAGING:
            return {'ksize':(self.gui.avaraging_kernel_size.value(),1),#second pair should be kernel_y
                    'anchor':(self.gui.avaraging_anchor_x.value(),self.gui.avaraging_anchor_y.value()),
                    'border':BorderType(self.gui.avaraging_border_type_2.currentText())
            }
        if filter_name==Filter.GAUSSIAN:
            return {
                'gauss_size':(self.gui.gauss_k_size_x.value(),self.gui.gauss_k_size_y.value()),
                'kernel_deviation':(self.gui.gauss_sigma_x.value(),self.gui.gauss_sigma_y.value()),
                'border':BorderType(self.gui.gauss_border_type.currentText())
            }
        if filter_name==Filter.MEDIAN:
            return {
                'kernel_size':self.gui.median_kernel_size.value()
            }
        if filter_name==Filter.BILATERAL:
            print('EEEEEEEEEEEEEEEE')
            print(self.gui.bilateral_diameter.value())
            return {
                'diameter':self.gui.bilateral_diameter.value(),
                'sigma_color':self.gui.bilateral_sigma_color.value(),
                'sigma_space':self.gui.bilateral_sigma_space.value(),
                'border_type':BorderType(self.gui.bilateral_border_type.currentText())
            }