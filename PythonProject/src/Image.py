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
from Mask import Mask
from Thresold import Thresold
class Image(QObject):
    """
    Image is a class responsible for doing operations on an image. Class should be initialized when
    new image from file is required. Every operation that is operating on an image should be contained
    in this class.
    Insert necessery methods below.
    """
    mask_range_changed = pyqtSignal()
    pixel_selected = pyqtSignal(int)
    img_loaded = pyqtSignal()
    thresh_val_calc=pyqtSignal(int)
    def __init__(self, graphic_area):
        super().__init__(None)
        self.image = np.empty(0)
        self.tmp_image = np.empty(0)
        self.active_img = np.empty(0)
        self.thresholded_pixels = np.empty(0)
        self.mask_copy=np.empty(0) # name should be changed
        self.graphic_area = graphic_area
        self.active_img=np.empty(0)#active part of image that will be edited
        self.Bilateral=Bilateral()
        self.Avaraging=Avaraging(self.graphic_area)
        self.Gaussian=Gaussian(self.graphic_area)
        self.Median=Median()
        self.active_mask = None
        self.history = []
        self.Otsu=Thresold()
        self.is_thresolded=False

    def _show_img(self, frame):
        print("show img shape : ",frame.shape)
        img_rep = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format.Format_RGB888)
        self.graphic_area.setPixmap(QtGui.QPixmap.fromImage(img_rep))

    def _update_img(self, img, save=True):
        if save:
            print("saving image to history.")
            self.history.append(self.tmp_image)
        self.tmp_image = img
        frame = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self._show_img(frame)


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
        return (indexes_x // x_ratio, indexes_y // y_ratio)

    def _send_changed_mask_data(self):
        red_x, red_y = np.where(self.active_img == False)
        display_img = cv.cvtColor(self.tmp_image, cv.COLOR_GRAY2RGB)
        display_img[red_x,red_y,0] = 255
        display_img[red_x,red_y,1] = 0
        display_img[red_x,red_y,2] = 0
        self._show_img(display_img)
        # print("display img shape : ", display_img.shape)
        # red_indexes = np.where(self.active_img == False)
        # img_copy = np.copy(self.tmp_image)
        # indexes_x, indexes_y = self._transform_pixels_to_display(indexes[1], indexes[0])
        # self.graphic_area.show_mask(indexes_x, indexes_y, MaskColor.RED)

    def show_curr_img(self):
        frame = cv.cvtColor(self.tmp_image, cv.COLOR_BGR2RGB)
        self._show_img(frame)


    def undo(self):
        try:
            last_image = self.history.pop()
            self._update_img(last_image, save=False)
        except IndexError:
            print("TO DO : HANDLE INDEX ERROR")

# TO DO : save/ load to another class
    def save(self):
        if not self._error_msg():
            destination = QFileDialog.getSaveFileName(filter="Image (*.jpg *.png)")[0]
            cv.imwrite(destination,self.tmp_image)

    def load(self):
        file_name = QFileDialog.getOpenFileName(None, "Open File", "/home", "Images (*.png *.xpm *.jpg)")[0]
        if file_name:
            self.graphic_area.setScaledContents(True)#sets image to fill the graphic area
            self.image = cv.imread(file_name, cv.IMREAD_GRAYSCALE)
            self.thresholded_pixels = np.full((self.image.shape[0], self.image.shape[1]), -1, dtype=int)
            self.active_mask = Mask(self.image.shape[0], self.image.shape[1])
            self.tmp_image = self.image
            self._update_img(self.image)
            self.img_loaded.emit()
 
    def pop_mask_pixel(self):
        self.active_mask.pop_pixel()
        self.apply_pixel_mask()
    
    def update_mask_pixel_tol(self, value): # will call Mask method
        self.active_mask.update_pixel_tol(value)
        self.apply_pixel_mask()

    def activate_mask(self):
        indexes = np.where(self.active_img == True)
        indexes_x, indexes_y = self._transform_pixels_to_display(indexes[1], indexes[0])
        self.graphic_area.apply_mask(indexes_x, indexes_y)

    def not_thresholded_handler(self):
        indexes = np.where(self.thresholded_pixels == -1)
        indexes_x, indexes_y = self._transform_pixels_to_display(indexes[1], indexes[0])
        self.graphic_area.show_mask(indexes_x, indexes_y, MaskColor.BLUE)

    def apply_slider_mask(self, s_min, s_max, s_tol): # will 
        self.active_img = self.active_mask.slider_mask(s_min, s_max, s_tol, self.tmp_image, self.thresholded_pixels)
        self._send_changed_mask_data()
        # self.mask_range_changed.emit()

    def apply_pixel_mask(self):
        self.active_img =  self.active_mask.pixel_mask(self.tmp_image, self.thresholded_pixels)
        self._send_changed_mask_data()

    def pixel_clicked_handler(self, x, y):
        img_x, img_y = self._transform_pixel_to_img(x, y)
        # self.graphic_area.draw_pixel(img_x, img_y)
        grey_value = self.image[img_y][img_x]
        self.pixel_selected.emit(grey_value)
        self.active_mask.add_pixel(grey_value)
        # self.apply_pixel_mask()


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
    
    def apply_otsu(self):
    
        if self.is_thresolded == False:
            self.mask_copy=np.copy(self.tmp_image)
            self.is_thresolded=True
        indexes_to_thr=np.nonzero(self.active_img==True)
        img_to_thr=self.tmp_image[indexes_to_thr]
        otsu_res,ret=self.Otsu.apply_otsu(img_to_thr)
        self.tmp_image[tuple((indexes_to_thr))]=otsu_res.flatten()
        self._update_img(self.tmp_image)
        self.thresh_val_calc.emit(ret)
    
    def apply_thres(self):

        if self.is_thresolded == False:
            self.mask_copy=np.copy(self.tmp_image)
            self.is_thresolded=True
        
        indexes_to_thr=np.nonzero(self.active_img==True)
        img_to_thr=self.mask_copy[indexes_to_thr]
        otsu_res=self.Otsu.apply(img_to_thr)
        self.tmp_image[tuple((indexes_to_thr))]=otsu_res.flatten()
        self._update_img(self.tmp_image)
    
    def apply_to_img(self):
        self.mask_copy=self.tmp_image
        self.is_thresolded=False
        self.thre
    def remove_threshold(self):
        #TODO
        self._update_img(self.mask_copy)
        self.is_thresolded=False

