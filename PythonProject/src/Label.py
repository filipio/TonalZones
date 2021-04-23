from PyQt5.QtCore import (Qt, pyqtSignal,QRect,QPoint,QSize)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QObject
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtWidgets import QRubberBand
from Color import MaskColor
class Label(QtWidgets.QLabel):
    rect_change = pyqtSignal(QRect)
    pixel_clicked = pyqtSignal(int, int)
    

    def __init__(self, *args, **kwargs):        
        QtWidgets.QLabel.__init__(self, *args, **kwargs)
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.pixel_selections = []
        self.setMouseTracking(True)
        self.origin = QPoint()
        self.changeRubberBand = False
        self.rect_selection_active = False
        self.mouse_selection_active = False
        self.indexes = []
        self.active_indexes = []
        self.mask_color = QColor(255, 0, 0, 60)

    def activate_rect_selection(self):
        self.rect_selection_active = True

    def activate_mouse_selection(self):
        self.mouse_selection_active = True
        QApplication.setOverrideCursor(Qt.CursorShape.CrossCursor)


    def mousePressEvent(self, event):
        """if mouse left button is pressed start selecting
           if it's pressed again delete selection
        """
        if event.button()==Qt.LeftButton:
            if self.rect_selection_active:
                self.origin = event.pos()
                self.rubberBand.setGeometry(QRect(self.origin, QSize()))
                self.rect_change.emit(self.rubberBand.geometry())
                self.rubberBand.show()
                self.changeRubberBand = True
            elif self.mouse_selection_active:
                x = event.pos().x()
                y = event.pos().y()
                self.pixel_clicked.emit(x,y)
                print("pixel_clicked signal was emitted")

        QtWidgets.QLabel.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        """when mouse is moved update selection shape"""
        if self.changeRubberBand:
            self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())
        QtWidgets.QLabel.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        """if mouse is reales emit signal with selection shape"""
        self.changeRubberBand = False
        if self.rect_selection_active==True:
            self.rect_change.emit(self.rubberBand.geometry())
            self.rect_selection_active=False
        QtWidgets.QLabel.mouseReleaseEvent(self, event)

    def paintEvent(self, event):
        size = 3
        QtWidgets.QLabel.paintEvent(self,event)
        print("paint event was called")
        if self.indexes:
            painter = QPainter(self)
            painter.setPen(QPen(self.mask_color, 2, Qt.SolidLine))
            painter.setBrush(QBrush(self.mask_color, Qt.SolidPattern))
            for i in range(len(self.indexes)):
                painter.drawEllipse(QPoint(self.indexes[i][0], self.indexes[i][1]), size, size)
                # rect = QRect(self.indexes[i][0] - size/2, self.indexes[i][1] - size/2, size, size)
                # painter.drawRect(rect) 
            painter.end()       
        
    def show_active_mask(self):
        self.show_mask(self.active_indexes, MaskColor.GREEN)

    def show_mask(self, indexes, color):
        self.indexes = indexes
        if color == MaskColor.RED:
            self.mask_color = QColor(255, 0, 0, 60)
        elif color == MaskColor.GREEN:
            self.mask_color = QColor(64, 224, 43, 120)
        elif color == MaskColor.BLUE:
            self.mask_color = QColor(62, 118, 235, 120)
        print("show mask was called")
        self.update()

    def hide_mask(self):
        self.indexes = []
        self.update()