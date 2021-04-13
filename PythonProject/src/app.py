import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.uic import loadUi
from Image import Image
from UI import UI
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
        self.connect_signals()

    def connect_signals(self):
        self.actionLoad.triggered.connect(self.image.load)
        self.actionSave.triggered.connect(self.image.save)
        self.actionRotate.triggered.connect(self.image.rotate)

        #filter methods connection
        self.actionBlurAvg.triggered.connect(self.image.blur_avg_filter)
        self.actionBlurBilateral.triggered.connect(self.image.blur_bilateral_filter)
        self.actionBlurGauss.triggered.connect(self.image.blur_gauss_filter)
        self.actionBlurMed.triggered.connect(self.image.blur_med_filter)
        #select methods connection
        self.actionSelectionRectangular.triggered.connect(self.image.select_rect)
        self.actionSelectionCustom.triggered.connect(self.image.select_custom)
        self.graphicArea.rectChanged.connect(self.image.select_rect)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())