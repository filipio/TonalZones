import cv2 as cv
class Avaraging:
    def __init__(self):
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
        return cv.blur(img,
            ksize=(self.ksize_x,self.ksize_y),
            anchor=(self.anchor_x,self.anchor_y),
            borderType=self.border
        )
