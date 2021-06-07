class Memento:
    def __init__(self, img, thresholded_pixels, mask_belongings):
        self.img = img
        self.thresholded_pixels = thresholded_pixels
        self.mask_belongings = mask_belongings