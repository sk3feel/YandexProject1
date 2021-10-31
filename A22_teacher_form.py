import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import sqlite3
import funsions

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
        self.load_date()
        self.initUI()

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


    def pick_student(self):
        if self.check_duty():
            pass


    def change_date(self):
        if self.check_duty():
            pass





    # Страница 2: личные данные
    def initUI(self):
        result = funsions.get_users_info(self.login)
        self.ledit_login.setEnabled(False)
        self.ledit_surname.setEnabled(False)
        self.ledit_name.setEnabled(False)
        self.ledit_fathername.setEnabled(False)
        self.ledit_class.setEnabled(False)
        self.ledit_gender.setEnabled(False)

        self.ledit_login.setText(result[funsions.user_inx_login])
        self.ledit_surname.setText(result[funsions.user_inx_surname])
        self.ledit_name.setText(result[funsions.user_inx_name])
        self.ledit_fathername.setText(result[funsions.user_inx_fathername])
        self.ledit_gender.setText(result[funsions.user_inx_gender])
        classid = funsions.users_get_class_id(self.login)
        self.ledit_class.setText(classid)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Teacher_Form('MS')
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())