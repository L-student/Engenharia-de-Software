from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def feminino():
    tela1.feminino_2.show()
    tela1.beleza_2.close()
    tela1.casa_3.close()
    tela1.plussize_2.close()
    tela1.infantil_2.close()
    tela1.masculino_2.close()
    tela1.casa_4.close()


def masculino():
    tela1.masculino_2.show()
    tela1.beleza_2.close()
    tela1.casa_3.close()
    tela1.plussize_2.close()
    tela1.infantil_2.close()
    tela1.feminino_2.close()
    tela1.casa_4.close()


def infantil():
    tela1.infantil_2.show()
    tela1.beleza_2.close()
    tela1.casa_3.close()
    tela1.plussize_2.close()
    tela1.masculino_2.close()
    tela1.feminino_2.close()
    tela1.casa_4.close()


def plus():
    tela1.plussize_2.show()
    tela1.beleza_2.close()
    tela1.casa_3.close()
    tela1.infantil_2.close()
    tela1.masculino_2.close()
    tela1.feminino_2.close()
    tela1.casa_4.close()


def casa():
    tela1.beleza_2.close()
    tela1.plussize_2.close()
    tela1.infantil_2.close()
    tela1.masculino_2.close()
    tela1.feminino_2.close()
    tela1.casa_3.show()
    tela1.casa_4.close()


def beleza():
    tela1.casa_3.close()
    tela1.plussize_2.close()
    tela1.infantil_2.close()
    tela1.masculino_2.close()
    tela1.feminino_2.close()
    tela1.beleza_2.show()
    tela1.casa_4.close()


def curtidos():
    tela1.casa_4.show()
    tela1.beleza_2.close()
    tela1.casa_3.close()
    tela1.plussize_2.close()
    tela1.infantil_2.close()
    tela1.masculino_2.close()
    tela1.feminino_2.close()

def out():
    tela1.close()

def out2():
    tela2.close()

def out3():
    tela3.close()

def entrou():
    tela3.close()
    tela1.pushButton_20.close()


def enviar():
    tela2.label_61.show()

def help1():
    tela2.show()

def login():
    tela3.show()

app = QtWidgets.QApplication([])

tela1 = uic.loadUi("segundo.ui")
tela2 = uic.loadUi("ajuda.ui")
tela3 = uic.loadUi("entrar.ui")

tela1.pushButton_16.clicked.connect(feminino)
tela1.pushButton_18.clicked.connect(masculino)
tela1.pushButton_15.clicked.connect(infantil)
tela1.pushButton_17.clicked.connect(plus)
tela1.pushButton_14.clicked.connect(casa)
tela1.pushButton_19.clicked.connect(beleza)
tela1.pushButton_22.clicked.connect(curtidos)
tela1.pushButton_13.clicked.connect(out)
tela2.pushButton_13.clicked.connect(out2)
tela2.pushButton_14.clicked.connect(enviar)
tela1.pushButton_12.clicked.connect(help1)
tela1.pushButton_20.clicked.connect(login)
tela3.pushButton_22.clicked.connect(out3)
tela3.pushButton_23.clicked.connect(entrou)
tela3.pushButton_26.clicked.connect(entrou)


tela1.beleza_2.close()
tela1.casa_3.close()
tela1.plussize_2.close()
tela1.infantil_2.close()
tela1.masculino_2.close()
tela1.casa_4.close()
tela2.label_61.close()

tela1.show()
app.exec()