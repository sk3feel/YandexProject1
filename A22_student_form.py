import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import funsions
import sqlite3


class Student_Form(QMainWindow):
    def __init__(self, login):
        super().__init__()
        uic.loadUi('A12_student_form.ui', self)
        self.setWindowTitle('DutyManager')
        self.login = login
        self.btn_bid.clicked.connect(self.make_a_bid)
        self.con = sqlite3.connect('duty_db.sqlite')
        self.cur = self.con.cursor()
        self.load_date()
        self.results()
        self.initUI()

    # Страница 1: подача заявки
    def load_date(self):
        self.ledit_day_month.setEnabled(False)
        classid = funsions.get_users_info(self.login)[funsions.user_inx_classid]
        self.ledit_day_month.setText(funsions.get_near_day_of_duty(classid))

    def make_a_bid(self):
        self.cur.execute('''
                UPDATE Users SET desireSt=? WHERE login= ?''', (True, self.login,))
        self.con.commit()

    def results(self):
        self.ledit_res.setEnabled(False)
        classid = funsions.users_get_class_id(self.login)
        result = self.cur.execute(
            '''SELECT act FROM Users WHERE login=(SELECT loginTeacher FROM Classes WHERE classId = ?)''', (classid,)
        ).fetchone()
        if funsions.get_users_info(self.login)[funsions.user_inx_act]:
            self.ledit_res.setText('Дежуришь')
        elif result:
            self.ledit_res.setText('Не дежуришь')
        else:
            self.ledit_res.setText('Неизвестен')

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
    ex = Student_Form('skfeel')
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
