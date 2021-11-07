import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import random

from Py_Designs.A12_student_form_ui import Ui_MainWindow

from routine_functions import *
from messages import *
from base_db_functions import *


class Student_Form(QMainWindow, Ui_MainWindow):
    def __init__(self, login):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi(STUDENT_UI_FILE, self)
        self.setWindowTitle(DUTY_MANAGER)
        self.login = login
        # Страница 1: подача заявки
        self.near_duty_day, self.classid = UNDEFINED, UNDEFINED
        self.btn_bid.clicked.connect(self.make_a_bid)
        self.btn_update.clicked.connect(self.update_results)
        self.btn_next.clicked.connect(self.show_random_frase)
        self.load_date_of_near_duty()
        self.load_results()
        self.show_random_frase()
        # Страница 2: личные данные
        self.load_info_about_user()

    # Страница 1: подача заявки
    def load_date_of_near_duty(self):
        self.ledit_day_month.setEnabled(False)
        self.classid = select_one_with_aspect(USERS, LOGIN, self.login, CLASS_ID)[0]
        all_duty_days = select_all_with_two_aspects \
            (DUTYS, CLASS_ID, self.classid, PASSED, base_date_status, DATE)
        if all_duty_days:
            self.near_duty_day = get_near_day_of_duty(all_duty_days)
            self.ledit_day_month.setText(self.near_duty_day)
        else:
            self.ledit_day_month.setText('-')

    def make_a_bid(self):
        update_aspect(USERS, DESIRE_ST, bid_desireSt, LOGIN, self.login)

    def load_results(self):
        self.ledit_res.setEnabled(False)
        teachers_login = select_one_with_aspect(CLASSES, CLASS_ID, self.classid, LOGIN_TEACHER)[0]
        teacher_act = select_one_with_aspect(USERS, LOGIN, teachers_login, ACT)[0]
        student_act = select_one_with_aspect(USERS, LOGIN, self.login, ACT)[0]

        if teacher_act and student_act:
            self.ledit_res.setText(IS_ON_DUTY)
        elif teacher_act and not student_act:
            self.ledit_res.setText(IS_NOT_ON_DUTY)
        else:
            self.ledit_res.setText(UNKNOWN)

    def update_results(self):
        self.load_results()
        self.load_date_of_near_duty()

    def show_random_frase(self):
        frases = open(NAME_TXT_FILE, mode='rt', encoding='utf8').read().split('\n')[:-1]
        n = random.randint(0, len(frases) - 1)
        self.lbl_for_frase.setText(frases[n])

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
    ex = Student_Form('skfeel')
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
