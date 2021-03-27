import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.uic import loadUi
from PhotoEdit_ui import Ui_MainWindow
from Image import Image
import urllib
"""
all libraries and necessery files should be imported above.
"""


class Window(QMainWindow, Ui_MainWindow):
    """
    This is class is responsible for handling UI events and basic gui operations.
    This class should be calling event handlers from other classes.
    Feel free to create necessary classes.
    """
    def __init__(self, parent=None):
        self.rotation = 0
        self.scaleFactor = 1.0
        super().__init__(parent)
        self.setupUi(self)
        self.connect_signals()

    def connect_signals(self):
        self.actionLoad.triggered.connect(self.load_handler)
        self.actionSave.triggered.connect(self.save_handler) # seems like a binding for the event
        self.actionRotate.triggered.connect(self.rotate_handler)
        self.actionZoomOut.triggered.connect(self.zoomOut)
        self.actionZoomIn.triggered.connect(self.zoomIn)


    def save_handler(self):
        destination = QFileDialog.getSaveFileName(filter="Image (*.jpg *.png)")[0]
        self.img.save(destination)


    def load_handler(self):
        print("load was called.")
        # QMessageBox.information(self, "Image Viewer", "Cannot load the image.")
        # this is pretty cool, we can easily display some info to the user
        fileName = QFileDialog.getOpenFileName(self, "Open File",
                                       "/home",
                                       "Images (*.png *.xpm *.jpg)")[0]
        self.pixmap = QtGui.QPixmap.fromImage(self.img.ui_image())
        self.graphicArea.setPixmap(self.pixmap)

    def rotate_handler(self):
        self.rotation += 90
        transform = QtGui.QTransform().rotate(self.rotation)
        rotated_pixmap = self.pixmap.transformed(transform,QtCore.Qt.TransformationMode.SmoothTransformation)
        self.graphicArea.setPixmap(rotated_pixmap)

    def zoomIn(self):
        self.scaleImage(1.25)

    def zoomOut(self):
        self.scaleImage(0.8)

    def scaleImage(self, factor):
        self.scaleFactor *= factor
        # to do 

    def normalSize(self):
        self.graphicArea.adjustSize()
        self.scaleFactor = 1.0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())