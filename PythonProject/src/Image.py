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
from Enums import *
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
    mask_saved = pyqtSignal(str)
    def __init__(self, graphic_area, default_mask_name):
        super().__init__(None)
        self.default_mask_name = default_mask_name
        self.image = np.empty(0)
        self.tmp_image = np.empty(0)
        self.thresholded_pixels = np.empty(0) 
        self.mask_belongings = np.empty(0)
        self.mask_copy=np.empty(0) # name should be changed
        self.graphic_area = graphic_area
        self.Bilateral=Bilateral()
        self.Avaraging=Avaraging(self.graphic_area)
        self.Gaussian=Gaussian(self.graphic_area)
        self.Median=Median()
        self.active_mask = None
        self.mask_index = -1
        self.masks = {}
        self.masks_mapping = {}
        self.history = []
        self.Otsu=Thresold()
        self.is_thresolded=False

    def _show_img(self, frame):
        """
        function to show image represented by the frame.
        """
        img_rep = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format.Format_RGB888)
        self.graphic_area.setPixmap(QtGui.QPixmap.fromImage(img_rep))

    def _update_img(self, img, save=True):
        """
        function to display and save new state of image.
        """
        if save:
            print("saving image to history.")
            self.history.append(self.tmp_image)
        self.tmp_image = img
        frame = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self._show_img(frame)


    def _empty_img_error(self):
        """
        function to check whether any image was loaded 
        and display appropriate message to user.
        """
        if self.tmp_image.size == 0: 
            msg_box = QMessageBox.about(self.graphic_area,"Error","Image needs to be loaded first.")
            return True
        return False

    def _ratio_to_img(self):
        """
        function to get the ratio between real image and screen image.
        """
        img_height = self.image.shape[0]
        img_width = self.image.shape[1]  
        return (img_width / self.graphic_area.width(), img_height / self.graphic_area.height())

    def _transform_pixel_to_img(self, index_x, index_y):
        """
        function to map pixel where user clicked on the screen-image to real image.
        """
        x_ratio , y_ratio = self._ratio_to_img()
        return (int(index_x * x_ratio), int(index_y * y_ratio))

    def _create_mask_img(self, rows, columns, color):
        """
        function to create what needs to be displayed based on parameters:
        rows and columns contain indexes where pixel of given color should be placed.
        The rest of pixels are the same as in current image.
        """
        mask_img = cv.cvtColor(self.tmp_image, cv.COLOR_GRAY2RGB)
        mask_img[rows, columns, :] = 0
        mask_img[rows, columns, color] = MaskColor.FILL
        return mask_img

    def _get_mask(self, m_id):
        """
        function to get mask by it's id.
        """
        return self.masks.get(self.masks_mapping.get(m_id))

    def _update_masks_data(self, prev_mask_values):
        """
        function which saves information about pixels that current mask owns.
        If current mask is in read-state, every pixel that which belonged to some mask (prev_owner_mask)
        and now belongs to current mask changes its owner. User is notified if such event takes place.
        """
        if self.active_mask.is_read and self.active_mask.saved:
            active_mask_values = self.active_mask.get(self.tmp_image, self.mask_belongings, self.thresholded_pixels)
            to_remove_rows, to_remove_columns = np.where((prev_mask_values == True) & (active_mask_values == False))
            self.mask_belongings[to_remove_rows, to_remove_columns] = MaskBelonging.NONE
            occupied_rows, occupied_columns = np.where((active_mask_values == True) & (self.mask_belongings != self.active_mask.id) & (self.mask_belongings >= 0)) 
            if len(occupied_rows) > 0:
                QMessageBox.information(self.graphic_area, "Masks modified",
                 "Your modification will remove some pixels from other masks.")
            for i in range(len(occupied_rows)):
                prev_owner_mask = self._get_mask(self.mask_belongings[occupied_rows[i], occupied_columns[i]])
                assert prev_owner_mask.id == self.mask_belongings[occupied_rows[i], occupied_columns[i]]
                prev_owner_mask.remove(occupied_rows[i], occupied_columns[i])
            self.mask_belongings[active_mask_values] = self.active_mask.id
            self._update_all_masks()

    def _update_all_masks(self):
        for key, value in self.masks.items():
            if key != self.default_mask_name:
                self.mask_belongings[value.get(self.tmp_image, self.mask_belongings, self.thresholded_pixels)] = value.id


    def undo(self): # may occur some pitfalls with it
        """
        ctrl + z mechanism.
        """
        try:
            last_image = self.history.pop()
            self._update_img(last_image, save=False)
        except IndexError:
            print("TO DO : HANDLE INDEX ERROR")

    def save(self):
        """
        function to save current image. If not every pixel was thresholded, question
        occurs whether user wants to continue.
        """
        if not self._empty_img_error():
            if not np.all(self.thresholded_pixels):
                reply = QMessageBox.question(self.graphic_area, "Work not finished", "Are you sure you want to quit ? Some pixels haven't been thresholded yet.")
                if reply == QMessageBox.Yes:
                    destination = QFileDialog.getSaveFileName(filter="Image (*.jpg *.png)")[0]
                    cv.imwrite(destination,self.tmp_image)        
            else:
                destination = QFileDialog.getSaveFileName(filter="Image (*.jpg *.png)")[0]
                cv.imwrite(destination,self.tmp_image)

    def load(self):
        """
        function to load an image from destination and reset some Image object values
        """
        file_name = QFileDialog.getOpenFileName(None, "Open File", "/home", "Images (*.png *.xpm *.jpg)")[0]
        if file_name:
            self.graphic_area.setScaledContents(True)
            self.image = cv.imread(file_name, cv.IMREAD_GRAYSCALE)
            self.thresholded_pixels = np.full((self.image.shape[0], self.image.shape[1]), False, dtype=bool)
            self.mask_belongings = np.full((self.image.shape[0], self.image.shape[1]), MaskBelonging.NONE, dtype=int)
            self.tmp_image = self.image
            self._update_img(self.image)
            if not self.masks:
                self.new_mask()
            else:
                self._update_all_masks()
                self.show_curr_mask()
            # was call to new here
            self.img_loaded.emit()


    def show_curr_mask(self, modified = True):
        """
        function to show the current mask = last that was applied
        """
        print("show_curr_mask called.")
        red_rows, red_columns = np.where(self.active_mask.get(self.tmp_image, self.mask_belongings, self.thresholded_pixels, modified) == False)
        mask_img = self._create_mask_img(red_rows, red_columns, MaskColor.RED)
        self._show_img(mask_img)

    def show_curr_img(self):
        """
        function to show curr img
        """
        frame = cv.cvtColor(self.tmp_image, cv.COLOR_BGR2RGB)
        self._show_img(frame)

    def save_mask(self, name):
        """
        function to save curr mask as a given name. If the name was provided before, warning occurs.
        """
        print("save_mask()")
        if name in self.masks.keys():
            QMessageBox.warning(self.graphic_area,"Error","Mask with such name already exist.")
        else:
            self.mask_belongings[self.active_mask.get(self.tmp_image, self.mask_belongings, self.thresholded_pixels)] = self.active_mask.id
            self.masks_mapping[self.active_mask.id] = name
            self.masks[name] = self.active_mask
            self.active_mask.saved = True
            self.mask_saved.emit(name)
            print("mask was saved.")
            
            
 
    def new_mask(self):
        """
        function to create a new mask.
        """
        self.mask_index += 1
        if self.active_mask:
            self.active_mask.is_read = False
        self.active_mask = Mask(self.image.shape[0], self.image.shape[1], self.mask_index)
        self.masks[self.default_mask_name] = self.active_mask
        # self.masks_mapping[self.active_mask.id] = self.default_mask_name
        self.mask_loaded.emit(self.active_mask)
        self.show_curr_img()

    def load_mask(self, name):
        """
        function to load mask given by name. Some values are reset in case new image was loaded.
        """
        print("load_mask()")
        self.active_mask.is_read = False
        self.active_mask = self.masks.get(name)
        self.active_mask.loaded_handler()
        self.mask_loaded.emit(self.active_mask)
        self.show_curr_mask()
        if(not self.active_mask.new):
            self.active_mask.is_read = True
        

    def delete_mask(self, name):
        self.mask_belongings[self.active_mask.get(modified=False)] = MaskBelonging.NONE
        self.masks.pop(name)
        self.masks_mapping.pop(self.active_mask.id)
        self._update_all_masks()


    def pop_mask_pixel(self):
        """
        function to pop a pixel from a current mask pixel list.
        """
        prev_mask = self.active_mask.get(modified=False)
        self.active_mask.pop_pixel()
        self.apply_mask(prev_mask)
    
    def update_mask_pixel_tol(self, value):
        """
        function to update pixel tolerance in current mask.
        """
        prev_mask = self.active_mask.get(modified=False)
        self.active_mask.update_pixel_tol(value)
        self.apply_mask(prev_mask)

    def update_slider_mask(self, s_min, s_max, s_tol):
        prev_mask = self.active_mask.get(modified=False)
        self.active_mask.update_slider_mask(s_min, s_max, s_tol)
        self.apply_mask(prev_mask)

    def not_thresholded_handler(self):
        """
        function to show which pixels haven't been thresholded yet.
        """
        blue_x, blue_y = np.where(self.thresholded_pixels == False)
        mask_img = self._create_mask_img(blue_x, blue_y, MaskColor.BLUE)
        self._show_img(mask_img)



    def apply_mask(self, previous_mask):
        self._update_masks_data(previous_mask)
        self.show_curr_mask()


    def pixel_clicked_handler(self, x, y):
        """
        function to add pixel to current mask pixel list.
        """
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
        """
            method to apply averaging filter, all methods in this class
            ending with _filter are used to apply filters indicatated by method name.
        """
        self._update_img(self.Avaraging.apply(self.tmp_image))
    
    def blur_bilateral_filter(self,params_dict):
        self._update_img(self.Bilateral.apply(self.tmp_image))
    
    def blur_gauss_filter(self,params_dict):
        self._update_img(self.Gaussian.apply(self.tmp_image))
    
    def blur_med_filter(self,params_dict):
        # print('is image None? : ',self.tmp_image==None)
        self._update_img(self.Median.apply(self.tmp_image))
    
    def apply_otsu(self):
        """
            method to find and apply to image lookup otsu thresolding
        """
        if self.is_thresolded == False:
            self.mask_copy=np.copy(self.tmp_image)
            self.is_thresolded=True
            indexes_to_thr=np.where(self.active_mask.get(modified=False))
            img_to_thr=self.mask_copy[indexes_to_thr]
            otsu_res,ret=self.Otsu.apply_otsu(img_to_thr)
            self.tmp_image[tuple((indexes_to_thr))]=otsu_res.flatten()
            self._update_img(self.tmp_image)
            self.thresh_val_calc.emit(ret)
    
    def apply_thres(self):
        """
            Function to apply changes made by moving and realising slider
            TODO: architecture here can be better :)(
        """
        if self.is_thresolded == False:
            self.is_thresolded=True
            self.mask_copy=np.copy(self.tmp_image)
        indexes_to_thr=np.where(self.active_mask.get(modified=False))
        img_to_thr=self.mask_copy[indexes_to_thr]
        otsu_res=self.Otsu.apply(img_to_thr)
        self.thresholded_pixels[tuple((indexes_to_thr))] = True
        self.tmp_image[tuple((indexes_to_thr))]=otsu_res.flatten()
        self._update_img(self.tmp_image)

    def apply_thres_by_button(self):
        """
            apply thresold using apply button.
            After this operation it is not possible to
            remove applied changes
        """
        if self.is_thresolded == False:
            self.is_thresolded=True
        self.mask_copy=np.copy(self.tmp_image)
        indexes_to_thr=np.where(self.active_mask.get(modified=False))
        img_to_thr=self.mask_copy[indexes_to_thr]
        otsu_res=self.Otsu.apply(img_to_thr)
        self.thresholded_pixels[tuple((indexes_to_thr))] = True
        self.tmp_image[tuple((indexes_to_thr))]=otsu_res.flatten()
        self._update_img(self.tmp_image)
    
    def remove_threshold(self):
        """
            remove visible changes on image.
            Set slider of thresolding to 0
        """
        # send signal to set slider to 0
        self.thresh_val_calc.emit(0)
        self._update_img(self.mask_copy)
        self.is_thresolded=False

