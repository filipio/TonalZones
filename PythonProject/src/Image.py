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
    pixel_selected = pyqtSignal(int)
    img_loaded = pyqtSignal()
    thresh_val_calc = pyqtSignal(int)
    mask_loaded = pyqtSignal(Mask)
    new_mask_sig = pyqtSignal()
    mask_saved = pyqtSignal(str)
    def __init__(self, graphic_area, default_mask_name):
        super().__init__(None)
        self.default_mask_name = default_mask_name
        self.image = np.empty(0)
        self.tmp_image = np.empty(0)
        self.thresholded_pixels = np.empty(0) 
        self.mask_belongings = np.empty(0) # arr to indicate which pixel belongs to which mask
        self.mask_copy=np.empty(0) # name should be changed
        self.graphic_area = graphic_area
        self.Bilateral=Bilateral()
        self.Avaraging=Avaraging(self.graphic_area)
        self.Gaussian=Gaussian(self.graphic_area)
        self.Median=Median()
        self.active_mask = None
        self.mask_index = -1 # for signing which pixel belongs to which mask
        self.masks = {}
        self.masks_mapping = {}
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

    def _create_display_img(self, rows, columns, color):
        display_img = cv.cvtColor(self.tmp_image, cv.COLOR_GRAY2RGB)
        display_img[rows, columns, :] = 0
        display_img[rows, columns, color] = MaskColor.FILL
        return display_img

    def _get_mask(self, m_id):
        return self.masks.get(self.masks_mapping.get(m_id))

    def _send_changed_mask_data(self, prev_mask):
        print("send_changed_mask_data")
        if self.active_mask.is_read:
            to_remove_rows, to_remove_columns = np.where((prev_mask == True) & (self.active_mask.get() == False))
            self.mask_belongings[to_remove_rows, to_remove_columns] = -1
            occupied_rows, occupied_columns = np.where((self.active_mask.get() == True) & (self.mask_belongings != self.active_mask.id) & (self.mask_belongings >= 0)) 
            print(f"found ", len(occupied_rows), "elements to change the mask.")
            for i in range(len(occupied_rows)):
                prev_owner_mask = self._get_mask(self.mask_belongings[occupied_rows[i], occupied_columns[i]])
                assert prev_owner_mask.id == self.mask_belongings[occupied_rows[i], occupied_columns[i]]
                prev_owner_mask.remove(occupied_rows[i], occupied_columns[i])
            self.mask_belongings[occupied_rows, occupied_columns] = self.active_mask.id
        
        # self.thresholded_pixels[np.where(self.active_mask.get() == True)] = self.active_mask.id
        red_rows, red_columns = np.where(self.active_mask.get() == False)
        display_img = self._create_display_img(red_rows, red_columns, MaskColor.RED)
        self._show_img(display_img)

    def show_curr_img(self):
        frame = cv.cvtColor(self.tmp_image, cv.COLOR_BGR2RGB)
        self._show_img(frame)


    def undo(self):
        try:
            last_image = self.history.pop()
            self._update_img(last_image, save=False)
        except IndexError:
            print("TO DO : HANDLE INDEX ERROR")

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
            self.mask_belongings = np.full((self.image.shape[0], self.image.shape[1]), -1, dtype=int)
            self.tmp_image = self.image
            self._update_img(self.image)
            self.new_mask()
            self.img_loaded.emit()
 
    def new_mask(self):
        print("new_mask()")
        self.mask_index += 1
        if(self.active_mask != None):
            self.active_mask.is_read = False
        self.active_mask = Mask(self.image.shape[0], self.image.shape[1], self.mask_index, self.mask_belongings, self.thresholded_pixels)
        self.masks[self.default_mask_name] = self.active_mask
        self.mask_loaded.emit(self.active_mask)
        self._send_changed_mask_data(None) # can fk up sth
        self.load_mask(self.default_mask_name)
        self.new_mask_sig.emit()

    def save_mask(self, name):
        print("save_mask()")
        if name in self.masks.keys():
            QMessageBox.warning(self.graphic_area,"Error","Mask with such name already exist.")
        else:
            self.mask_belongings[self.active_mask.get()] = self.active_mask.id
            self.masks_mapping[self.active_mask.id] = name
            assigned = len(np.where(self.mask_belongings >= 0)[0])
            print(f"assigned pixels to mask : {assigned}")
            self.masks[name] = self.active_mask
            self.mask_saved.emit(name)
    
    def load_mask(self, name):
        print("load mask()")
        self.active_mask.is_read = False
        loaded_mask = self.masks.get(name)
        self.active_mask = loaded_mask
        if not self.active_mask.is_new:
            print("not new mask")
            self.active_mask.is_read = True
        self.active_mask.height = self.image.shape[0]
        self.active_mask.width = self.image.shape[1]
        self.mask_loaded.emit(self.active_mask)
        self._send_changed_mask_data(None) # can fk up sth

    def pop_mask_pixel(self):
        self.active_mask.pop_pixel()
        self.apply_pixel_mask()
    
    def update_mask_pixel_tol(self, value): # will call Mask method
        self.active_mask.update_pixel_tol(value)
        self.apply_pixel_mask()

    def activate_mask(self):
        pass # does this method make any sense?
        # if it does, the active mask will be drawn in this class
        # indexes = np.where(self.active_mask.get() == False)

    def not_thresholded_handler(self):
        blue_x, blue_y = np.where(self.thresholded_pixels == False)
        display_img = self._create_display_img(blue_x, blue_y, MaskColor.BLUE)
        self._show_img(display_img)

    def apply_slider_mask(self, s_min, s_max, s_tol):
        previous_mask = self.active_mask.get()
        self.active_mask.slider_mask(s_min, s_max, s_tol, self.tmp_image, self.mask_belongings,self.thresholded_pixels)
        if np.where(previous_mask == True) == np.where(self.active_mask.get() == True):
            print("mask have the same true vales before and after apply")
        else :
            print("different mask values")
        self._send_changed_mask_data(previous_mask)
        # self.mask_range_changed.emit()

    def apply_pixel_mask(self):
        previous_mask = self.active_mask.get()
        self.active_mask.pixel_mask(self.tmp_image, self.mask_belongings, self.thresholded_pixels)
        if np.where(previous_mask == True) == np.where(self.active_mask.get() == True):
            print("mask have the same true vales before and after apply")
        self._send_changed_mask_data(previous_mask)

    def pixel_clicked_handler(self, x, y):
        img_x, img_y = self._transform_pixel_to_img(x, y)
        grey_value = self.image[img_y][img_x]
        self.pixel_selected.emit(grey_value)
        self.active_mask.add_pixel(grey_value)


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
        indexes_to_thr=np.nonzero(self.active_mask.get() == True)
        img_to_thr=self.tmp_image[indexes_to_thr]
        otsu_res,ret=self.Otsu.apply_otsu(img_to_thr)
        self.tmp_image[tuple((indexes_to_thr))]=otsu_res.flatten()
        self._update_img(self.tmp_image)
        self.thresh_val_calc.emit(ret)
    
    def apply_thres(self):

        if self.is_thresolded == False:
            self.mask_copy=np.copy(self.tmp_image)
            self.is_thresolded=True
        
        indexes_to_thr=np.nonzero(self.active_mask.get() == True)
        img_to_thr=self.mask_copy[indexes_to_thr]
        otsu_res=self.Otsu.apply(img_to_thr)
        self.thresholded_pixels[tuple((indexes_to_thr))] = True
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

