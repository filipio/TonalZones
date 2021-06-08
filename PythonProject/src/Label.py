from PyQt5.QtCore import (Qt, pyqtSignal,QRect,QPoint)
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtWidgets import QApplication

class Label(QtWidgets.QLabel):
    """
    This class is responsible for handling UI events such as :
    -notify about clicked pixel events
    -mark clicked pixels
    """
    rect_change = pyqtSignal(QRect)
    pixel_clicked = pyqtSignal(int, int)
    pixel_mode_entered = pyqtSignal()
    pixel_mode_left = pyqtSignal()
    

    def __init__(self, *args, **kwargs):        
        QtWidgets.QLabel.__init__(self, *args, **kwargs)
        QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)
        self.pixel_mode_active = False
        self.clicked_pixels = []
        self.should_draw = False
        self.pixel_color = QColor(37, 203, 39, 60) # default color, here it's light green
        self.draw_size = 3

    def switch_mouse_selection(self):
        """
            change cursos shape
        """
        self.pixel_mode_active = not self.pixel_mode_active
        if self.pixel_mode_active:
            QApplication.setOverrideCursor(Qt.CursorShape.CrossCursor)
        else:
            QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)


    def enter_pixel_mode(self):
        """
            enter mode in which you manually select pixels by clicking on them
        """
        self.switch_mouse_selection()
        self.pixel_mode_entered.emit()
        self.should_draw = True
        self.update()

    def mouseReleaseEvent(self, event):
        """
            overriden method for mouse release handling
        """
        if event.button() == Qt.LeftButton and self.pixel_mode_active:
            x = event.pos().x()
            y = event.pos().y()
            self.clicked_pixels.append((x,y))
            self.should_draw = True
            self.pixel_clicked.emit(x,y)
            self.update()
        elif event.button() == Qt.MiddleButton and not self.pixel_mode_active:
            self.enter_pixel_mode()
        elif event.button() == Qt.RightButton and self.pixel_mode_active: 
            self.switch_mouse_selection()
            self.pixel_mode_left.emit()

        QtWidgets.QLabel.mouseReleaseEvent(self, event)

    def pop_last_pixel(self):
        if len(self.clicked_pixels):
            self.clicked_pixels.pop()

    def clear_pixels(self):
        self.clicked_pixels.clear()


    def paintEvent(self, event):
        """
        function that paints clicked pixels on image. Do not call this directly. Call it by
        self.update()
        """
        QtWidgets.QLabel.paintEvent(self,event)
        if self.should_draw:
            painter = QPainter(self)
            painter.setPen(QPen(self.pixel_color, 2, Qt.SolidLine))
            painter.setBrush(QBrush(self.pixel_color, Qt.SolidPattern))
            for i in range(len(self.clicked_pixels)):
                painter.drawEllipse(QPoint(self.clicked_pixels[i][0], self.clicked_pixels[i][1]), self.draw_size, self.draw_size)
            self.should_draw = False
            painter.end()       
