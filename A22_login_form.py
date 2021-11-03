import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from A22_register_wig import Registr
from A22_student_form import Student_Form
from A22_teacher_form import Teacher_Form
from A22_admin_form import Admin_Form

from function_bd import *
from constants import *

from messages import *

class Log_In(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('A12_login_form.ui', self)

        self.setWindowTitle(DUTY_MANAGER)
        self.btn_register.clicked.connect(self.registration)
        self.btn_enter.clicked.connect(self.enter)
        self.reg_wind = Registr()

    def registration(self):
        self.reg_wind.show()

    def enter(self):
        login = self.ledit_login.text()
        password = self.ledit_password.text()

        if is_login_exist(login):
            if corr_password(login, password):
                status_code = get_users_info_by_log(login)[us_inx_code]
                self.open_duty_manager(login, status_code)
            else:
                self.error_wrong_pass()
        else:
            self.error_login_dont_exist()

    def error_login_dont_exist(self):
        self.statusBar().showMessage(LOGIN_ISNT_EXIST)

    def error_wrong_pass(self):
        self.statusBar().showMessage(WRONG_PASS)

    def open_duty_manager(self, login, status_code):
        if status_code == int_student_cod:
            self.student_wind = Student_Form(login)
            self.student_wind.show()
        elif status_code == int_teacher_cod:
            self.teacher_wind = Teacher_Form(login)
            self.teacher_wind.show()
        elif status_code == int_admin_cod:
            self.admin_wind = Admin_Form(login)
            self.admin_wind.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Log_In()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
