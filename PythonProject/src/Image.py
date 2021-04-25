import cv2 as cv
from PyQt5.QtGui import QImage
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (QFileDialog,QMessageBox, QComboBox)
from PyQt5.QtWidgets import QPushButton
import numpy as np
from Bilateral import Bilateral
from Avaraging import Avaraging
from Gaussian import Gaussian
from Median import Median
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject
from Color import MaskColor

class Image(QObject):
    """
    Image is a class responsible for doing operations on an image. Class should be initialized when
    new image from file is required. Every operation that is operating on an image should be contained
    in this class.
    Insert necessery methods below.
    """
    mask_range_changed = pyqtSignal(int, int)
    img_loaded = pyqtSignal()

    def __init__(self, graphic_area):
        super().__init__(None)
        self.image = np.empty(0)
        self.tmp_image = np.empty(0)
        self.active_img = np.empty(0)
        self.thresholded_pixels = np.empty(0)
        self.graphic_area = graphic_area
        self.active_img=np.empty(0)#active part of image that will be edited
        self.Bilateral=Bilateral()
        self.Avaraging=Avaraging(self.graphic_area)
        self.Gaussian=Gaussian(self.graphic_area)
        self.Median=Median()
        self.mask_min = None
        self.mask_max = None
        self.mask_tol = 0

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

    def _ratio_to_img(self):
        img_height = self.image.shape[0]
        img_width = self.image.shape[1]  
        return (img_width / self.graphic_area.width(), img_height / self.graphic_area.height())

    def _transform_pixel_to_img(self, index_x, index_y):
        x_ratio , y_ratio = self._ratio_to_img()
        return (int(index_x * x_ratio), int(index_y * y_ratio))

    def _transform_pixels_to_display(self, indexes_x, indexes_y):
        x_ratio , y_ratio = self._ratio_to_img()
        display_x = [int(indexes_x[i] / x_ratio) for i in range(len(indexes_x))]
        display_y = [int(indexes_y[i] / y_ratio) for i in range(len(indexes_y))]
        return list(zip(display_x, display_y))

    def save(self):
        if not self._error_msg():
            destination = QFileDialog.getSaveFileName(filter="Image (*.jpg *.png)")[0]
            cv.imwrite(destination,self.tmp_image)

    def load(self):
        file_name = QFileDialog.getOpenFileName(None, "Open File", "/home", "Images (*.png *.xpm *.jpg)")[0]
        if file_name:
            self.graphic_area.setScaledContents(True)#sets image to fill the graphic area
            self.image = cv.imread(file_name, cv.IMREAD_GRAYSCALE)
            self.thresholded_pixels = np.full((self.image.shape[0], self.image.shape[1]), False, dtype=bool)
            self._update_img(self.image)
            self.img_loaded.emit()

    def rotate(self):
        if not self._error_msg():
            rotated_img = cv.rotate(self.tmp_image,cv.ROTATE_90_CLOCKWISE)
            self._update_img(rotated_img)
 
    def activate_mask(self):
        indexes= np.where(self.active_img == True)
        indexes = self._transform_pixels_to_display(indexes[1], indexes[0])
        self.graphic_area.apply_mask(indexes)


    def update_mask(self, m_min, m_max, m_tol):
        self.mask_min = m_min
        self.mask_max = m_max
        self.mask_tol = m_tol
        if m_min is not None and m_max is not None:
            self.mask_range_changed.emit(self.mask_min, self.mask_max)
            self.active_img = (self.mask_min - self.mask_tol <= self.tmp_image) & (
            self.tmp_image <= self.mask_max + self.mask_tol) & (
            self.thresholded_pixels == False)

            indexes = np.where(self.active_img == True)
            indexes = self._transform_pixels_to_display(indexes[1], indexes[0])
            self.graphic_area.show_mask(indexes, MaskColor.RED)

    def not_thresholded_handler(self):
        indexes = np.where(self.thresholded_pixels == False)
        indexes = self._transform_pixels_to_display(indexes[1], indexes[0])
        self.graphic_area.show_mask(indexes, MaskColor.BLUE)

    def pixel_clicked_handler(self, x, y):
        img_x, img_y = self._transform_pixel_to_img(x, y)
        grey_value = self.image[img_x][img_y]
        new_mask_min = self.mask_min
        new_mask_max = self.mask_max
        if self.mask_min is None or grey_value < self.mask_min:
            new_mask_min = grey_value
        if self.mask_max is None or grey_value > self.mask_max:
            new_mask_max = grey_value
        self.update_mask(new_mask_min, new_mask_max, self.mask_tol)

    def select_rect(self,rect):
        x1,y1,x2,y2=rect.getCoords()
        print(x1,y1,x2,y2)

        print("shape : ",self.image.shape)
        # print('selected rectangle',r)
    def select_custom(self):
        print('select_custom')
    def blur_avg_filter(self,params_dict):
        self._update_img(self.Avaraging.apply(self.tmp_image))
    def blur_bilateral_filter(self,params_dict):
        self._update_img(self.Bilateral.apply(self.tmp_image))
    def blur_gauss_filter(self,params_dict):
        self._update_img(self.Gaussian.apply(self.tmp_image))
    def blur_med_filter(self,params_dict):
        print('is image None? : ',self.tmp_image==None)
        self._update_img(self.Median.apply(self.tmp_image))
    


