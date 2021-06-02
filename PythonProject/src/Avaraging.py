import cv2 as cv
from PyQt5.QtWidgets import QMessageBox
class Avaraging:
    """
        Class for avaraging filter, for more info see docs for Gaussian Filter
        docs: https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#ga8c45db9afe636703801b0b2e440fce37
    """
    def __init__(self,img_view):
        self.img_view=img_view
        self.ksize_x=0
        self.ksize_y=0
        self.anchor_x=0
        self.anchor_y=0
        self.border=0
        self.borders=[
        cv.BORDER_CONSTANT,
        cv.BORDER_REPLICATE,
        cv.BORDER_REFLECT,
        cv.BORDER_REFLECT_101,
        cv.BORDER_TRANSPARENT,
        cv.BORDER_REFLECT101,
        cv.BORDER_DEFAULT,
        cv.BORDER_ISOLATED
        ]
    def set_ksize_x(self,ksize_x):
        self.ksize_x=ksize_x
    def set_ksize_y(self,ksize_y):
        self.ksize_y=ksize_y
    def set_anchor_x(self,anchor_x):
        self.anchor_x=anchor_x
    def set_anchor_y(self,anchor_y):
        self.anchor_y=anchor_y
    def set_border(self,border):
        self.borde=self.borders[border]
    def apply(self,img):
        print(self.anchor_x,self.anchor_y,self.ksize_x,self.ksize_y)
        if self.anchor_x>=0 and self.anchor_y>=0 and self.anchor_x<self.ksize_x and self.anchor_y<self.ksize_y:
            return cv.blur(img,
                ksize=(self.ksize_x,self.ksize_y),
                anchor=(self.anchor_x,self.anchor_y),
                borderType=self.border
            )
        else:
            QMessageBox.critical(self.img_view, 'Error, following inequalities must hold: ', 'Kernel X>Anchor X and Kernel Y>Anchor Y')
            return img
