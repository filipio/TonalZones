import numpy as np
from Enums import (MaskBelonging, MaskModification)
class Mask:
    """
    This class contains all operations that modify the mask.
    """
    def __init__(self, height, width, m_id):
        self.id = m_id
        self.pixel_values = []
        self.pixels_tol = 0
        self.slider_min = 0
        self.slider_max = 0
        self.slider_tol = 0
        self.height = height
        self.width = width
        self.mask = np.full((self.height, self.width), False, dtype=bool)
        self.is_read = False
        self.saved = False
        self.new = True
        self.last_modification = MaskModification.PIXEL # not sure whether this is necessery...


    def get(self, img=None, mask_belonging_arr=None, thresholded_pixels=None, modified = True):
        if not modified:
            return self.mask
        if(self.last_modification == MaskModification.RANGE):
            self._calc_mask([self.slider_min - self.slider_tol], [self.slider_max + self.slider_tol], img, mask_belonging_arr, thresholded_pixels)
        else:
            mask_mins = [self.pixel_values[i] - self.pixels_tol for i in range(len(self.pixel_values))]
            mask_maxs = [self.pixel_values[i] + self.pixels_tol for i in range(len(self.pixel_values))]
            self._calc_mask(mask_mins, mask_maxs, img, mask_belonging_arr, thresholded_pixels)
        return self.mask

    def remove(self, row, column):
        self.mask[row,column] = False

    def add_pixel(self,grey_value):
        self.pixel_values.append(grey_value)
        self.last_modification = MaskModification.PIXEL
    
    def pop_pixel(self):
        try:
            self.pixel_values.pop()
            self.last_modification = MaskModification.PIXEL
        except IndexError:
            print("TO DO : HANDLE POP PIX ERROR")

    def update_pixel_tol(self, value):
        self.pixels_tol = value
        self.last_modification = MaskModification.PIXEL
    

    def update_slider_mask(self, s_min, s_max, s_tol):
        """
        function that saves new values of a slider mask.
        """
        self.slider_min = s_min
        self.slider_max = s_max
        self.slider_tol = s_tol
        self.last_modification = MaskModification.RANGE

    def loaded_handler(self): # maybe height and width also here
        if self.last_modification == MaskModification.RANGE:
            self.pixels_tol = 0
            self.pixel_values.clear()
        else:
            self.slider_min = 0
            self.slider_max = 0
            self.slider_tol = 0


    def _calc_mask(self, mask_mins, mask_maxs, img, mask_belonging_arr, thresholded_pixels):
        """
        calculates the mask from lists of minimal and maximal values
        each pair mask_mins[i] and mask_maxs[i] is a 'from-to' range for a mask
        """
        self.new = False
        self.mask = np.full((self.height, self.width), False, dtype=bool)
        for i in range(len(mask_mins)):
            self.mask = self.mask | ((mask_mins[i] <= img) & (img <= mask_maxs[i]))
        if self.is_read and self.saved:
            self.mask[thresholded_pixels] = False
        else:
            self.mask[((mask_belonging_arr != MaskBelonging.NONE) & (mask_belonging_arr != self.id)) | (thresholded_pixels == True)] = False
        
