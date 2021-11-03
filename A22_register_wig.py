import sys

from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5.QtWidgets import QInputDialog
from function_bd import *
from routine_functions import *

from messages import *

class Registr(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('A12_register_widget.ui', self)
        self.setWindowTitle(REGISTRATION)
        self.btn_create_account.clicked.connect(self.create_account)
        self.btn_class.clicked.connect(self.pick_class)
        self.btn_sex.clicked.connect(self.pick_sex)
        self.clas, self.gender = '', ''

    # Создание аккаунта и далее необходимые для этого функции
    def create_account(self):
        self.load_data()
        if self.check_corr_datas():
            self.load_class_id_to_dict()
            if self.is_login_unique(self.datas_dict[Login]):
                if self.check_exist_class_teacher(self.datas_dict[ClassId]):
                    if self.check_cod_and_class():
                        self.add_user()
                        self.add_class_teacher_if_code_1()
                        self.close()

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
        self.statusBar().showMessage(WRONG_DATAS)
        return False

    def load_class_id_to_dict(self):
        class_id = get_class_id_by_class_title(self.datas_dict[Class])
        self.datas_dict[ClassId] = class_id

    def is_login_unique(self, login):
        if us_is_login_unique(login):
            return True
        self.statusBar().showMessage(LOGIN_EXIST)
        return False

    def check_exist_class_teacher(self, class_id):
        if self.datas_dict[Code] == teacher_cod and cl_is_exist_teacher(class_id):
            self.statusBar().showMessage(CLASS_HAVE_TEACHER)
            return False
        return True

    def check_cod_and_class(self):
        if code_and_class_can_exist(self.datas_dict[Code], self.datas_dict[Class]):
            return True
        self.statusBar().showMessage(
            COD_NOT_FIT_TO_CLASS)
        return False

    def add_user(self):
        d = self.datas_dict
        us_add_user(d[Surname], d[Name], d[Fathername], d[Code],
                    d[ClassId], d[Gender], d[Password], d[Login])
        self.statusBar().showMessage(ACCOUNT_CREATED)

    def add_class_teacher_if_code_1(self):
        if self.datas_dict[Code] == teacher_cod:
            cl_add_class_teacher_login(self.datas_dict[Login], self.datas_dict[ClassId])

    # Выбор класса
    def pick_class(self):
        clas, ok_pressed = QInputDialog.getItem(
            self, PICK_YOUR_CLASS, WHICH_CLASS,
            tuple([no_class] + titles_of_classes), 1, False)
        if ok_pressed:
            self.btn_class.setText(clas)
            self.clas = clas

    # Выбор пола
    def pick_sex(self):
        gender, ok_pressed = QInputDialog.getItem(
            self, PICK_YOUR_GENDER, WHICH_GENDER,
            (MALE, FEMALE, DONT_KNOW), 0, False)
        if ok_pressed:
            self.btn_sex.setText(gender)
            self.gender = gender


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Registr()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
# import sys
#
# from PyQt5 import uic
#
# from PyQt5.QtWidgets import QApplication, QMainWindow
#
# import sqlite3
# from PyQt5.QtWidgets import QInputDialog
# import funsions
#
# Login = 'логин'
# Surname = 'фамилия'
# Name = 'имя'
# Fathername = 'отчество'
# Password = 'пароль'
# Code = 'код пользователя'
# Gender = 'гендер'
# Class = 'класс'
# ClassId = 'классId'
# base_desireSt = False
# base_served = 0
# codes = ['0', '1', '2']
#
# student_cod = '0'
# teacher_cod = '1'
# admin_cod = '2'
# no_class = 'нет'
#
#
# class Registr(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi('A12_register_widget.ui', self)
#         self.setWindowTitle('Регистрация')
#         self.btn_create_account.clicked.connect(self.create_account)
#         self.btn_class.clicked.connect(self.pick_class)
#         self.btn_sex.clicked.connect(self.pick_sex)
#         self.con = sqlite3.connect('duty_db.sqlite')
#         self.cur = self.con.cursor()
#         self.clas, self.gender = 0, 0
#
#     def create_account(self):
#         self.load_data()
#         if self.check_corr_datas():
#             if self.check_unique_login():
#                 class_id = self.get_class_id()
#                 self.datas_dict[ClassId] = class_id
#                 if self.check_exist_class_teacher(class_id):
#                     if self.check_exist_class_teacher(class_id):
#                         if self.check_cod_and_class():
#                             self.add_user()
#                             self.add_class_teacher()
#                             self.con.close()
#                             self.close()
#
#     def pick_class(self):
#         clas, ok_pressed = QInputDialog.getItem(
#             self, "Выберите ваш класс", "Какой класс?",
#             tuple([no_class] + funsions.titles_of_classes), 1, False)
#         if ok_pressed:
#             self.clas = clas
#             self.btn_class.setText(clas)
#
#     def pick_sex(self):
#         gender, ok_pressed = QInputDialog.getItem(
#             self, "Выберите ваш пол", "Какой пол?",
#             ('Мужчина', 'Женщина', 'Не определился'), 0, False)
#         if ok_pressed:
#             self.gender = gender
#             self.btn_sex.setText(gender)
#
#     def load_data(self):
#         self.datas_dict = {
#             Login: self.ledit_login.text(),
#             Surname: self.ledit_lastname.text(),
#             Name: self.ledit_name.text(),
#             Fathername: self.ledit_fathername.text(),
#             Password: self.ledit_password.text()
#         }
#         # Код, класс и пол пока не добавляем в словарь, они подлежат другой проверке:
#         #
#         self.code = self.ledit_cod.text()
#
#     def check_corr_datas(self):
#         f = True
#         d = self.datas_dict
#         for key in d:
#             if d[key] == '':
#                 f = False
#         self.datas_dict[Code] = self.code
#         self.datas_dict[Gender] = self.gender
#         self.datas_dict[Class] = self.clas
#
#         if self.code not in codes or self.gender == 0 or self.clas == 0:
#             f = False
#
#         if not f:
#             self.statusBar().showMessage('Данные некорректны или не введены')
#         return f
#
#     def check_unique_login(self):
#         result = self.cur.execute(
#             '''SELECT * FROM Users WHERE login=?''', (self.datas_dict[Login],)
#         ).fetchone()
#         if not (result is None):
#             self.statusBar().showMessage('Пользователь с таким логином уже существует')
#         return result is None
#
#     def get_class_id(self):
#         class_id = self.cur.execute(
#             '''SELECT classId FROM Classes WHERE title = ?''', (self.datas_dict[Class],)
#         ).fetchone()[0]
#         return class_id
#
#     def check_exist_class_teacher(self, class_id):
#         loginteacher = self.cur.execute(
#             '''SELECT loginTeacher FROM Classes WHERE classId = ?''', (class_id,)
#         ).fetchone()[0]
#
#         if self.datas_dict[Code] == '1' and loginteacher != None:
#             self.statusBar().showMessage('Этот класс уже имеет своего учителя')
#             return False
#         return True
#
#     def check_cod_and_class(self):
#         f = True
#         if self.datas_dict[Code] != admin_cod and self.datas_dict[Class] == no_class:
#             f = False
#         if self.datas_dict[Code] == admin_cod and self.datas_dict[Class] != no_class:
#             f = False
#         if not f:
#             self.statusBar().showMessage(
#                 'У пользователя с таким кодом не может быть указан данный класс')
#         return f
#
#     def add_user(self):
#         d = self.datas_dict
#         self.cur.execute(
#             '''INSERT INTO Users
#             (surname,name, patronymic,status,classId,gender,password,login, desireSt, served)
#              VALUES(?,?,?,?,?,?,?,?,?,?)''',
#             (d[Surname], d[Name], d[Fathername], d[Code],
#              d[ClassId], d[Gender], d[Password], d[Login], base_desireSt, base_served)
#         ).fetchall()
#         self.con.commit()
#
#     def add_class_teacher(self):
#         if self.datas_dict[Code] == teacher_cod:
#             self.cur.execute('''UPDATE Classes SET loginTeacher = ? WHERE classId = ?''',
#                              (self.datas_dict[Login], self.datas_dict[ClassId],))
#             self.con.commit()
#
#
# def except_hook(cls, exception, traceback):
#     sys.__excepthook__(cls, exception, traceback)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Registr()
#     ex.show()
#     sys.excepthook = except_hook
#     sys.exit(app.exec_())
