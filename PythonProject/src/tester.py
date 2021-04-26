from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

colors = [ QColor(200, 200, 200), QColor(100, 100, 100), QColor(255,255,255), QColor(0,0,0)]

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        w = QListWidget()
        for n in range(len(colors)):
            i = QListWidgetItem('%s' % n)
            i.setBackground( colors[n] )
            w.addItem(i)

        self.setCentralWidget(w)

        self.show()


app = QApplication([])
w = MainWindow()
app.exec_()