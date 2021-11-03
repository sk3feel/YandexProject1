import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from constants import *
from function_bd import *
from routine_functions import *

from messages import *


class Student_Form(QMainWindow):
    def __init__(self, login):
        super().__init__()
        uic.loadUi('A12_student_form.ui', self)
        self.setWindowTitle(DUTY_MANAGER)
        self.login = login
        self.btn_bid.clicked.connect(self.make_a_bid)
        self.load_date_of_near_duty()
        self.load_results()
        self.load_info_about_user()

    # Страница 1: подача заявки
    def load_date_of_near_duty(self):
        self.ledit_day_month.setEnabled(False)
        classid = get_class_id_by_login(self.login)
        self.ledit_day_month.setText(get_near_day_of_duty(classid))

    def make_a_bid(self):
        desire_true_by_login(self.login)

    def load_results(self):
        self.ledit_res.setEnabled(False)
        classid = get_class_id_by_login(self.login)
        teacher_act = is_teacher_decided(classid)
        student_act = get_users_info_by_log(self.login)[us_inx_act]

        if teacher_act and student_act:
            self.ledit_res.setText(IS_ON_DUTY)
        elif teacher_act and not student_act:
            self.ledit_res.setText(IS_NOT_ON_DUTY)
        else:
            self.ledit_res.setText(UNKNOWN)

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
    ex = Student_Form('skfeel')
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
