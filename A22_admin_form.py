import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QInputDialog
import sqlite3
import funsions

inx_surname = 1
inx_name = 2
inx_fathername = 3
inx_clas = 5
inx_gender = 6
inx_login = 8

inx_date_dutys = 0
inx_classID_dutys = 1


class Admin_Form(QMainWindow):
    def __init__(self, login):
        super().__init__()
        uic.loadUi('A12_admin_form.ui', self)
        self.setWindowTitle('DutyManager')
        self.ok_pressed = False
        self.login = login
        self.con = sqlite3.connect('duty_db.sqlite')
        self.cur = self.con.cursor()
        self.calendar.selectionChanged.connect(self.change_day_calendar)
        self.btn_make_duty.clicked.connect(self.make_duty)
        self.btn_pick_class.clicked.connect(self.pick_class)
        self.btn_reload_bd.clicked.connect(self.reload_bd)
        self.load_ledits()
        self.reload_bd()
        self.initUI()

    # Страница 2: личные данные
    def initUI(self):
        result = funsions.get_users_info(self.login)
        self.ledit_login.setEnabled(False)
        self.ledit_surname.setEnabled(False)
        self.ledit_name.setEnabled(False)
        self.ledit_fathername.setEnabled(False)
        self.ledit_gender.setEnabled(False)

        self.ledit_login.setText(result[funsions.user_inx_login])
        self.ledit_surname.setText(result[funsions.user_inx_surname])
        self.ledit_name.setText(result[funsions.user_inx_name])
        self.ledit_fathername.setText(result[funsions.user_inx_fathername])
        self.ledit_gender.setText(result[funsions.user_inx_gender])

    # Страница 1: выбор дежурных классов

    def load_ledits(self):
        self.date = None
        self.clas = None
        self.ledit_date.setEnabled(False)
        self.ledit_class.setEnabled(False)
        self.ledit_class.setText('---')
        self.ledit_date.setText('---')

    def reload_bd(self):
        self.date_and_classid = self.cur.execute(
            '''SELECT * FROM Dutys'''
        ).fetchall()

    def change_day_calendar(self):
        dateselected = self.calendar.selectedDate()
        date_in_string = str(dateselected.toPyDate()).split('-')[::-1]
        self.date = ' '.join(date_in_string)
        self.ledit_date.setText(self.date)

        self.date_in_db = any(list(map(lambda x: self.date in x, self.date_and_classid)))
        if self.date_in_db:
            for i in self.date_and_classid:
                if self.date in i:
                    self.ledit_class.setText(funsions.get_class_title(i[inx_classID_dutys]))
        else:
            self.ledit_class.setText('-')

    def pick_class(self):
        clas, self.ok_pressed = QInputDialog.getItem(
            self, "Выберите класс", "Какой класс?",
            (
                '10А', '10Б', '10В', '10Г', '10Д',
                '11А', '11Б', '11В', '11Г', '11Д',
                '9А', '9Б', '9В', '9Г', '9Д',
                '8А', '8Б', '8В', '8Г', '8Д',
                '7А', '7Б', '7В', '7Г'
            ), 0, False)
        if self.ok_pressed:
            self.clas = clas
            self.btn_pick_class.setText(clas)

    def discard(self):
        self.ledit_class.setText(self.clas)
        self.clas = None
        self.btn_pick_class.setText('Выбрать класс')

    def change_class(self):
        self.cur.execute('''
        UPDATE Dutys SET classId=? WHERE date = ?''', (funsions.get_class_id(self.clas), self.date,))
        self.con.commit()

    def put_class(self):
        self.cur.execute(
            '''INSERT INTO Dutys
            (date, classId, passed)
             VALUES(?,?,?)''',
            (self.date, funsions.get_class_id(self.clas), False,)
        ).fetchall()
        self.con.commit()
        self.discard()

    def make_duty(self):
        if self.date is None:
            self.statusBar().showMessage('Сначала нужно выбрать день')
        elif not self.ok_pressed:
            self.statusBar().showMessage('Сначала нужно выбрать класс')
        else:
            if self.date_in_db:
                self.change_class()
            else:
                self.put_class()

    # Страница 3: утвержденные дежурства


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Admin_Form('YG')
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
