from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QColor
from Enums import Color

class PixelListView:
    """
    Class responsible for managing list of clicked pixels - GUI.
    """
    def __init__(self, p_list):
        self.list = p_list

    def load_from_mask(self, mask):
        """
        function to load pixels from given mask
        """
        self.clear()
        for el in mask.pixel_values:
            self.add_element(el)

    def add_element(self, grey_value):
        """
        function to add element to pixel list.
        """
        element = QListWidgetItem('%s' % grey_value)
        element.setBackground(QColor(grey_value, grey_value, grey_value))
        if grey_value > Color.WHITE // 2 : 
            element.setForeground(QColor(Color.BLACK, Color.BLACK, Color.BLACK))
        else : 
            element.setForeground(QColor(Color.WHITE, Color.WHITE, Color.WHITE))
        self.list.addItem(element)

    def remove_last(self):
        """
        function to remove last clicked pixel.
        """
        self.list.takeItem(self.list.count() - 1)
    
    def clear(self):
        """
        function to remove all values from the pixel list.
        """
        items_to_delete = self.list.count()
        for i in range(items_to_delete):
            self.list.takeItem(0)