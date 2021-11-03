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

from constants import *
from function_bd import *
from routine_functions import *

from messages import *

from base_db_functions import *



class Teacher_Form(QMainWindow):
    def __init__(self, login):
        super().__init__()
        uic.loadUi('A12_teacher_form.ui', self)
        self.setWindowTitle(DUTY_MANAGER)
        self.login = login
        self.btn_1st_st.clicked.connect(self.pick_student)
        self.btn_2nd_st.clicked.connect(self.pick_student)
        self.btn_3d_st.clicked.connect(self.pick_student)
        self.btn_end.clicked.connect(self.change_date)
        self.make_array_of_studs()
        self.load_date_of_near_duty()
        self.load_info_about_user()

    # Страница 1: выбор дежурных
    def load_date_of_near_duty(self):
        self.ledit_day_month.setEnabled(False)
        self.classid = select_one_with_aspect(USERS, LOGIN, self.login, CLASS_ID)[0]
        all_duty_days = select_all_with_aspect(DUTYS, CLASS_ID, self.classid, DATE)
        self.near_duty_day = get_near_day_of_duty(all_duty_days)
        self.ledit_day_month.setText(self.near_duty_day)

    def check_duty(self):
        if self.near_duty_day == EMPTYNESS:
            self.statusBar().showMessage(NO_STATED_DUTYS)
            return False
        return True

    def make_array_of_studs(self):
        pass


    def pick_student(self):
        if self.check_duty():
            pass


    def change_date(self):
        if self.check_duty():
            pass


    # Страница 2: личные данные
    def load_info_about_user(self):
        info_array = select_one_with_aspect(USERS, LOGIN, self.login, *TABLES[USERS])
        self.ledit_login.setEnabled(False)
        self.ledit_surname.setEnabled(False)
        self.ledit_name.setEnabled(False)
        self.ledit_fathername.setEnabled(False)
        self.ledit_class.setEnabled(False)
        self.ledit_gender.setEnabled(False)

        self.ledit_login.setText(str(info_array[us_inx_login]))
        self.ledit_surname.setText(str(info_array[us_inx_surname]))
        self.ledit_name.setText(str(info_array[us_inx_name]))
        self.ledit_fathername.setText(str(info_array[us_inx_fathername]))
        self.ledit_gender.setText(str(info_array[us_inx_gender]))
        class_title = select_one_with_aspect(CLASSES, CLASS_ID, self.classid, TITLE)[0]
        self.ledit_class.setText(str(class_title))



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Teacher_Form('EKA')
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())