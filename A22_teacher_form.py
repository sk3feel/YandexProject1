import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import sqlite3
import funsions

from constants import *
from function_bd import *
from routine_functions import *

no_duty = '-'

class Teacher_Form(QMainWindow):
    def __init__(self, login):
        super().__init__()
        uic.loadUi('A12_teacher_form.ui', self)
        self.setWindowTitle('DutyManager')
        self.login = login
        self.con = sqlite3.connect('duty_db.sqlite')
        self.cur = self.con.cursor()
        self.btn_1st_st.clicked.connect(self.pick_student)
        self.btn_2nd_st.clicked.connect(self.pick_student)
        self.btn_3d_st.clicked.connect(self.pick_student)
        self.btn_end.clicked.connect(self.change_date)
        self.make_array_of_studs()
        self.load_date()
        self.load_info_about_user()

    # Страница 1: выбор дежурных
    def load_date(self):
        self.ledit_day_month.setEnabled(False)
        self.classid = funsions.get_users_info(self.login)[funsions.user_inx_classid]
        self.ledit_day_month.setText(funsions.get_near_day_of_duty(self.classid))

    def check_duty(self):
        if funsions.get_near_day_of_duty(self.classid) == '-':
            self.statusBar().showMessage('Нет утвержденных дежурств')
            return False
        return True

    def make_array_of_studs(self):
        pass
    #     clas, self.ok_pressed = QInputDialog.getItem(
    #         self, "Выберите класс", "Какой класс?",
    #         (
    #             'Крамин Карим, дежурил 4 раза', '10Б', '10В', '10Г', '10Д',
    #             '11А', '11Б', '11В', '11Г', '11Д',
    #             '9А', '9Б', '9В', '9Г', '9Д',
    #             '8А', '8Б', '8В', '8Г', '8Д',
    #             '7А', '7Б', '7В', '7Г'
    #         ), 0, False)
    #     if self.ok_pressed:
    #         self.clas = clas
    #         self.btn_pick_class.setText(clas)


    def pick_student(self):
        if self.check_duty():
            pass


    def change_date(self):
        if self.check_duty():
            pass


    # Страница 2: личные данные
    def load_info_about_user(self):
        info_array = get_users_info_by_log(self.login)
        self.ledit_login.setEnabled(False)
        self.ledit_surname.setEnabled(False)
        self.ledit_name.setEnabled(False)
        self.ledit_fathername.setEnabled(False)
        self.ledit_class.setEnabled(False)
        self.ledit_gender.setEnabled(False)

        self.ledit_login.setText(info_array[us_inx_login])
        self.ledit_surname.setText(info_array[us_inx_surname])
        self.ledit_name.setText(info_array[us_inx_name])
        self.ledit_fathername.setText(info_array[us_inx_fathername])
        self.ledit_gender.setText(info_array[us_inx_gender])
        class_title = get_class_title_by_log(self.login)
        self.ledit_class.setText(class_title)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Teacher_Form('EKA')
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())