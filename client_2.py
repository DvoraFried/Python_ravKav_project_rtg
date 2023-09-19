from PyQt5 import QtWidgets
from gui import Ui_MainWindow

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow("127.0.0.1", 1023)
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
