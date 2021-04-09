from PyQt5.QtCore import (Qt, pyqtSignal,QRect,QPoint,QSize)
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QRubberBand
class Label(QtWidgets.QLabel):
    rectChanged = pyqtSignal(QRect)
    def __init__(self, *args, **kwargs):
        QtWidgets.QLabel.__init__(self, *args, **kwargs)
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.setMouseTracking(True)
        self.origin = QPoint()
        self.changeRubberBand = False
        self.selection_active = False
    def mousePressEvent(self, event):
        """if mouse left button is pressed start selecting
           if it's pressed again delete selection
        """
        if event.button()==Qt.LeftButton:
            self.selection_active=True
            self.origin = event.pos()
            self.rubberBand.setGeometry(QRect(self.origin, QSize()))
            self.rectChanged.emit(self.rubberBand.geometry())
            self.rubberBand.show()
            self.changeRubberBand = True
        QtWidgets.QLabel.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        """when mouse is moved update selection shape"""
        if self.changeRubberBand:
            self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())
        QtWidgets.QLabel.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        """if mouse is reales emit signal with selection shape"""
        self.changeRubberBand = False
        if self.selection_active==True:
            self.rectChanged.emit(self.rubberBand.geometry())
            self.selection_active=False
        QtWidgets.QLabel.mouseReleaseEvent(self, event)
