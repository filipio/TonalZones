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
        self.create_filter_menu(MainWindow)
        self.create_selection_menu(MainWindow)
    def create_filter_menu(self,MainWindow):
        self.filterButton = QtWidgets.QToolButton(MainWindow)
        self.filterButton.setText("Filter   ")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui\\../../resources/filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filterButton.setIcon(icon)
        
        self.actionBlurGauss = QtWidgets.QAction(MainWindow)
        self.actionBlurAvg = QtWidgets.QAction(MainWindow)
        self.actionBlurMed = QtWidgets.QAction(MainWindow)
        self.actionBlurBilateral = QtWidgets.QAction(MainWindow)

        self.actionBlurGauss.setText("Gaussian")
        self.actionBlurMed.setText("Median")
        self.actionBlurAvg.setText("Avaraging")
        self.actionBlurBilateral.setText("Bilateral")
        
        drop_menu = QtWidgets.QMenu("awesome",MainWindow)
        
        drop_menu.addAction(self.actionBlurAvg)
        drop_menu.addAction(self.actionBlurGauss)
        drop_menu.addAction(self.actionBlurMed)
        drop_menu.addAction(self.actionBlurBilateral)

        self.filterButton.setMenu(drop_menu)
        self.filterButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)

        self.toolBar.addWidget(self.filterButton)
    def create_selection_menu(self,MainWindow):
        self.filterButton = QtWidgets.QToolButton(MainWindow)
        self.filterButton.setText("Select   ")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui\\../../resources/scissors-cutting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filterButton.setIcon(icon)
        self.actionSelectionRectangular = QtWidgets.QAction(MainWindow)
        self.actionSelectionCustom = QtWidgets.QAction(MainWindow)
        self.actionSelectionPixels = QtWidgets.QAction(MainWindow)
        # add another selection tools here
        self.actionSelectionRectangular.setText("Rectangular")
        self.actionSelectionCustom.setText("Custom")
        self.actionSelectionCustom.setText("Pixels")
        drop_menu = QtWidgets.QMenu("awesome",MainWindow)
        drop_menu.addAction(self.actionSelectionRectangular)
        drop_menu.addAction(self.actionSelectionCustom)
        self.filterButton.setMenu(drop_menu)
        self.filterButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)

        self.toolBar.addWidget(self.filterButton)