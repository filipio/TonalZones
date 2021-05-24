import cv2 as cv
class Bilateral:
    """
        class for bilateral filetr, for more info see docs for Gaussian
    """
    def __init__(self):
        self.ksize=0
        self.sigma_color=0
        self.sigma_space=0
        self.border=0
        self.borders=[
        cv.BORDER_CONSTANT,
        cv.BORDER_WRAP,
        cv.BORDER_REPLICATE,
        cv.BORDER_REFLECT,
        cv.BORDER_REFLECT_101,
        cv.BORDER_TRANSPARENT,
        cv.BORDER_REFLECT101,
        cv.BORDER_DEFAULT,
        cv.BORDER_ISOLATED
    ]
    def set_ksize(self,ksize):
        self.ksize=ksize
    def set_sigma_color(self,sigma_color):
        self.sigma_color=sigma_color
    def set_sigma_space(self, sigma_space):
        self.sigma_space=sigma_space
    def set_border(self,border):
        self.border=self.borders[border]
    def apply(self,img):
        print('applying filter',self.ksize,self.sigma_color,self.sigma_space,self.border)
        return cv.bilateralFilter(img,
            self.ksize,
            self.sigma_color,
            self.sigma_space,   
            self.border
        )
