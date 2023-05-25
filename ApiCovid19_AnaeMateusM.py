from PyQt5 import  uic
import PyQt5.QtWidgets as QtWidgets

import sys

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('C:/Users/mateu/Desktop/ApiCovid19/tela_api.ui', self)
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()