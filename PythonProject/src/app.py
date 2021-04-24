import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.uic import loadUi
from Image import Image
from UI import UI
from functools import partial
from FiltersEnum import Filter
from ParamsFactory import ParamsFactory

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
        self.params_f=ParamsFactory(self)
        self.connect_signals()
    def connect_signals(self):
        self.actionLoad.triggered.connect(self.image.load)
        self.actionSave.triggered.connect(self.image.save)
        self.actionRotate.triggered.connect(self.image.rotate)

        #filter methods connection
        self.actionAvaraging.triggered.connect(partial(self.image.blur_avg_filter,self.params_f.get_fparams(Filter.AVARAGING)))
        self.actionBilateral.triggered.connect(self.image.blur_bilateral_filter)
        self.actionGaussian.triggered.connect(self.image.blur_gauss_filter)
        self.actionMedian.triggered.connect(self.image.blur_med_filter)
        #select methods connection
        self.actionRect.triggered.connect(self.graphicArea.switch_rect_selection)
        # self.actionSelectionCustom.triggered.connect(self.image.select_custom)
        self.graphicArea.rect_change.connect(self.image.select_rect)
        
        self._connect_mask()
        

        
        
    def _connect_mask(self):

        #mask sliders
        mask_update = lambda : self.image.update_mask(self.min_slider.value(), self.max_slider.value(), self.tolerance_slider.value())
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
        self.image.mask_range_changed.connect(lambda x, y : self.active_mask_btn.setEnabled(False))
        self.image.mask_range_changed.connect(self.params_f.set_mask_params)
        self.image.img_loaded.connect(lambda : self.not_thresholded_btn.setEnabled(True))
        self.graphicArea.pixel_clicked.connect(self.image.pixel_clicked_handler)

        #mask buttons
        self.hide_mask_btn.clicked.connect(self.graphicArea.hide_mask)
        self.active_mask_btn.clicked.connect(self.graphicArea.show_active_mask)
        self.not_thresholded_btn.clicked.connect(self.image.not_thresholded_handler)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())