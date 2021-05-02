import numpy as np
class Mask:
    """
    This class contains all operations that modify the mask.
    """
    def __init__(self, height, width):
        self.clicked_pixels = []
        self.pixels_tol = 0
        self.slider_min = None
        self.slider_max = None
        self.slider_tol = 0
        self.height = height
        self.width = width
        self.mask = np.empty(0)
        self.is_read = False
    
    def get(self):
        return self.mask

    def add_pixel(self,grey_value):
        self.clicked_pixels.append(grey_value)
    
    def pop_pixel(self):
        try:
            self.clicked_pixels.pop()
        except IndexError:
            print("TO DO : HANDLE POP PIX ERROR")
        

    def update_pixel_tol(self, value):
        self.pixels_tol = value

    def calc_mask(self, mask_mins, mask_maxs, img, thresholded):
        self.mask = np.full((self.height, self.width), False, dtype=bool)
        for i in range(len(mask_mins)):
            self.mask = self.mask | (mask_mins[i] <= img) & (img <= mask_maxs[i])
        if not self.is_read:
            self.mask = self.mask & (thresholded == -1)
        


    def slider_mask(self, s_min, s_max, s_tol, img, thresholded):
        self.slider_min = s_min
        self.slider_max = s_max
        self.slider_tol = s_tol
        self.calc_mask([s_min - s_tol], [s_max + s_tol], img, thresholded)

    def pixel_mask(self, img, thresholded):
        mask_mins = [self.clicked_pixels[i] - self.pixels_tol for i in range(len(self.clicked_pixels))]
        mask_maxs = [self.clicked_pixels[i] + self.pixels_tol for i in range(len(self.clicked_pixels))]
        self.calc_mask(mask_mins, mask_maxs, img, thresholded)


# doesn't know about thresholded pixels