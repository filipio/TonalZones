import cv2 as cv
class Thresold:
    def __init__(self):
        self.maxval=255
        self.thres_val=0
        self.types=[
            cv.THRESH_BINARY,
            cv.THRESH_BINARY_INV
        ]
        self.type1=self.types[0]
    def set_thres_val(self,val):
        print('setting thresold value')
        self.thres_val=val
    def set_type1(self,indx):
        self.type1=self.types[indx]
        print(self.type1)
    def apply(self,img):
        print('applying thresold to img')
        # should be used to set image depending on slider value
        ret,thres_img=cv.threshold(img,self.thres_val,255,self.type1)
        return thres_img                
    def apply_otsu(self,img):
        # apply otsu algorithm to selected subset of image
        # returns image and value of thresold to which slider should be set 
        ret,thres_img=cv.threshold(img,0,255,self.type1+cv.THRESH_OTSU)
        return thres_img,ret        
    def remove_threshold(self):
        pass