import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

import csv


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(613, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 601, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 581, 491))
        self.frame_2.setStyleSheet("QFrame {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(176, 224, 230);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton.setGeometry(QtCore.QRect(30, 120, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(90, 70, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 451, 51))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame = QtWidgets.QFrame(self.tab_2)
        self.frame.setGeometry(QtCore.QRect(-10, -20, 601, 521))
        self.frame.setStyleSheet("QFrame {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(176, 224, 230);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(140, 70, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lbl_register = QtWidgets.QLabel(self.frame)
        self.lbl_register.setGeometry(QtCore.QRect(40, 20, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_register.setFont(font)
        self.lbl_register.setObjectName("lbl_register")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(140, 300, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.ledit_login = QtWidgets.QLineEdit(self.frame)
        self.ledit_login.setGeometry(QtCore.QRect(240, 70, 221, 20))
        self.ledit_login.setObjectName("ledit_login")
        self.ledit_password_2 = QtWidgets.QLineEdit(self.frame)
        self.ledit_password_2.setGeometry(QtCore.QRect(240, 110, 221, 20))
        self.ledit_password_2.setObjectName("ledit_password_2")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(140, 110, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(140, 150, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.ledit_password_3 = QtWidgets.QLineEdit(self.frame)
        self.ledit_password_3.setGeometry(QtCore.QRect(240, 150, 221, 20))
        self.ledit_password_3.setObjectName("ledit_password_3")
        self.ledit_password_4 = QtWidgets.QLineEdit(self.frame)
        self.ledit_password_4.setGeometry(QtCore.QRect(240, 230, 221, 20))
        self.ledit_password_4.setObjectName("ledit_password_4")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(140, 190, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(140, 230, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(140, 380, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.ledit_login_2 = QtWidgets.QLineEdit(self.frame)
        self.ledit_login_2.setGeometry(QtCore.QRect(240, 300, 221, 20))
        self.ledit_login_2.setObjectName("ledit_login_2")
        self.btn_register_4 = QtWidgets.QPushButton(self.frame)
        self.btn_register_4.setGeometry(QtCore.QRect(240, 340, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_register_4.setFont(font)
        self.btn_register_4.setObjectName("btn_register_4")
        self.btn_register_5 = QtWidgets.QPushButton(self.frame)
        self.btn_register_5.setGeometry(QtCore.QRect(240, 380, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_register_5.setFont(font)
        self.btn_register_5.setObjectName("btn_register_5")
        self.ledit_password_5 = QtWidgets.QLineEdit(self.frame)
        self.ledit_password_5.setGeometry(QtCore.QRect(240, 190, 221, 20))
        self.ledit_password_5.setObjectName("ledit_password_5")
        self.btn_register_6 = QtWidgets.QPushButton(self.frame)
        self.btn_register_6.setGeometry(QtCore.QRect(240, 260, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Futura LT")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_register_6.setFont(font)
        self.btn_register_6.setObjectName("btn_register_6")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 613, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Дата:"))
        self.radioButton.setText(_translate("MainWindow", "Подать заявку"))
        self.label.setText(_translate("MainWindow", "Ближайшее предстоящее дежурство:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "Подать заявку"))
        self.label_3.setText(_translate("MainWindow", "Логин:"))
        self.lbl_register.setText(_translate("MainWindow", "Личные данные:"))
        self.label_5.setText(_translate("MainWindow", "Пол:"))
        self.label_7.setText(_translate("MainWindow", "Фамилия:"))
        self.label_8.setText(_translate("MainWindow", "Имя:"))
        self.label_9.setText(_translate("MainWindow", "Отчество:"))
        self.label_10.setText(_translate("MainWindow", "Класс:"))
        self.label_4.setText(_translate("MainWindow", "Пароль:"))
        self.btn_register_4.setText(_translate("MainWindow", "Изменить пол"))
        self.btn_register_5.setText(_translate("MainWindow", "Изменить пароль"))
        self.btn_register_6.setText(_translate("MainWindow", "Изменить класс"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Личные данные"))


class WidgetStudent(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('DutyManager')

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WidgetStudent()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())