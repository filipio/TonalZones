import cv2 as cv
from qtpy.QtWidgets import QMessageBox
class Gaussian:
    def __init__(self,img_view):
        self.ksize_x=1
        self.ksize_y=1
        self.sigma_x=0
        self.sigma_y=0
        self.border=7
        self.img_view=img_view
        self.borders=[
        cv.BORDER_CONSTANT,
        cv.BORDER_REPLICATE,
        cv.BORDER_REFLECT,
        cv.BORDER_WRAP,
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
    def set_sigma_x(self,sigma_x):
        self.sigma_x=sigma_x
    def set_sigma_y(self,sigma_y):
        self.sigma_y=sigma_y
    def set_border(self,border):
        self.border=self.borders[border]
    def apply(self,img):
        print('applying gaussian filter')
        if (self.ksize_x==0 and self.ksize_y==0) or (self.ksize_x%2==1 and self.ksize_y%2==1):
            return cv.GaussianBlur(img,
                (self.ksize_x,self.ksize_y),
                self.sigma_x,
                self.sigma_y,
                self.border
            )
        else:
            # print error message about incorrect messages
            print('Gaussian filter error')
            QMessageBox.critical(self.img_view, "Error", "Kerne X and Kernel Y should be both equal 0 or odd")
            return img