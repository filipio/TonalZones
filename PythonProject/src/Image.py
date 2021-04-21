import cv2 as cv
from PyQt5.QtGui import QImage
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (QFileDialog,QMessageBox, QComboBox)
from PyQt5.QtWidgets import QPushButton
import numpy as np
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject

class Image(QObject):
    """
    Image is a class responsible for doing operations on an image. Class should be initialized when
    new image from file is required. Every operation that is operating on an image should be contained
    in this class.
    Insert necessery methods below.
    """
    mask_range_changed = pyqtSignal(int, int)

    def __init__(self, graphic_area):
        super().__init__(None)
        self.image = np.empty(0)
        self.tmp_image = np.empty(0)
        self.graphic_area = graphic_area
        self.active_img=np.empty(0)#active part of image that will be edited
        self.mask_min = None
        self.mask_max = None
        self.mask_tol = None

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

    def _transform_to_img(self, x, y):
        img_height = self.image.shape[0]
        img_width = self.image.shape[1]
        x_ratio = img_width / self.graphic_area.width()
        y_ratio = img_height / self.graphic_area.height()
        return (int(x * x_ratio), int(y * y_ratio))

    def _transform_to_display(self, indexes):
        result = []
        x_ratio = self.graphic_area.width() / self.image.shape[1] 
        y_ratio = self.graphic_area.height() / self.image.shape[0]
        for i in range(len(indexes)):
            result.append((int(indexes[i][1] * x_ratio), int(indexes[i][0] * y_ratio)))
            
        return result

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

    def update_mask(self, m_min, m_max):
        self.mask_min = m_min
        self.mask_max = m_max
        print(f"updated values of mask are : {self.mask_min} and {self.mask_max}")
        if m_min is not None and m_max is not None:
            print("emitting signal to draw new mask")
            self.mask_range_changed.emit(self.mask_min, self.mask_max)
            self.active_img = self.tmp_image[(self.mask_min <= self.tmp_image) & (self.tmp_image <= self.mask_max)]
            # print("active img : ", self.active_img)
            indexes = np.where((self.mask_min <= self.tmp_image) & (self.tmp_image <= self.mask_max))
            indexes = list(zip(indexes[0], indexes[1]))
            indexes = self._transform_to_display(indexes)
            self.graphic_area.show_mask(indexes)


    def pixel_handler(self, x, y):
        print(f"pixel x : {x}, y : {y}")
        img_x, img_y = self._transform_to_img(x, y)
        print(f"img x : {img_x}, img_y : {img_y}")
        grey_value = self.image[img_x][img_y]
        print("grey value is :", grey_value)
        new_mask_min = self.mask_min
        new_mask_max = self.mask_max
        if self.mask_min is None or grey_value < self.mask_min:
            print(f"need to update value {self.mask_min} to {grey_value}")
            new_mask_min = grey_value
        if self.mask_max is None or grey_value > self.mask_max:
            print(f"need to update value {self.mask_max} to {grey_value}")
            new_mask_max = grey_value
        self.update_mask(new_mask_min, new_mask_max)

    def select_rect(self,rect):
        x1,y1,x2,y2=rect.getCoords()
        print(x1,y1,x2,y2)

        print("shape : ",self.image.shape)
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
    


