import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

import csv

class Ui_DM_Authorization(object):
    def setupUi(self, DM_Authorization):
        DM_Authorization.setObjectName("DM_Authorization")
        DM_Authorization.resize(518, 397)
        self.centralwidget = QtWidgets.QWidget(DM_Authorization)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 501, 341))
        self.frame.setStyleSheet("QFrame {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(176, 224, 230);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_voyti = QtWidgets.QLabel(self.frame)
        self.lbl_voyti.setGeometry(QtCore.QRect(80, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_voyti.setFont(font)
        self.lbl_voyti.setObjectName("lbl_voyti")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(170, 80, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lbl_register = QtWidgets.QLabel(self.frame)
        self.lbl_register.setGeometry(QtCore.QRect(80, 210, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_register.setFont(font)
        self.lbl_register.setObjectName("lbl_register")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(170, 110, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.ledit_login = QtWidgets.QLineEdit(self.frame)
        self.ledit_login.setGeometry(QtCore.QRect(260, 80, 221, 20))
        self.ledit_login.setObjectName("ledit_login")
        self.ledit_password = QtWidgets.QLineEdit(self.frame)
        self.ledit_password.setGeometry(QtCore.QRect(260, 110, 221, 20))
        self.ledit_password.setObjectName("ledit_password")
        self.btn_register = QtWidgets.QPushButton(self.frame)
        self.btn_register.setGeometry(QtCore.QRect(150, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_register.setFont(font)
        self.btn_register.setObjectName("btn_register")
        self.btn_enter = QtWidgets.QPushButton(self.frame)
        self.btn_enter.setGeometry(QtCore.QRect(320, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_enter.setFont(font)
        self.btn_enter.setObjectName("btn_enter")
        DM_Authorization.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DM_Authorization)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 21))
        self.menubar.setObjectName("menubar")
        DM_Authorization.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DM_Authorization)
        self.statusbar.setObjectName("statusbar")
        DM_Authorization.setStatusBar(self.statusbar)

        self.retranslateUi(DM_Authorization)
        QtCore.QMetaObject.connectSlotsByName(DM_Authorization)

    def retranslateUi(self, DM_Authorization):
        _translate = QtCore.QCoreApplication.translate
        DM_Authorization.setWindowTitle(_translate("DM_Authorization", "MainWindow"))
        self.lbl_voyti.setText(_translate("DM_Authorization", "Войти в аккаунт:"))
        self.label_2.setText(_translate("DM_Authorization", "Логин:"))
        self.lbl_register.setText(_translate("DM_Authorization", "Зарегистрироваться"))
        self.label_5.setText(_translate("DM_Authorization", "Пароль:"))
        self.btn_register.setText(_translate("DM_Authorization", "Регистрация"))
        self.btn_enter.setText(_translate("DM_Authorization", "Войти"))


class WidgetLogIn(QMainWindow, Ui_DM_Authorization):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Авторизация')

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WidgetLogIn()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())