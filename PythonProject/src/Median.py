import cv2 as cv
class Median:
    """
        class responsible for median filtering. For more info
        see docs for gaussian in gaussian.py
        docs: https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#ga564869aa33e58769b4469101aac458f9
    """
    def __init__(self):
        self.ksize=None
    def set_ksize(self,ksize):
        """
            set kernel size
        """
        self.ksize=ksize
    def apply(self,img):
        """
            apply median filter to image
        """
        return cv.medianBlur(img,
            self.ksize
        )
