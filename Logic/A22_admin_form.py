import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QInputDialog

from Py_Designs.A12_admin_form_ui import Ui_MainWindow

from routine_functions import *

from messages import *

from base_db_functions import *


class Admin_Form(QMainWindow, Ui_MainWindow):
    def __init__(self, login):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi(ADMIN_UI_FILE, self)
        self.setWindowTitle(DUTY_MANAGER)
        self.login = login
        # Страница 1: выбор дежурных классов
        self.self_date_in_db, self.date_and_classid, self.date, self.clas = \
            UNDEFINED, UNDEFINED, UNDEFINED, UNDEFINED,
        self.calendar.selectionChanged.connect(self.change_day_calendar)
        self.btn_make_duty.clicked.connect(self.make_duty)
        self.btn_pick_class.clicked.connect(self.pick_class)
        self.load_all_ledits_btns()
        self.reload_bd()
        self.load_table_of_baddays()
        # self.date_and_classid = self.get_db_dutys()
        # Страница 2: личные данные
        self.load_info_about_user()
        # Страница 3: утвержденные дежурства
        self.load_approved_dutys()

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
        self.ledit_date.setEnabled(False)
        self.ledit_class.setEnabled(False)
        self.ledit_class.setText('---')
        self.ledit_date.setText('---')

    def load_table_of_baddays(self):
        title_inx = 0
        login_teacher_inx = 1
        classes_and_teach_logins = select_table(CLASSES, TITLE, LOGIN_TEACHER)
        classes_and_teach_logins = list(filter(lambda x: x[login_teacher_inx] != UNDEFINED, classes_and_teach_logins))
        self.tblwg_n_baddays.setRowCount(len(classes_and_teach_logins))
        tablerow = 0
        for row in classes_and_teach_logins:
            title = row[title_inx]
            teach_login = row[login_teacher_inx]
            served = select_one_with_aspect(USERS, LOGIN, teach_login, SERVED)[0]
            bad_day = select_one_with_aspect(CLASSES, LOGIN_TEACHER, teach_login, BAD_DAYS)[0]
            self.tblwg_n_baddays.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(title))
            self.tblwg_n_baddays.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(served)))
            self.tblwg_n_baddays.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(bad_day))
            tablerow += 1

    # def get_db_dutys(self):
    #     return select_table(DUTYS, *TABLES[DUTYS])

    def reload_bd(self):
        self.date_and_classid = select_table(DUTYS, DATE, CLASS_ID)

    def reload_self_date_in_db(self):
        self.reload_bd()
        if self.date is not None:
            self.self_date_in_db = is_duty_in_date(self.date, self.date_and_classid)
            return self.self_date_in_db
        else:
            return None

    def change_day_calendar(self):
        dateselected = self.calendar.selectedDate()
        date_in_string = str(dateselected.toPyDate()).split('-')[::-1]
        self.date = ' '.join(date_in_string)
        self.ledit_date.setText(self.date)

        # обновление переменной self.self_date_in_db
        self.reload_self_date_in_db()

        # если дата в базе данных,  вывести класс в ledit, в противно случае -
        if self.self_date_in_db:
            class_id = select_one_with_aspect(DUTYS, DATE, self.date, CLASS_ID)[0]
            class_title = select_one_with_aspect(CLASSES, CLASS_ID, class_id, TITLE)[0]
            self.ledit_class.setText(class_title)
        else:
            self.ledit_class.setText(EMPTYNESS)

    def pick_class(self):
        clas, ok_pressed = QInputDialog.getItem(
            self, PICK_CLASS, WHICH_CLASS,
            tuple(titles_of_classes), 0, False)
        if ok_pressed:
            self.clas = clas
            self.btn_pick_class.setText(clas)

    def discard(self):
        self.ledit_class.setText(self.clas)
        self.clas = None
        self.btn_pick_class.setText(TO_PICK_CLASS)

    def change_class(self):
        class_id = select_one_with_aspect(CLASSES, TITLE, self.clas, CLASS_ID)[0]
        update_aspect(DUTYS, CLASS_ID, class_id, DATE, self.date)
        self.discard()

    def put_class(self):
        class_id = select_one_with_aspect(CLASSES, TITLE, self.clas, CLASS_ID)[0]
        insert_for_dutys(self.date, class_id, base_date_status)
        self.discard()

    # Страница 2: личные данные
    def load_info_about_user(self):
        info_array = select_one_with_aspect(USERS, LOGIN, self.login, *TABLES[USERS])
        self.ledit_login.setEnabled(False)
        self.ledit_surname.setEnabled(False)
        self.ledit_name.setEnabled(False)
        self.ledit_fathername.setEnabled(False)
        self.ledit_gender.setEnabled(False)

        self.ledit_login.setText(str(info_array[us_inx_login]))
        self.ledit_surname.setText(str((info_array[us_inx_surname])))
        self.ledit_name.setText(str(info_array[us_inx_name]))
        self.ledit_fathername.setText(str(info_array[us_inx_fathername]))
        self.ledit_gender.setText(str(info_array[us_inx_gender]))

    # Страница 3: утвержденные дежурства
    def load_approved_dutys(self):
        dates = sort_days(select_table(DUTYS, DATE))
        self.tablewdt_dutys.setRowCount(len(dates))
        tablerow = 0
        for date in dates:
            class_id = select_one_with_aspect(DUTYS, DATE, date, CLASS_ID)[0]
            class_title = select_one_with_aspect(CLASSES, CLASS_ID, class_id, TITLE)[0]
            self.tablewdt_dutys.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(date))
            self.tablewdt_dutys.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(class_title))
            tablerow += 1


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Admin_Form('ADMIN')
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
