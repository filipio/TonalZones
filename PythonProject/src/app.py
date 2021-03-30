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

        # TO DO : connect appropriate methods
        # self.actionBlurAvg.triggered.connect()
        # self.actionBlurBilateral.triggered.connect()
        # self.actionBlurGauss.triggered.connect()
        # self.actionBlurMed.triggered.connect()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())