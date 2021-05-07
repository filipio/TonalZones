from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QColor
from Enums import Color

class PixelList:
    def __init__(self, p_list):
        self.list = p_list

    def load_from_mask(self, mask):
        self.clear()
        for el in mask.clicked_pixels:
            self.add_element(el)

    def add_element(self, grey_value):
        print("pixelList is adding element.")
        element = QListWidgetItem('%s' % grey_value)
        element.setBackground(QColor(grey_value, grey_value, grey_value))
        if grey_value > Color.WHITE // 2 : 
            element.setForeground(QColor(Color.BLACK, Color.BLACK, Color.BLACK))
        else : 
            element.setForeground(QColor(Color.WHITE, Color.WHITE, Color.WHITE))
        self.list.addItem(element)

    def remove_last(self):
        self.list.takeItem(self.list.count() - 1)
    
    def clear(self):
        items_to_delete = self.list.count()
        for i in range(items_to_delete):
            self.list.takeItem(0)