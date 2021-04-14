from PhotoEdit_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from Label import Label
class UI(Ui_MainWindow):
    """
    This class is responsible for creating GUI elements which can't be created
    with the use of Designer. Only creation of elements should be contained here.
    """
    def setupUi(self,MainWindow):
        # proponuje przerobić to na zwykłą klasę z konstruktorem w której będziemy trzymać MainWindow????
        super().setupUi(MainWindow)