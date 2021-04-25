import cv2 as cv
class Thresold:
    def __init__(self):
        self.maxval=255
        self.thres_val=0
        self.type1=None
        self.type2=None
        self.types=[
            cv.THRESH_BINARY,
            cv.THRESH_BINARY_INV,
            cv.THRESH_TRUNC,
            cv.THRESH_TOZERO,
            cv.THRESH_TOZERO_INV,   
            cv.THRESH_OTSU
        ]
    def set_maxval(self,val):
        self.maxval=val
    def set_thres_val(self,val):
        self.maxval=val
    def set_type1(self,indx):
        self.type1=self.types[indx]
    def set_type2(self,indx):
        self.type2=self.types[indx]
    def apply(self,img,thr_val):
        # should be used to set image depending on slider value
        ret,thres_img=cv.threshold(img,thr_val,255,cv.THRESH_BINARY)
        return thres_img                
    def apply_otsu(self,img):
        # apply otsu algorithm to selected subset of image
        # returns image and value of thresold to which slider should be set 
        ret,thres_img=cv.threshold(img,0,255,cv.self.type1+self.type2)
        return thres_img        