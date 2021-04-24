# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/PhotoEdit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Label import Label

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1273, 1105)
        MainWindow.setStyleSheet("* {\n"
"    font-size: 16px;\n"
"}\n"
"QMainWindow {\n"
"    background-color:rgb(82, 82, 82);\n"
"}\n"
"QTextEdit {\n"
"    background-color:rgb(42, 42, 42);\n"
"    color: rgb(0, 255, 0);\n"
"}\n"
"QPushButton{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-bottom-color: rgb(58, 58, 58);\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"    border-bottom-color: rgb(115, 115, 115);\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(62, 62, 62, 255), stop:1 rgba(22, 22, 22, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-bottom-color: rgb(58, 58, 58);\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-bottom-color: rgb(58, 58, 58);\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: rgb(0, 0, 0);\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));\n"
"}\n"
"QLineEdit {\n"
"    border-width: 1px; border-radius: 4px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    padding: 0 8px;\n"
"    color: rgb(255, 255, 255);\n"
"    background:rgb(100, 100, 100);\n"
"    selection-background-color: rgb(187, 187, 187);\n"
"    selection-color: rgb(60, 63, 65);\n"
"}\n"
"QLabel {\n"
"    color:rgb(255,255,255);    \n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color:rgb(77,77,77);\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));\n"
"    border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"    background:rgb(82, 82, 82);\n"
"}\n"
"QMenuBar::item {\n"
"    color:rgb(223,219,210);\n"
"    spacing: 3px;\n"
"    padding: 1px 4px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background:rgb(115, 115, 115);\n"
"}\n"
"QMenu::item:selected {\n"
"    color:rgb(255,255,255);\n"
"    border-width:2px;\n"
"    border-style:solid;\n"
"    padding-left:18px;\n"
"    padding-right:8px;\n"
"    padding-top:2px;\n"
"    padding-bottom:3px;\n"
"    background:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-bottom-color: rgb(58, 58, 58);\n"
"    border-bottom-width: 1px;\n"
"}\n"
"QMenu::item {\n"
"    color:rgb(223,219,210);\n"
"    background-color:rgb(78,78,78);\n"
"    padding-left:20px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:10px;\n"
"}\n"
"QMenu{\n"
"    background-color:rgb(78,78,78);\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:rgb(247,246,246);\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(77,77,77);\n"
"        background-color:rgb(101,101,101);\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    padding:2px;\n"
"    color:rgb(250,250,250);\n"
"      background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"      border-top-right-radius:4px;\n"
"   border-top-left-radius:4px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
"    border-bottom-color: rgb(101,101,101);\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      background-color:rgb(101,101,101);\n"
"      margin-left: 0px;\n"
"      margin-right: 1px;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"        margin-top: 1px;\n"
"        margin-right: 1px;\n"
"}\n"
"QCheckBox {\n"
"    color:rgb(223,219,210);\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: rgb(87, 97, 106);\n"
"    background-color:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 150), stop:1 rgba(93, 103, 113, 150));\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    border-width:1px;\n"
"    border-color: rgb(180,180,180);\n"
"      background-color:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    border-width:1px;\n"
"    border-color: rgb(87, 97, 106);\n"
"      background-color:rgb(255,255,255);\n"
"}\n"
"QStatusBar {\n"
"    color:rgb(240,240,240);\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 14px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    height: 14px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background: #04b97f;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 847, 1040))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.graphicArea = Label(self.scrollAreaWidgetContents_2)
        self.graphicArea.setText("")
        self.graphicArea.setObjectName("graphicArea")
        self.gridLayout_5.addWidget(self.graphicArea, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1273, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFilter = QtWidgets.QMenu(self.menubar)
        self.menuFilter.setObjectName("menuFilter")
        self.menuSelect = QtWidgets.QMenu(self.menubar)
        self.menuSelect.setObjectName("menuSelect")
        self.menuMask = QtWidgets.QMenu(self.menubar)
        self.menuMask.setObjectName("menuMask")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolsSettings = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolsSettings.sizePolicy().hasHeightForWidth())
        self.toolsSettings.setSizePolicy(sizePolicy)
        self.toolsSettings.setMinimumSize(QtCore.QSize(400, 229))
        self.toolsSettings.setObjectName("toolsSettings")
        self.Container = QtWidgets.QWidget()
        self.Container.setObjectName("Container")
        self.gridLayout = QtWidgets.QGridLayout(self.Container)
        self.gridLayout.setObjectName("gridLayout")
        self.Settings = QtWidgets.QToolBox(self.Container)
        self.Settings.setObjectName("Settings")
        self.Filters = QtWidgets.QWidget()
        self.Filters.setGeometry(QtCore.QRect(0, 0, 382, 922))
        self.Filters.setObjectName("Filters")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Filters)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.avaraging_border_type = QtWidgets.QTabWidget(self.Filters)
        self.avaraging_border_type.setObjectName("avaraging_border_type")
        self.gauss_settings_2 = QtWidgets.QWidget()
        self.gauss_settings_2.setObjectName("gauss_settings_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gauss_settings_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtWidgets.QLabel(self.gauss_settings_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_13 = QtWidgets.QLabel(self.gauss_settings_2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.gauss_k_size_x = QtWidgets.QSpinBox(self.gauss_settings_2)
        self.gauss_k_size_x.setObjectName("gauss_k_size_x")
        self.verticalLayout_4.addWidget(self.gauss_k_size_x)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.gauss_settings_2)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.gauss_k_size_y = QtWidgets.QSpinBox(self.gauss_settings_2)
        self.gauss_k_size_y.setObjectName("gauss_k_size_y")
        self.verticalLayout_5.addWidget(self.gauss_k_size_y)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_10 = QtWidgets.QLabel(self.gauss_settings_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_17 = QtWidgets.QLabel(self.gauss_settings_2)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_8.addWidget(self.label_17)
        self.gauss_sigma_x = QtWidgets.QSpinBox(self.gauss_settings_2)
        self.gauss_sigma_x.setObjectName("gauss_sigma_x")
        self.verticalLayout_8.addWidget(self.gauss_sigma_x)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_18 = QtWidgets.QLabel(self.gauss_settings_2)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_9.addWidget(self.label_18)
        self.gauss_sigma_y = QtWidgets.QSpinBox(self.gauss_settings_2)
        self.gauss_sigma_y.setObjectName("gauss_sigma_y")
        self.verticalLayout_9.addWidget(self.gauss_sigma_y)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.label_11 = QtWidgets.QLabel(self.gauss_settings_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.gauss_border_type = QtWidgets.QComboBox(self.gauss_settings_2)
        self.gauss_border_type.setObjectName("gauss_border_type")
        self.gauss_border_type.addItem("")
        self.gauss_border_type.addItem("")
        self.gauss_border_type.addItem("")
        self.gauss_border_type.addItem("")
        self.gauss_border_type.addItem("")
        self.gauss_border_type.addItem("")
        self.gauss_border_type.addItem("")
        self.gauss_border_type.addItem("")
        self.gauss_border_type.addItem("")
        self.verticalLayout.addWidget(self.gauss_border_type)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.avaraging_border_type.addTab(self.gauss_settings_2, "")
        self.median_settings = QtWidgets.QWidget()
        self.median_settings.setObjectName("median_settings")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.median_settings)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.median_settings)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_10.addWidget(self.label_12)
        self.median_kernel_size = QtWidgets.QSpinBox(self.median_settings)
        self.median_kernel_size.setMinimum(1)
        self.median_kernel_size.setSingleStep(2)
        self.median_kernel_size.setObjectName("median_kernel_size")
        self.verticalLayout_10.addWidget(self.median_kernel_size)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem1)
        self.gridLayout_4.addLayout(self.verticalLayout_10, 0, 0, 1, 1)
        self.avaraging_border_type.addTab(self.median_settings, "")
        self.avaraging_settings = QtWidgets.QWidget()
        self.avaraging_settings.setObjectName("avaraging_settings")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.avaraging_settings)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_19 = QtWidgets.QLabel(self.avaraging_settings)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_11.addWidget(self.label_19)
        self.avaraging_kernel_size = QtWidgets.QSpinBox(self.avaraging_settings)
        self.avaraging_kernel_size.setObjectName("avaraging_kernel_size")
        self.verticalLayout_11.addWidget(self.avaraging_kernel_size)
        self.verticalLayout_14.addLayout(self.verticalLayout_11)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_21 = QtWidgets.QLabel(self.avaraging_settings)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_13.addWidget(self.label_21)
        self.avaraging_anchor_x = QtWidgets.QSpinBox(self.avaraging_settings)
        self.avaraging_anchor_x.setObjectName("avaraging_anchor_x")
        self.verticalLayout_13.addWidget(self.avaraging_anchor_x)
        self.horizontalLayout_5.addLayout(self.verticalLayout_13)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_20 = QtWidgets.QLabel(self.avaraging_settings)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_12.addWidget(self.label_20)
        self.avaraging_anchor_y = QtWidgets.QSpinBox(self.avaraging_settings)
        self.avaraging_anchor_y.setObjectName("avaraging_anchor_y")
        self.verticalLayout_12.addWidget(self.avaraging_anchor_y)
        self.horizontalLayout_5.addLayout(self.verticalLayout_12)
        self.verticalLayout_14.addLayout(self.horizontalLayout_5)
        self.label_22 = QtWidgets.QLabel(self.avaraging_settings)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_14.addWidget(self.label_22)
        self.avaraging_border_type_2 = QtWidgets.QComboBox(self.avaraging_settings)
        self.avaraging_border_type_2.setObjectName("avaraging_border_type_2")
        self.avaraging_border_type_2.addItem("")
        self.avaraging_border_type_2.addItem("")
        self.avaraging_border_type_2.addItem("")
        self.avaraging_border_type_2.addItem("")
        self.avaraging_border_type_2.addItem("")
        self.avaraging_border_type_2.addItem("")
        self.avaraging_border_type_2.addItem("")
        self.avaraging_border_type_2.addItem("")
        self.verticalLayout_14.addWidget(self.avaraging_border_type_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem2)
        self.avaraging_border_type.addTab(self.avaraging_settings, "")
        self.bilateral_settings = QtWidgets.QWidget()
        self.bilateral_settings.setObjectName("bilateral_settings")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.bilateral_settings)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_23 = QtWidgets.QLabel(self.bilateral_settings)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_15.addWidget(self.label_23)
        self.bilateral_diameter = QtWidgets.QSpinBox(self.bilateral_settings)
        self.bilateral_diameter.setMinimum(-100)
        self.bilateral_diameter.setMaximum(100)
        self.bilateral_diameter.setObjectName("bilateral_diameter")
        self.verticalLayout_15.addWidget(self.bilateral_diameter)
        self.verticalLayout_18.addLayout(self.verticalLayout_15)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_24 = QtWidgets.QLabel(self.bilateral_settings)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_16.addWidget(self.label_24)
        self.bilateral_sigma_color = QtWidgets.QSpinBox(self.bilateral_settings)
        self.bilateral_sigma_color.setObjectName("bilateral_sigma_color")
        self.verticalLayout_16.addWidget(self.bilateral_sigma_color)
        self.horizontalLayout_6.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_25 = QtWidgets.QLabel(self.bilateral_settings)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_17.addWidget(self.label_25)
        self.bilateral_sigma_space = QtWidgets.QSpinBox(self.bilateral_settings)
        self.bilateral_sigma_space.setMinimum(-100)
        self.bilateral_sigma_space.setMaximum(100)
        self.bilateral_sigma_space.setObjectName("bilateral_sigma_space")
        self.verticalLayout_17.addWidget(self.bilateral_sigma_space)
        self.horizontalLayout_6.addLayout(self.verticalLayout_17)
        self.verticalLayout_18.addLayout(self.horizontalLayout_6)
        self.label_26 = QtWidgets.QLabel(self.bilateral_settings)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_18.addWidget(self.label_26)
        self.bilateral_border_type = QtWidgets.QComboBox(self.bilateral_settings)
        self.bilateral_border_type.setObjectName("bilateral_border_type")
        self.bilateral_border_type.addItem("")
        self.bilateral_border_type.addItem("")
        self.bilateral_border_type.addItem("")
        self.bilateral_border_type.addItem("")
        self.bilateral_border_type.addItem("")
        self.bilateral_border_type.addItem("")
        self.bilateral_border_type.addItem("")
        self.bilateral_border_type.addItem("")
        self.bilateral_border_type.addItem("")
        self.verticalLayout_18.addWidget(self.bilateral_border_type)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem3)
        self.avaraging_border_type.addTab(self.bilateral_settings, "")
        self.gridLayout_2.addWidget(self.avaraging_border_type, 0, 0, 1, 1)
        self.Settings.addItem(self.Filters, "")
        self.Mask = QtWidgets.QWidget()
        self.Mask.setGeometry(QtCore.QRect(0, 0, 382, 922))
        self.Mask.setObjectName("Mask")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.Mask)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_27 = QtWidgets.QLabel(self.Mask)
        self.label_27.setStyleSheet("color:black;")
        self.label_27.setObjectName("label_27")
        self.verticalLayout_19.addWidget(self.label_27)
        self.horizontalSlider = QtWidgets.QSlider(self.Mask)
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_19.addWidget(self.horizontalSlider)
        self.label_32 = QtWidgets.QLabel(self.Mask)
        self.label_32.setStyleSheet("color:black;")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_19.addWidget(self.label_32)
        self.verticalLayout_22.addLayout(self.verticalLayout_19)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_28 = QtWidgets.QLabel(self.Mask)
        self.label_28.setStyleSheet("color:black;")
        self.label_28.setObjectName("label_28")
        self.verticalLayout_20.addWidget(self.label_28)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.Mask)
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout_20.addWidget(self.horizontalSlider_2)
        self.label_31 = QtWidgets.QLabel(self.Mask)
        self.label_31.setStyleSheet("color:black;")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_20.addWidget(self.label_31)
        self.verticalLayout_22.addLayout(self.verticalLayout_20)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_29 = QtWidgets.QLabel(self.Mask)
        self.label_29.setStyleSheet("color : black;")
        self.label_29.setObjectName("label_29")
        self.verticalLayout_21.addWidget(self.label_29)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.Mask)
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setProperty("value", 0)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setInvertedAppearance(False)
        self.horizontalSlider_3.setInvertedControls(False)
        self.horizontalSlider_3.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.verticalLayout_21.addWidget(self.horizontalSlider_3)
        self.label_30 = QtWidgets.QLabel(self.Mask)
        self.label_30.setStyleSheet("color:black;")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_21.addWidget(self.label_30)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem4)
        self.verticalLayout_22.addLayout(self.verticalLayout_21)
        self.Settings.addItem(self.Mask, "")
        self.Thresholding = QtWidgets.QWidget()
        self.Thresholding.setGeometry(QtCore.QRect(0, 0, 382, 922))
        self.Thresholding.setObjectName("Thresholding")
        self.Settings.addItem(self.Thresholding, "")
        self.gridLayout.addWidget(self.Settings, 0, 0, 1, 1)
        self.toolsSettings.setWidget(self.Container)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.toolsSettings)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSelect = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui/../../resources/selection-drag(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelect.setIcon(icon)
        self.actionSelect.setObjectName("actionSelect")
        self.actionRotate = QtWidgets.QAction(MainWindow)
        self.actionRotate.setObjectName("actionRotate")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionZoomIn = QtWidgets.QAction(MainWindow)
        self.actionZoomIn.setObjectName("actionZoomIn")
        self.actionZoomOut = QtWidgets.QAction(MainWindow)
        self.actionZoomOut.setObjectName("actionZoomOut")
        self.actionGaussian = QtWidgets.QAction(MainWindow)
        self.actionGaussian.setObjectName("actionGaussian")
        self.actionAvaraging = QtWidgets.QAction(MainWindow)
        self.actionAvaraging.setObjectName("actionAvaraging")
        self.actionMedian = QtWidgets.QAction(MainWindow)
        self.actionMedian.setObjectName("actionMedian")
        self.actionBilateral = QtWidgets.QAction(MainWindow)
        self.actionBilateral.setObjectName("actionBilateral")
        self.actionRect = QtWidgets.QAction(MainWindow)
        self.actionRect.setObjectName("actionRect")
        self.actionSelect_from_image = QtWidgets.QAction(MainWindow)
        self.actionSelect_from_image.setObjectName("actionSelect_from_image")
        self.actionApply = QtWidgets.QAction(MainWindow)
        self.actionApply.setObjectName("actionApply")
        self.actionApply_2 = QtWidgets.QAction(MainWindow)
        self.actionApply_2.setObjectName("actionApply_2")
        self.actionkernel_x_gauss_changed = QtWidgets.QAction(MainWindow)
        self.actionkernel_x_gauss_changed.setObjectName("actionkernel_x_gauss_changed")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuEdit.addAction(self.actionZoomIn)
        self.menuEdit.addAction(self.actionZoomOut)
        self.menuFilter.addAction(self.actionGaussian)
        self.menuFilter.addAction(self.actionAvaraging)
        self.menuFilter.addAction(self.actionMedian)
        self.menuFilter.addAction(self.actionBilateral)
        self.menuSelect.addAction(self.actionRect)
        self.menuMask.addAction(self.actionSelect_from_image)
        self.menuMask.addAction(self.actionApply)
        self.menuMask.addAction(self.actionApply_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFilter.menuAction())
        self.menubar.addAction(self.menuSelect.menuAction())
        self.menubar.addAction(self.menuMask.menuAction())

        self.retranslateUi(MainWindow)
        self.Settings.setCurrentIndex(0)
        self.avaraging_border_type.setCurrentIndex(3)
        self.horizontalSlider_3.valueChanged['int'].connect(self.label_30.setNum)
        self.horizontalSlider.valueChanged['int'].connect(self.label_32.setNum)
        self.horizontalSlider_2.valueChanged['int'].connect(self.label_31.setNum)
        self.bilateral_diameter.valueChanged['int'].connect(self.bilateral_diameter.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuFilter.setTitle(_translate("MainWindow", "Filter"))
        self.menuSelect.setTitle(_translate("MainWindow", "Select"))
        self.menuMask.setTitle(_translate("MainWindow", "Mask"))
        self.label_9.setText(_translate("MainWindow", "Kernel Size"))
        self.label_13.setText(_translate("MainWindow", "Kernel X"))
        self.label_14.setText(_translate("MainWindow", "Kernel Y"))
        self.label_10.setText(_translate("MainWindow", "Kernel Standard Deviation"))
        self.label_17.setText(_translate("MainWindow", "X - axis"))
        self.label_18.setText(_translate("MainWindow", "Y - axis"))
        self.label_11.setText(_translate("MainWindow", "Border Type"))
        self.gauss_border_type.setItemText(0, _translate("MainWindow", "BORDER_CONSTANT"))
        self.gauss_border_type.setItemText(1, _translate("MainWindow", "BORDER_REPLICATE"))
        self.gauss_border_type.setItemText(2, _translate("MainWindow", "BORDER_REFLECT"))
        self.gauss_border_type.setItemText(3, _translate("MainWindow", "BORDER_WRAP"))
        self.gauss_border_type.setItemText(4, _translate("MainWindow", "BORDER_REFLECT_101"))
        self.gauss_border_type.setItemText(5, _translate("MainWindow", "BORDER_TRANSPARENT"))
        self.gauss_border_type.setItemText(6, _translate("MainWindow", "BORDER_REFLECT101"))
        self.gauss_border_type.setItemText(7, _translate("MainWindow", "BORDER_DEFAULT"))
        self.gauss_border_type.setItemText(8, _translate("MainWindow", "BORDER_ISOLATED"))
        self.avaraging_border_type.setTabText(self.avaraging_border_type.indexOf(self.gauss_settings_2), _translate("MainWindow", "Gauss"))
        self.label_12.setText(_translate("MainWindow", "Kernel Size"))
        self.avaraging_border_type.setTabText(self.avaraging_border_type.indexOf(self.median_settings), _translate("MainWindow", "Median"))
        self.label_19.setText(_translate("MainWindow", "Kernel Size"))
        self.label_21.setText(_translate("MainWindow", "Anchor X"))
        self.label_20.setText(_translate("MainWindow", "Anchor Y"))
        self.label_22.setText(_translate("MainWindow", "Border Type"))
        self.avaraging_border_type_2.setItemText(0, _translate("MainWindow", "BORDER_CONSTANT"))
        self.avaraging_border_type_2.setItemText(1, _translate("MainWindow", "BORDER_REPLICATE"))
        self.avaraging_border_type_2.setItemText(2, _translate("MainWindow", "BORDER_REFLECT"))
        self.avaraging_border_type_2.setItemText(3, _translate("MainWindow", "BORDER_REFLECT_101"))
        self.avaraging_border_type_2.setItemText(4, _translate("MainWindow", "BORDER_TRANSPARENT"))
        self.avaraging_border_type_2.setItemText(5, _translate("MainWindow", "BORDER_REFLECT101"))
        self.avaraging_border_type_2.setItemText(6, _translate("MainWindow", "BORDER_DEFAULT"))
        self.avaraging_border_type_2.setItemText(7, _translate("MainWindow", "BORDER_ISOLATED"))
        self.avaraging_border_type.setTabText(self.avaraging_border_type.indexOf(self.avaraging_settings), _translate("MainWindow", "Avaraging"))
        self.label_23.setText(_translate("MainWindow", "Diameter"))
        self.label_24.setText(_translate("MainWindow", "Sigma Color"))
        self.label_25.setText(_translate("MainWindow", "Sigma Space"))
        self.label_26.setText(_translate("MainWindow", "Border Type"))
        self.bilateral_border_type.setItemText(0, _translate("MainWindow", "BORDER_CONSTANT"))
        self.bilateral_border_type.setItemText(1, _translate("MainWindow", "BORDER_WRAP"))
        self.bilateral_border_type.setItemText(2, _translate("MainWindow", "BORDER_REPLICATE"))
        self.bilateral_border_type.setItemText(3, _translate("MainWindow", "BORDER_REFLECT"))
        self.bilateral_border_type.setItemText(4, _translate("MainWindow", "BORDER_REFLECT_101"))
        self.bilateral_border_type.setItemText(5, _translate("MainWindow", "BORDER_TRANSPARENT"))
        self.bilateral_border_type.setItemText(6, _translate("MainWindow", "BORDER_REFLECT101"))
        self.bilateral_border_type.setItemText(7, _translate("MainWindow", "BORDER_DEFAULT"))
        self.bilateral_border_type.setItemText(8, _translate("MainWindow", "BORDER_ISOLATED"))
        self.avaraging_border_type.setTabText(self.avaraging_border_type.indexOf(self.bilateral_settings), _translate("MainWindow", "Bilateral"))
        self.Settings.setItemText(self.Settings.indexOf(self.Filters), _translate("MainWindow", "Filters"))
        self.label_27.setText(_translate("MainWindow", "Minimum"))
        self.label_32.setText(_translate("MainWindow", "0"))
        self.label_28.setText(_translate("MainWindow", "Maximum"))
        self.label_31.setText(_translate("MainWindow", "0"))
        self.label_29.setText(_translate("MainWindow", "Tolerance"))
        self.label_30.setText(_translate("MainWindow", "0"))
        self.Settings.setItemText(self.Settings.indexOf(self.Mask), _translate("MainWindow", "Mask"))
        self.Settings.setItemText(self.Settings.indexOf(self.Thresholding), _translate("MainWindow", "Thresholding"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSelect.setText(_translate("MainWindow", "Select"))
        self.actionRotate.setText(_translate("MainWindow", "rotate"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionZoomIn.setText(_translate("MainWindow", "zoom-in"))
        self.actionZoomOut.setText(_translate("MainWindow", "zoom-out"))
        self.actionGaussian.setText(_translate("MainWindow", "Gaussian"))
        self.actionAvaraging.setText(_translate("MainWindow", "Avaraging"))
        self.actionMedian.setText(_translate("MainWindow", "Median"))
        self.actionBilateral.setText(_translate("MainWindow", "Bilateral"))
        self.actionRect.setText(_translate("MainWindow", "Rectangular"))
        self.actionSelect_from_image.setText(_translate("MainWindow", "Select from image"))
        self.actionApply.setText(_translate("MainWindow", "Select from settings"))
        self.actionApply_2.setText(_translate("MainWindow", "Apply"))
        self.actionkernel_x_gauss_changed.setText(_translate("MainWindow", "kernel_x_gauss_changed"))
