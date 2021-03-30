from PhotoEdit_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class UI(Ui_MainWindow):
    """
    This class is responsible for creating GUI elements which can't be created
    with the use of Designer. Only creation of elements should be contained here.
    """
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
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
