import numpy as np
from Enums import (MaskBelonging, MaskModification)
class Mask:
    # Mask identifier - do not change it manually.
    free_index = 0
    """
    This class contains all operations that modify the mask.
    """
    def __init__(self, height, width):
        self.id = Mask.free_index
        Mask.free_index += 1
        self.pixel_values = []
        self.pixels_tol = 0
        self.slider_min = 0
        self.slider_max = 0
        self.slider_tol = 0
        self.mask = np.full((height, width), False, dtype=bool)
        self.new = True
        self.is_read = False
        self.saved = False
        self.last_modification = MaskModification.RANGE

    def __eq__(self, other):
        return self.id == other.id

    def get(self, img=None, mask_belonging_arr=None, thresholded_pixels=None, modified = True):
        """
        function to get the mask values based on which pixels had been thresholded and which already
        belong to other mask. The function returns masks values according to type of last modification
        that was applied.
        """
        if not modified:
            return self.mask
        if(self.last_modification == MaskModification.RANGE):
            self._calc_mask([self.slider_min - self.slider_tol], [self.slider_max + self.slider_tol], img, mask_belonging_arr, thresholded_pixels)
        else:
            pixel_mins = [self.pixel_values[i] - self.pixels_tol for i in range(len(self.pixel_values))]
            pixel_maxs = [self.pixel_values[i] + self.pixels_tol for i in range(len(self.pixel_values))]
            self._calc_mask(pixel_mins, pixel_maxs, img, mask_belonging_arr, thresholded_pixels)
        return self.mask

    def remove(self, row, column):
        """
        function to remove pixel from mask.
        """
        self.mask[row,column] = False

    def add_pixel(self,grey_value):
        """
        function to add clicked pixel value to other values.
        """
        self.pixel_values.append(grey_value)
        self.last_modification = MaskModification.PIXEL
    
    def pop_pixel(self):
        """
        function to pop clicked pixel value from other values.
        """
        try:
            self.pixel_values.pop()
            self.last_modification = MaskModification.PIXEL
        except IndexError:
            raise IndexError("there aren't any pixels to pop.")

    def update_pixel_tol(self, value):
        """
        function to update mask pixel tolerance value.
        """
        self.pixels_tol = value
        self.last_modification = MaskModification.PIXEL
    

    def update_slider_mask(self, s_min, s_max, s_tol):
        """
        function that saves new values of mask's sliders.
        """
        self.slider_min = s_min
        self.slider_max = s_max
        self.slider_tol = s_tol
        self.last_modification = MaskModification.RANGE

    def loaded_handler(self):
        """
        function is called whenever mask was loaded. Values that were in last modification are saved,
        everything else is removed.
        """
        if self.last_modification == MaskModification.RANGE:
            self.pixels_tol = 0
            self.pixel_values.clear()
        else:
            self.slider_min = 0
            self.slider_max = 0
            self.slider_tol = 0


    def _calc_mask(self, mins, maxs, img, mask_belonging_arr, thresholded_pixels):
        """
        calculates the mask from lists of minimal and maximal values
        each pair mins[i] and maxs[i] is a 'from-to' range for a mask
        """
        self.new = False
        self.mask = np.full((img.shape[0], img.shape[1]), False, dtype=bool)
        for i in range(len(mins)):
            self.mask = self.mask | ((mins[i] <= img) & (img <= maxs[i]))
        if self.is_read and self.saved:
            self.mask[thresholded_pixels] = False
        else:
            self.mask[((mask_belonging_arr != MaskBelonging.NONE) & (mask_belonging_arr != self.id)) | (thresholded_pixels == True)] = False
        
