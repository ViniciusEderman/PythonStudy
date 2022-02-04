from PyQt5 import  uic,QtWidgets

from main_2 import menu

def funcao_p():
    print("teste")

app=QtWidgets.QApplication([])
main=uic.loudUi("menu.ui")
menu.pushButton.clicked.connect(funcao_p)

menu.show()
app.exec()