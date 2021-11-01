import sys

from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QMainWindow

import sqlite3
from PyQt5.QtWidgets import QInputDialog
import funsions
from constants import *
from function_bd import *
from routine_functions import *


class Registr(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('A12_register_widget.ui', self)
        self.setWindowTitle('Регистрация')
        self.btn_create_account.clicked.connect(self.create_account)
        self.btn_class.clicked.connect(self.pick_class)
        self.btn_sex.clicked.connect(self.pick_sex)
        self.con = sqlite3.connect('duty_db.sqlite')
        self.cur = self.con.cursor()
        self.clas, self.gender = '', ''

    def create_account(self):
        self.load_data()
        if self.check_corr_datas():
            self.load_class_id_to_dict()
            if us_is_login_unique(self.datas_dict[Login]):
                if self.check_exist_class_teacher(self.datas_dict[ClassId]):
                    if self.check_cod_and_class():
                        self.add_user()
                        self.add_class_teacher_if_code_1()

    def pick_class(self):
        clas, ok_pressed = QInputDialog.getItem(
            self, "Выберите ваш класс", "Какой класс?",
            tuple([no_class] + titles_of_classes), 1, False)
        if ok_pressed:
            self.btn_class.setText(clas)
            self.clas = clas

    def pick_sex(self):
        gender, ok_pressed = QInputDialog.getItem(
            self, "Выберите ваш пол", "Какой пол?",
            ('Мужчина', 'Женщина', 'Не определился'), 0, False)
        if ok_pressed:
            self.btn_sex.setText(gender)
            self.gender = gender

    def load_data(self):
        self.datas_dict = {
            Login: self.ledit_login.text(),
            Surname: self.ledit_lastname.text(),
            Name: self.ledit_name.text(),
            Fathername: self.ledit_fathername.text(),
            Password: self.ledit_password.text(),
            Code: self.ledit_cod.text(),
            Class: self.clas,
            Gender: self.gender
        }

    def check_corr_datas(self):
        if check_dict_on_emptiness(self.datas_dict) \
                and check_correct_status_code(self.datas_dict[Code]):
            return True
        self.statusBar().showMessage('Данные некорректны или не введены')
        return False

    def load_class_id_to_dict(self):
        class_id = us_get_class_id_by_class_title(self.datas_dict[Class])
        self.datas_dict[ClassId] = class_id

    def check_exist_class_teacher(self, class_id):
        if self.datas_dict[Code] == teacher_cod and cl_is_exist_teacher(class_id):
            self.statusBar().showMessage('Этот класс уже имеет своего учителя')
            return False
        return True

    def check_cod_and_class(self):
        if code_and_class_can_exist(self.datas_dict[Code], self.datas_dict[Class]):
            return True
        self.statusBar().showMessage(
            'У пользователя с таким кодом не может быть указан данный класс')
        return False

    def add_user(self):
        d = self.datas_dict
        us_add_user(d[Surname], d[Name], d[Fathername], d[Code],
                    d[ClassId], d[Gender], d[Password], d[Login])

    def add_class_teacher_if_code_1(self):
        if self.datas_dict[Code] == teacher_cod:
            cl_add_class_teacher_login(self.datas_dict[Login], self.datas_dict[ClassId])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Registr()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
