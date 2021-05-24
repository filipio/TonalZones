import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.uic import loadUi
from Image import Image
from UI import UI
from functools import partial
from FiltersEnum import Filter
from MaskViewController import MaskViewController
from PixelListView import PixelListView


# all libraries and necessery files should be imported above.



class Window(QMainWindow, UI):
    """
    This is class is responsible for handling UI events and basic gui operations.
    This class should be calling event handlers from other classes.
    Feel free to create necessary classes.
    """
    def __init__(self, parent=None):

        super().__init__(parent)
        
        self.setupUi(self)
        self.mask_deleted_indicator = 0
        default_mask_name = self.read_mask_c_box.currentText()
        self.image = Image(self.graphicArea, default_mask_name)
        self.pixel_list_view = PixelListView(self.pixel_list)
        self.params_f=MaskViewController(self)
        self.connect_signals()
    def connect_signals(self):
        self.actionLoad.triggered.connect(self.image.load)
        self.actionSave.triggered.connect(self.image.save)

        #filter methods connection
        self.actionAvaraging.triggered.connect(self.image.blur_avg_filter)
        self.actionBilateral.triggered.connect(self.image.blur_bilateral_filter)
        self.actionGaussian.triggered.connect(self.image.blur_gauss_filter)
        self.actionMedian.triggered.connect(self.image.blur_med_filter)
        #bileteral filter
        self.bilateral_diameter.valueChanged.connect(self.image.Bilateral.set_ksize)
        self.bilateral_sigma_color.valueChanged.connect(self.image.Bilateral.set_sigma_color)
        self.bilateral_sigma_space.valueChanged.connect(self.image.Bilateral.set_sigma_space)
        self.bilateral_border_type.currentIndexChanged.connect(self.image.Bilateral.set_border)
        #gaussian filter
        self.gauss_k_size_x.valueChanged.connect(self.image.Gaussian.set_ksize_x)
        self.gauss_k_size_y.valueChanged.connect(self.image.Gaussian.set_ksize_y)
        self.gauss_sigma_x.valueChanged.connect(self.image.Gaussian.set_sigma_x)
        self.gauss_sigma_y.valueChanged.connect(self.image.Gaussian.set_sigma_y)
        self.gauss_border_type.currentIndexChanged.connect(self.image.Gaussian.set_border)
        #median filter
        self.median_kernel_size.valueChanged.connect(self.image.Median.set_ksize)
        #avaraging
        self.avaraging_kernel_x.valueChanged.connect(self.image.Avaraging.set_ksize_x)
        self.avaraging_kernel_y.valueChanged.connect(self.image.Avaraging.set_ksize_y)
        self.avaraging_anchor_x.valueChanged.connect(self.image.Avaraging.set_anchor_x)
        self.avaraging_anchor_y.valueChanged.connect(self.image.Avaraging.set_anchor_y)
        self.avaraging_border_type_2.currentIndexChanged.connect(self.image.Avaraging.set_border)
    
        # thresold settings
        # slider value changes is here
        self.threshold_slider.valueChanged.connect(self.image.Otsu.set_thres_val)
        self.threshold_slider.sliderReleased.connect(self.image.apply_thres)
        self.threshold_combobox.currentIndexChanged.connect(self.image.Otsu.set_type1)
        self.otsu_button.clicked.connect(self.image.apply_otsu)
        self.apply_threshold_button.clicked.connect(self.image.apply_thres_by_button)
        self.remove_threshold_button.clicked.connect(self.image.remove_threshold)
        self.action_undo.triggered.connect(self.image.undo)
        
        self._connect_mask()
        self.remove_last_btn.clicked.connect(self.pixel_list_view.remove_last)
        self.remove_last_btn.clicked.connect(self.image.pop_mask_pixel)
        self.remove_last_btn.clicked.connect(self.graphicArea.pop_last_pixel)
        self.pixel_tolerance_slider.sliderReleased.connect(lambda : self.image.update_mask_pixel_tol(self.pixel_tolerance_slider.value()))
        self.image.pixel_selected.connect(self.pixel_list_view.add_element)
        self.image.thresh_val_calc.connect(self.threshold_slider.setValue)
        
        
    def _connect_mask(self):

        # #mask sliders
        mask_update = lambda : self.image.update_slider_mask(self.mask_min_slider.value(), self.mask_max_slider.value(), self.mask_tolerance_slider.value())
        self.mask_min_slider.sliderReleased.connect(mask_update)
        self.mask_max_slider.sliderReleased.connect(mask_update)
        self.mask_tolerance_slider.sliderReleased.connect(mask_update)

        # mask actions
        self.action_select_from_settings.triggered.connect(lambda : self.Settings.setCurrentIndex(1)) # show settings menu
        self.action_select_from_settings.triggered.connect(lambda : self.mask_tab_widget.setCurrentIndex(0))
        self.action_select_from_image.triggered.connect(self.graphicArea.enter_pixel_mode)
        
        #mask img signals
        self.image.img_loaded.connect(lambda : self.not_thresholded_btn.setEnabled(True))
        self.graphicArea.pixel_mode_entered.connect(self.image.show_curr_img)
        self.graphicArea.pixel_mode_entered.connect(lambda : self.Settings.setCurrentIndex(1))
        self.graphicArea.pixel_mode_entered.connect(lambda : self.mask_tab_widget.setCurrentIndex(1))
        self.graphicArea.pixel_mode_left.connect(lambda : self.image.update_mask_pixel_tol(self.pixel_tolerance_slider.value()))
        self.graphicArea.pixel_clicked.connect(self.image.pixel_clicked_handler)

        #mask buttons
        self.hide_mask_btn.clicked.connect(self.image.show_curr_img)
        self.show_mask_btn.clicked.connect(self.image.show_curr_mask)
        self.not_thresholded_btn.clicked.connect(self.image.not_thresholded_handler)
        self.new_mask_btn.clicked.connect(lambda : self.read_mask_c_box.setCurrentText(self.image.default_mask_name))
        self.new_mask_btn.clicked.connect(self.pixel_list_view.clear)
        self.new_mask_btn.clicked.connect(self.image.new_mask)
        self.new_mask_btn.clicked.connect(self.graphicArea.clear_pixels)
        self.save_mask_btn.clicked.connect(lambda : self.image.save_mask(self.mask_name_input.text()))
        self.delete_mask_btn.clicked.connect(lambda : self.image.delete_mask(self.read_mask_c_box.currentText()))
        def set_mask_deleted():
            self.mask_deleted_indicator = 2
        def set_combo_box_index(index):
            if self.mask_deleted_indicator:
                self.mask_deleted_indicator -=1
            else:
                self.read_mask_c_box.setCurrentIndex(index)
                self.thresh_read_mask_c_box.setCurrentIndex(index)

        #image signals
        self.image.mask_saved.connect(self.read_mask_c_box.addItem)
        self.image.mask_saved.connect(self.thresh_read_mask_c_box.addItem)
        self.image.mask_saved.connect(lambda value: self.mask_name_input.clear())
        self.image.mask_saved.connect(lambda : self.read_mask_c_box.setCurrentIndex(self.read_mask_c_box.count() - 1))
        self.image.mask_saved.connect(lambda : self.thresh_read_mask_c_box.setCurrentIndex(self.thresh_read_mask_c_box.count() - 1))
        self.image.mask_loaded.connect(self.pixel_list_view.load_from_mask)
        self.image.mask_loaded.connect(self.params_f.set_data_from_mask)

        self.delete_mask_btn.clicked.connect(lambda : set_mask_deleted())
        self.delete_mask_btn.clicked.connect(lambda : self.thresh_read_mask_c_box.removeItem(self.read_mask_c_box.currentIndex()))
        self.delete_mask_btn.clicked.connect(lambda : self.read_mask_c_box.removeItem(self.read_mask_c_box.currentIndex()))

        

        #combo boxes
        self.read_mask_c_box.currentIndexChanged.connect(lambda : self.delete_mask_btn.setEnabled(True) if self.read_mask_c_box.currentText() != self.image.default_mask_name else self.delete_mask_btn.setEnabled(False))
        self.read_mask_c_box.currentIndexChanged.connect(set_combo_box_index)
        self.read_mask_c_box.currentIndexChanged.connect(lambda : self.image.load_mask(self.read_mask_c_box.currentText()))
        self.thresh_read_mask_c_box.currentIndexChanged.connect(set_combo_box_index)
        
        




        


if __name__ == "__main__":
    """
        main moduleof this appp
    
    """
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())