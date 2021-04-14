import cv2 as cv
from PyQt5.QtGui import QImage
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (QFileDialog,QMessageBox, QComboBox)
from PyQt5.QtWidgets import QPushButton
import numpy as np

class Image:
    """
    Image is a class responsible for doing operations on an image. Class should be initialized when
    new image from file is required. Every operation that is operating on an image should be contained
    in this class.
    Insert necessery methods below.
    """
    def __init__(self, graphic_area):
        self.image = np.empty(0)
        self.tmp_image = np.empty(0)
        self.graphic_area = graphic_area
        self.active_img=np.empty(0)#active part of image that will be edited
    def _update_img(self,img):
        self.tmp_image = img
        frame = cv.cvtColor(self.tmp_image, cv.COLOR_BGR2RGB)
        img_rep = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format.Format_RGB888)
        self.graphic_area.setPixmap(QtGui.QPixmap.fromImage(img_rep))

    def _error_msg(self):
        if self.tmp_image.size == 0: 
            msg_box = QMessageBox.about(self.graphic_area,"Error","Image needs to be loaded first.")
            return True
        return False

    def _mask(self, min, max, img):
        return img[(min <= img) & (img <= max)]

    def save(self):
        if not self._error_msg():
            destination = QFileDialog.getSaveFileName(filter="Image (*.jpg *.png)")[0]
            cv.imwrite(destination,self.tmp_image)

    def load(self):
        file_name = QFileDialog.getOpenFileName(None, "Open File", "/home", "Images (*.png *.xpm *.jpg)")[0]
        if file_name:
            self.graphic_area.setScaledContents(True)#sets image to fill the graphic area
            self.image = cv.imread(file_name, cv.IMREAD_GRAYSCALE)
            self._update_img(self.image)

    def rotate(self):
        if not self._error_msg():
            rotated_img = cv.rotate(self.tmp_image,cv.ROTATE_90_CLOCKWISE)
            self._update_img(rotated_img)
    def zoom_in(self):
        pass
    def zoom_out(self):
        pass
    def select_rect(self,rect):
        x1,y1,x2,y2=rect.getCoords()
        print(x1,y1,x2,y2)
        # print(self.image.shape)
        # print('selected rectangle',r)
    def select_custom(self):
        print('select_custom')
    def blur_avg_filter(self,params_dict):
        print(params_dict)
        # self._update_img(cv.blur(self.tmp_image,ksize=size,anchor=point))
        print('applying blur_avg_filter')
    def blur_bilateral_filter(self):
        self._update_img(cv.bilateralFilter(self.tmp_image,9,75,75))
        print('applying filter 1')
    def blur_gauss_filter(self):
        self._update_img(cv.GaussianBlur(self.tmp_image,(5,5),0))
        print('applying gauss filter')
    def blur_med_filter(self):
        self._update_img(cv.medianBlur(self.tmp_image,5))
        print('applying blur med filter')
    


