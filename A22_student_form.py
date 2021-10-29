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

# from A22_login_form import LOGIN
# log = LOGIN
# print(log)
LOGIN = 'kramink'


class Student_Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('A12_student_form.ui', self)
        self.setWindowTitle('DutyManager')
        self.initUI()

    def initUI(self):
        con = sqlite3.connect('duty_db.sqlite')
        cur = con.cursor()
        result = cur.execute(
            '''SELECT * FROM Users WHERE login=?''', (LOGIN,)
        ).fetchone()
        self.ledit_login.setEnabled(False)
        self.ledit_surname.setEnabled(False)
        self.ledit_name.setEnabled(False)
        self.ledit_fathername.setEnabled(False)
        self.ledit_class.setEnabled(False)
        self.ledit_gender.setEnabled(False)


        self.ledit_login.setText(result[8])
        self.ledit_surname.setText(result[1])
        self.ledit_name.setText(result[2])
        self.ledit_fathername.setText(result[3])
        self.ledit_gender.setText(result[6])
        gender = cur.execute(
            '''SELECT title FROM Classes WHERE classId=?''', (result[5],)
        ).fetchone()[0]
        self.ledit_class.setText(gender)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Student_Form()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())