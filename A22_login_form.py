import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

import sqlite3

from A22_register_wig import Registr
from A22_student_form import Student_Form
from A22_teacher_form import Teacher_Form
from A22_admin_form import Admin_Form

LOGIN = ''
password_index = 7
code_index = 4

class Log_In(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('A12_login_form.ui', self)

        self.setWindowTitle('DutyManager')
        self.btn_register.clicked.connect(self.registration)
        self.btn_enter.clicked.connect(self.enter)
        self.reg_wind = Registr()


    def registration(self):
        self.reg_wind.show()


    def enter(self):
        f_entre = False
        con = sqlite3.connect('duty_db.sqlite')
        cur = con.cursor()
        login = self.ledit_login.text()
        password = self.ledit_password.text()
        result = cur.execute(
            '''SELECT * FROM Users WHERE login=?''', (login,)
        ).fetchone()
        if result is None:
            self.statusBar().showMessage('Аккаунта с таким логином не существует')
        else:
            if result[password_index] == password:
                f_entre = True
                self.statusBar().showMessage('Вы успешно вошли')
            else:
                self.statusBar().showMessage('Неверный пароль')
        if not f_entre:
            return f_entre
        code = result[code_index]
        self.student_wind = Student_Form(login)
        self.teacher_wind = Teacher_Form(login)
        self.admin_wind = Admin_Form(login)

        if code == 0:
            self.student_wind.show()
        if code == 1:
            self.teacher_wind.show()
        if code == 2:
            self.admin_wind.show()




def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Log_In()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())




