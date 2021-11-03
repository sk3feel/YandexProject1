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

from constants import *
from function_bd import *
from routine_functions import *


class Admin_Form(QMainWindow):
    def __init__(self, login):
        super().__init__()
        uic.loadUi('A12_admin_form.ui', self)
        self.setWindowTitle('DutyManager')
        self.login = login
        self.con = sqlite3.connect('duty_db.sqlite')
        self.cur = self.con.cursor()
        self.calendar.selectionChanged.connect(self.change_day_calendar)
        self.btn_make_duty.clicked.connect(self.make_duty)
        self.btn_pick_class.clicked.connect(self.pick_class)
        self.btn_reload_bd.clicked.connect(self.reload_bd)
        self.load_all_ledits_btns()
        self.reload_bd()
        self.load_info_about_user()

        self.self_date_in_db = None
        self.date_and_classid = None
        self.date = None
        self.clas = None
        self.date_and_classid = get_db_dutys()

    # Страница 1: выбор дежурных классов

    def make_duty(self):
        if self.date is None:
            self.statusBar().showMessage('Сначала нужно выбрать день')
        elif self.clas is None:
            self.statusBar().showMessage('Сначала нужно выбрать класс')
        else:
            self.reload_self_date_in_db()
            if self.self_date_in_db is True:
                self.change_class()
            elif self.self_date_in_db is False:
                self.put_class()



    def load_all_ledits_btns(self):
        self.date = None
        self.clas = None
        self.ledit_date.setEnabled(False)
        self.ledit_class.setEnabled(False)
        self.ledit_class.setText('---')
        self.ledit_date.setText('---')

    def reload_bd(self):
        self.date_and_classid = get_db_dutys()

    def reload_self_date_in_db(self):
        # self.reload_bd()
        if self.date is not None:
            self.self_date_in_db = is_duty_in_date(self.date, self.date_and_classid)
            return self.self_date_in_db
        else:
            return None

    def change_day_calendar(self):
        # self.reload_bd()
        dateselected = self.calendar.selectedDate()
        date_in_string = str(dateselected.toPyDate()).split('-')[::-1]
        self.date = ' '.join(date_in_string)
        self.ledit_date.setText(self.date)

        # обновление переменной self.self_date_in_db
        self.reload_self_date_in_db()

        # если дата в базе данных, вывести класс в ledit, в противно случае -
        if self.self_date_in_db:
            self.ledit_class.setText(d_get_class_title_by_date(self.date))
        else:
            self.ledit_class.setText('-')

    def pick_class(self):
        clas, ok_pressed = QInputDialog.getItem(
            self, "Выберите класс", "Какой класс?",
            tuple(funsions.titles_of_classes), 0, False)
        if ok_pressed:
            self.clas = clas
            self.btn_pick_class.setText(clas)

    def discard(self):
        self.ledit_class.setText(self.clas)
        self.clas = None
        self.btn_pick_class.setText('Выбрать класс')

    def change_class(self):
        change_class_in_date(get_class_id_by_class_title(self.clas), self.date, base_date_status)
        self.discard()

    def put_class(self):
        put_class_in_date(self.date, get_class_id_by_class_title(self.clas), base_date_status)
        self.discard()

    # Страница 2: личные данные
    def load_info_about_user(self):
        info_array = get_users_info_by_log(self.login)
        self.ledit_login.setEnabled(False)
        self.ledit_surname.setEnabled(False)
        self.ledit_name.setEnabled(False)
        self.ledit_fathername.setEnabled(False)
        self.ledit_gender.setEnabled(False)
        self.ledit_login.setText(info_array[us_inx_login])
        self.ledit_surname.setText(info_array[us_inx_surname])
        self.ledit_name.setText(info_array[us_inx_name])
        self.ledit_fathername.setText(info_array[us_inx_fathername])
        self.ledit_gender.setText(info_array[us_inx_gender])

    # Страница 3: утвержденные дежурства


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Admin_Form('YG')
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
