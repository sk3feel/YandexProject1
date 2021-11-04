import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from PIL import Image
from A22_register_wig import Registr
from A22_student_form import Student_Form
from A22_teacher_form import Teacher_Form
from A22_admin_form import Admin_Form

from messages import *
from base_db_functions import *
from constants import *

class Log_In(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(LOGIN_UI_FILE, self)
        self.setWindowTitle(DUTY_MANAGER)

        self.image, self.student_wind, self.teacher_wind, self.admin_wind, self.pixmap = \
            UNDEFINED, UNDEFINED, UNDEFINED, UNDEFINED, UNDEFINED

        self.load_pict()

        self.btn_register.clicked.connect(self.registration)
        self.btn_enter.clicked.connect(self.enter)
        self.reg_wind = Registr()

    def load_pict(self):
        im = Image.open(IMAGE)
        im2 = im.resize(NEW_SIZE_IMAGE)
        im2.save(NEW_IMAGE)
        self.pixmap = QPixmap(NEW_IMAGE)
        self.image = QLabel(self)
        self.image.move(*IMAGE_POSITION)
        self.image.resize(*NEW_SIZE_IMAGE)
        self.image.setPixmap(self.pixmap)

    def registration(self):
        self.reg_wind.show()

    def enter(self):
        login = self.ledit_login.text()
        password = self.ledit_password.text()

        password_and_status = select_one_with_aspect(USERS, LOGIN, login, PASSWORD, STATUS)
        if password_and_status is not None:
            db_password, db_status = password_and_status
            if password == str(db_password):
                self.open_duty_manager(login, db_status)
            else:
                self.error_wrong_pass()
        else:
            self.error_login_dont_exist()

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

    def error_login_dont_exist(self):
        self.statusBar().showMessage(LOGIN_ISNT_EXIST)

    def error_wrong_pass(self):
        self.statusBar().showMessage(WRONG_PASS)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Log_In()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
