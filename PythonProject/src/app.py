import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.uic import loadUi
from Image import Image
from UI import UI
from functools import partial
from FiltersEnum import Filter
from ParamsFactory import ParamsFactory
from PixelList import PixelList

"""
all libraries and necessery files should be imported above.
"""


class Window(QMainWindow, UI):
    """
    This is class is responsible for handling UI events and basic gui operations.
    This class should be calling event handlers from other classes.
    Feel free to create necessary classes.
    """
    def __init__(self, parent=None):

        super().__init__(parent)
        
        self.setupUi(self)
        self.image = Image(self.graphicArea)
        self.pixel_list_operator = PixelList(self.pixel_list)
        self.params_f=ParamsFactory(self)
        self.connect_signals()
    def connect_signals(self):
        self.actionLoad.triggered.connect(self.image.load)
        self.actionSave.triggered.connect(self.image.save)

        #filter methods connection
        self.actionAvaraging.triggered.connect(self.image.blur_avg_filter)
        self.actionBilateral.triggered.connect(self.image.blur_bilateral_filter)
        self.actionGaussian.triggered.connect(self.image.blur_gauss_filter)
        self.actionMedian.triggered.connect(self.image.blur_med_filter)
        #select methods connection
        self.actionRect.triggered.connect(self.image.select_rect)
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
        # self.actionSelectionCustom.triggered.connect(self.image.select_custom)
        self.graphicArea.rect_change.connect(self.image.select_rect)
    
        self.actionRect.triggered.connect(self.graphicArea.switch_rect_selection)
        # self.actionSelectionCustom.triggered.connect(self.image.select_custom)
        self.graphicArea.rect_change.connect(self.image.select_rect)
        # thresold settings
        # slider value changes is here
        self.threshold_slider.valueChanged.connect(self.image.Otsu.set_thres_val)
        self.threshold_slider.sliderReleased.connect(self.image.apply_thres)
        self.threshold_combobox.currentIndexChanged.connect(self.image.Otsu.set_type1)
        self.otsu_button.clicked.connect(self.image.apply_otsu)
        self.apply_threshold_button.clicked.connect(self.image.apply_thres)
        self.remove_threshold_button.clicked.connect(self.image.remove_threshold)
        self.action_undo.triggered.connect(self.image.undo)
        
        self._connect_mask()
        self.remove_last_btn.clicked.connect(self.pixel_list_operator.remove_last)
        self.remove_last_btn.clicked.connect(self.image.pop_mask_pixel)
        self.remove_last_btn.clicked.connect(self.graphicArea.pop_last_pixel)
        self.slider_pixel_tol.sliderReleased.connect(lambda : self.image.update_mask_pixel_tol(self.slider_pixel_tol.value()))
        self.image.pixel_selected.connect(self.pixel_list_operator.add_element)
        self.image.thresh_val_calc.connect(self.threshold_slider.setValue)
        # self.remove_all_test.clicked.connect(lambda : )
        
        
    def _connect_mask(self):

        #mask sliders
        mask_update = lambda : self.image.apply_slider_mask(self.min_slider.value(), self.max_slider.value(), self.tolerance_slider.value())
        self.min_slider.sliderReleased.connect(mask_update)
        self.max_slider.sliderReleased.connect(mask_update)
        self.tolerance_slider.sliderReleased.connect(mask_update)

        # mask actions
        self.action_apply_mask.triggered.connect(self.image.activate_mask)
        self.action_apply_mask.triggered.connect(lambda : self.active_mask_btn.setEnabled(True))
        # TO DO : enable thresholding if mask was applied
        # self.action_apply_mask.triggered.connect(<enable_thresholding_method>)
        self.action_select_from_settings.triggered.connect(lambda : self.Settings.setCurrentIndex(1)) # show settings menu
        self.action_select_from_image.triggered.connect(self.graphicArea.switch_mouse_selection)
        
        #mask img signals
        # self.image.mask_range_changed.connect(lambda : self.active_mask_btn.setEnabled(False))
        self.image.img_loaded.connect(lambda : self.not_thresholded_btn.setEnabled(True))
        self.graphicArea.pixel_mode_entered.connect(self.image.show_curr_img)
        self.graphicArea.pixel_mode_left.connect(self.image.apply_pixel_mask)
        self.graphicArea.pixel_clicked.connect(self.image.pixel_clicked_handler)

        #mask buttons
        self.hide_mask_btn.clicked.connect(self.graphicArea.hide_mask)
        self.active_mask_btn.clicked.connect(self.graphicArea.show_active_mask)
        self.not_thresholded_btn.clicked.connect(self.image.not_thresholded_handler)
        

        # self.graphicArea.pixel_mode_entered.connect(self.image.show)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())