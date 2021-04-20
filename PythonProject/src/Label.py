from PyQt5.QtCore import (Qt, pyqtSignal,QRect,QPoint,QSize)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QObject
from PyQt5.QtWidgets import QApplication

from PyQt5.QtWidgets import QRubberBand
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

    def parent_it(self, item):
        item.setParent(self)

    def show_mask(self, indexes):
        self.thread = QThread()
        self.worker = Worker(indexes)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.created.connect(lambda item : self.parent_it(item))
        self.thread.start()




class Worker(QObject):
    finished = pyqtSignal()
    created = pyqtSignal(QRubberBand)

    def __init__(self, indexes):
        super().__init__(None)
        self.indexes = indexes

    def run(self):
        for i in range(len(self.indexes)):
            pixel_rect = QRubberBand(QRubberBand.Rectangle, None)
            size = 5
            pixel_rect.setGeometry(self.indexes[i][0], self.indexes[i][1], size, size)
            self.created.emit(pixel_rect)
        self.finished.emit()