import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QInputDialog

from Py_Designs.A12_teacher_form_ui import Ui_MainWindow

from routine_functions import *
from messages import *
from base_db_functions import *

# Очень окальные константы
login_inx = 4
login_inx_in_line = -1

one_studens = 1
two_studens = 2
three_studens = 3

first_st = 'first'
sec_st = 'second'
third_st = 'third'


class Teacher_Form(QMainWindow,Ui_MainWindow):
    def __init__(self, login):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi(TEACHER_UI_FILE, self)
        self.setWindowTitle(DUTY_MANAGER)
        self.login = login
        # Страница 1: выбор дежурных
        self.array_lines_of_studs, self.near_duty_day, self.classid = UNDEFINED, UNDEFINED, UNDEFINED
        self.duty_positions = {first_st: '', sec_st: '', third_st: ''}
        self.connnect_buttons()
        self.load_date_of_near_duty()
        self.get_arr_of_want_studs()
        self.load_free_ledits()
        self.show_act_students()
        # Страница 2: личные данные
        self.load_info_about_user()
        # Страница 3: Неудобные дни
        self.load_badday()
        self.btn_pick_bad_day.clicked.connect(self.pick_badday)
        # Страница 4: утвержденные дежурства
        self.load_approved_dutys()

    # Страница 1: выбор дежурных
    def connnect_buttons(self):
        self.btn_1_st.clicked.connect(self.pick_student)
        self.btn_2_st.clicked.connect(self.pick_student)
        self.btn_3_st.clicked.connect(self.pick_student)
        self.btn_accept.clicked.connect(self.accept)
        self.btn_end.clicked.connect(self.change_date)

    def load_date_of_near_duty(self):
        self.ledit_day_month.setEnabled(False)
        self.classid = select_one_with_aspect(USERS, LOGIN, self.login, CLASS_ID)[0]
        all_duty_days = select_all_with_two_aspects \
            (DUTYS, CLASS_ID, self.classid, PASSED, base_date_status, DATE)
        if all_duty_days:
            self.near_duty_day = get_near_day_of_duty(all_duty_days)
            self.ledit_day_month.setText(self.near_duty_day)
        else:
            self.near_duty_day = EMPTYNESS
            self.ledit_day_month.setText('-')

    def check_duty_on_empty(self):
        if self.near_duty_day == EMPTYNESS:
            self.statusBar().showMessage(NO_STATED_DUTYS)
            return False
        return True

    def get_arr_of_want_studs(self):
        array_of_students = select_all_with_two_aspects(
            USERS, CLASS_ID, self.classid, STATUS, int_student_cod,
            SURNAME, NAME, SERVED, DESIRE_ST, LOGIN)
        array_of_students = sort_studends_by_dutys(array_of_students)
        array_studs = get_students_lines(array_of_students)
        self.array_lines_of_studs = array_studs

    def load_free_ledits(self):
        self.ledit_1st.setEnabled(False)
        self.ledit_3st.setEnabled(False)
        self.ledit_2st.setEnabled(False)
        self.ledit_1st.setText('-')
        self.ledit_3st.setText('-')
        self.ledit_2st.setText('-')

    def show_act_students(self):
        act_students = select_all_with_three_aspects(USERS, CLASS_ID, self.classid,
                                                     ACT, not_base_act,
                                                     STATUS, int_student_cod,
                                                     SURNAME, NAME, SERVED, DESIRE_ST, LOGIN)
        line_act_students = get_students_lines(act_students)
        n_studens = len(act_students)
        if n_studens >= one_studens:
            self.duty_positions[first_st] = act_students[0][login_inx]
            self.ledit_1st.setText(line_act_students[0])
        if n_studens >= two_studens:
            self.duty_positions[sec_st] = act_students[1][login_inx]
            self.ledit_2st.setText(line_act_students[1])
        if n_studens == three_studens:
            self.duty_positions[third_st] = act_students[2][login_inx]
            self.ledit_3st.setText(line_act_students[2])

    def pick_student(self):
        if self.check_duty_on_empty():
            line, ok_pressed = QInputDialog.getItem(self, PICK_STUDENT, WHICH_CLASS,
                                                    tuple(self.array_lines_of_studs), 0, False)
            if ok_pressed:
                login = line.split()[login_inx_in_line]
                if self.sender() == self.btn_1_st:
                    old_students_line = self.ledit_1st.text()
                    self.ledit_1st.setText(line)
                    self.duty_positions[first_st] = login
                elif self.sender() == self.btn_2_st:
                    old_students_line = self.ledit_2st.text()
                    self.ledit_2st.setText(line)
                    self.duty_positions[sec_st] = login
                else:
                    old_students_line = self.ledit_3st.text()
                    self.ledit_3st.setText(line)
                    self.duty_positions[third_st] = login
                self.delete_from_duty(old_students_line)

    def delete_from_duty(self, students_line):
        login = students_line.split(' ')[login_inx_in_line]
        update_aspect(USERS, ACT, base_act, LOGIN, login)

    def accept(self):
        if self.check_duty_on_empty():
            update_aspect(USERS, ACT, not_base_act, LOGIN, self.login)
            for key in self.duty_positions:
                login = self.duty_positions[key]
                if login != '':
                    update_aspect(USERS, ACT, not_base_act, LOGIN, login)

    def change_date(self):
        if self.check_duty_on_empty():
            d = self.duty_positions
            for key in d:
                login = d[key]
                if login != '':
                    update_aspect(USERS, DESIRE_ST, base_desireSt, LOGIN, login)
                    self.updates_and_discards(login)
            self.updates_and_discards(self.login)
            self.pass_day()
            self.discard_positions()
            self.load_date_of_near_duty()
            self.get_arr_of_want_studs()

    # Сброс параметра act, served(количество дежурств) +=1
    def updates_and_discards(self, login):
        last_served = select_one_with_aspect(USERS, LOGIN, login, SERVED)[0]
        update_aspect(USERS, SERVED, last_served + 1, LOGIN, login)
        update_aspect(USERS, ACT, base_act, LOGIN, login)

    def discard_positions(self):
        self.duty_positions = {
            first_st: '',
            sec_st: '',
            third_st: ''
        }
        self.load_free_ledits()

    def pass_day(self):
        update_aspect(DUTYS, PASSED, not_base_date_status, DATE, self.near_duty_day)

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

    # Страница 3: Неудобные дни
    def load_badday(self):
        badday = select_one_with_aspect(CLASSES, LOGIN_TEACHER, self.login, BAD_DAYS)[0]
        if badday:
            self.btn_pick_bad_day.setText(badday)
        else:
            pass

    def pick_badday(self):
        badday, ok_pressed = QInputDialog.getItem(
            self, PICK_BADDAY, WHICH_DAY,
            tuple(title_of_baddays), 0, False)
        if ok_pressed:
            if badday == NO:
                self.btn_pick_bad_day.setText(PICK_BADDAY)
                badday = EMPTY_LINE
            else:
                self.btn_pick_bad_day.setText(badday)
            update_aspect(CLASSES, BAD_DAYS, badday, LOGIN_TEACHER, self.login)

    # Страница 4: утвержденные дежурства
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
    ex = Teacher_Form('EKA')
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
