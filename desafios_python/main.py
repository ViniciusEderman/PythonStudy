from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import sys

def principal_func():
    print("Teste")

app = QApplication([])
Menu=uic.loudUi("Menu.ui")
Menu.pushButton.clicked .connect(principal_func)

Menu.show()
app.exec()  