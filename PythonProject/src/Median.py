import cv2 as cv
class Median:
    """
        class responsible for median filtering. For more info
        see docs for gaussian in gaussian.py
    """
    def __init__(self):
        self.ksize=None
    def set_ksize(self,ksize):
        print(ksize)
        self.ksize=ksize
    def apply(self,img):
        print('applying median filter')
        return cv.medianBlur(img,
            self.ksize
        )
