from PyQt5.QtCore import (Qt, pyqtSignal,QRect,QPoint,QSize)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtWidgets import QRubberBand, QApplication
from Color import MaskColor

class Label(QtWidgets.QLabel):
    """
    This class is responsible for handling UI events such as :
    -select area
    -draw mask
    -select pixel for mask
    """
    rect_change = pyqtSignal(QRect)
    pixel_clicked = pyqtSignal(int, int)
    

    def __init__(self, *args, **kwargs):        
        QtWidgets.QLabel.__init__(self, *args, **kwargs)
        QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.pixel_selections = []
        self.setMouseTracking(True)
        self.origin = QPoint()
        self.changeRubberBand = False
        self.rect_selection_active = False
        self.mouse_selection_active = False
        self.indexes = []
        self.active_indexes = []
        self.mask_color = QColor(255, 0, 0, 60) # default color, here it's red
        self.draw_size = 3

    def switch_rect_selection(self):
        self.rect_selection_active = not self.rect_selection_active

    def switch_mouse_selection(self):
        self.mouse_selection_active = not self.mouse_selection_active
        if self.mouse_selection_active:
            QApplication.setOverrideCursor(Qt.CursorShape.CrossCursor)
        else:
            QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)


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

        QtWidgets.QLabel.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        """when mouse is moved update selection shape"""
        if self.changeRubberBand:
            self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())
        QtWidgets.QLabel.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        """if mouse is released emit proper signal for rect and pixel selection"""
        self.changeRubberBand = False
        if self.rect_selection_active==True:
            self.rect_change.emit(self.rubberBand.geometry())
            self.rect_selection_active=False
        elif self.mouse_selection_active:
            x = event.pos().x()
            y = event.pos().y()
            self.pixel_clicked.emit(x,y)
        QtWidgets.QLabel.mouseReleaseEvent(self, event)

    def paintEvent(self, event):
        QtWidgets.QLabel.paintEvent(self,event)
        if self.indexes:
            painter = QPainter(self)
            painter.setPen(QPen(self.mask_color, 2, Qt.SolidLine))
            painter.setBrush(QBrush(self.mask_color, Qt.SolidPattern))
            cursor = QApplication.overrideCursor()
            QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
            for i in range(len(self.indexes)):
                # could be replaced with rect
                painter.drawEllipse(QPoint(self.indexes[i][0], self.indexes[i][1]), self.draw_size, self.draw_size) 
            painter.end()
            QApplication.setOverrideCursor(cursor)       
        
    def show_active_mask(self):
        self.show_mask(self.active_indexes, MaskColor.GREEN)

    def apply_mask(self, active_indexes):
        self.active_indexes = active_indexes
        self.mouse_selection_active = False
        QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)
        self.show_active_mask()


    def show_mask(self, indexes, color):
        self.indexes = indexes
        if color == MaskColor.RED:
            self.mask_color = QColor(255, 0, 0, 60)
        elif color == MaskColor.GREEN:
            self.mask_color = QColor(64, 224, 43, 60)
        elif color == MaskColor.BLUE:
            self.mask_color = QColor(62, 118, 235, 60)
        self.update() # call to paintEvent() - DON'T call it directly

    def hide_mask(self):
        self.indexes = []
        self.update()