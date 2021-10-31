import sys

from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QMainWindow

import sqlite3
from PyQt5.QtWidgets import QInputDialog

Login = 'логин'
Surname = 'фамилия'
Name = 'имя'
Fathername = 'отчество'
Password = 'пароль'
Code = 'код пользователя'
Gender = 'гендер'
Class = 'класс'
ClassId = 'классId'
base_desireSt = False
base_served = 0
codes = ['0', '1', '2']

student_cod = '0'
teacher_cod = '1'
admin_cod = '2'
no_class = 'нет'


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
        self.clas, self.gender = 0, 0

    def create_account(self):
        self.load_data()
        if self.check_corr_datas():
            if self.check_unique_login():
                class_id = self.get_class_id()
                self.datas_dict[ClassId] = class_id
                if self.check_exist_class_teacher(class_id):
                    if self.check_exist_class_teacher(class_id):
                        if self.check_cod_and_class():
                            self.add_user()
                            self.add_class_teacher()
                            self.con.close()
                            self.close()

    def pick_class(self):
        clas, ok_pressed = QInputDialog.getItem(
            self, "Выберите ваш класс", "Какой класс?",
            (
                no_class, '7А', '7Б', '7В', '7Г',
                '8А', '8Б', '8В', '8Г', '8Д',
                '9А', '9Б', '9В', '9Г', '9Д',
                '10А', '10Б', '10В', '10Г', '10Д',
                '11А', '11Б', '11В', '11Г', '11Д'
            ), 1, False)
        if ok_pressed:
            self.clas = clas
            self.btn_class.setText(clas)

    def pick_sex(self):
        gender, ok_pressed = QInputDialog.getItem(
            self, "Выберите ваш пол", "Какой пол?",
            ('Мужчина', 'Женщина', 'Не определился'), 0, False)
        if ok_pressed:
            self.gender = gender
            self.btn_sex.setText(gender)

    def load_data(self):
        self.datas_dict = {
            Login: self.ledit_login.text(),
            Surname: self.ledit_lastname.text(),
            Name: self.ledit_name.text(),
            Fathername: self.ledit_fathername.text(),
            Password: self.ledit_password.text()
        }
        # Код, класс и пол пока не добавляем в словарь, они подлежат другой проверке:
        #
        self.code = self.ledit_cod.text()

    def check_corr_datas(self):
        f = True
        d = self.datas_dict
        for key in d:
            if d[key] == '':
                f = False
        self.datas_dict[Code] = self.code
        self.datas_dict[Gender] = self.gender
        self.datas_dict[Class] = self.clas

        if self.code not in codes or self.gender == 0 or self.clas == 0:
            f = False

        if not f:
            self.statusBar().showMessage('Данные некорректны или не введены')
        return f

    def check_unique_login(self):
        result = self.cur.execute(
            '''SELECT * FROM Users WHERE login=?''', (self.datas_dict[Login],)
        ).fetchone()
        if not (result is None):
            self.statusBar().showMessage('Пользователь с таким логином уже существует')
        return result is None

    def get_class_id(self):
        class_id = self.cur.execute(
            '''SELECT classId FROM Classes WHERE title = ?''', (self.datas_dict[Class],)
        ).fetchone()[0]
        return class_id

    def check_exist_class_teacher(self, class_id):
        loginteacher = self.cur.execute(
            '''SELECT loginTeacher FROM Classes WHERE classId = ?''', (class_id,)
        ).fetchone()[0]

        if self.datas_dict[Code] == '1' and loginteacher != None:
            self.statusBar().showMessage('Этот класс уже имеет своего учителя')
            return False
        return True

    def check_cod_and_class(self):
        f = True
        if self.datas_dict[Code] != admin_cod and self.datas_dict[Class] == no_class:
            f = False
        if self.datas_dict[Code] == admin_cod and self.datas_dict[Class] != no_class:
            f = False
        if not f:
            self.statusBar().showMessage(
                'У пользователя с таким кодом не может быть указан данный класс')
        return f

    def add_user(self):
        d = self.datas_dict
        self.cur.execute(
            '''INSERT INTO Users
            (surname,name, patronymic,status,classId,gender,password,login, desireSt, served)
             VALUES(?,?,?,?,?,?,?,?,?,?)''',
            (d[Surname], d[Name], d[Fathername], d[Code],
             d[ClassId], d[Gender], d[Password], d[Login], base_desireSt, base_served)
        ).fetchall()
        self.con.commit()

    def add_class_teacher(self):
        if self.datas_dict[Code] == teacher_cod:
            self.cur.execute('''UPDATE Classes SET loginTeacher = ? WHERE classId = ?''',
                             (self.datas_dict[Login], self.datas_dict[ClassId],))
            self.con.commit()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Registr()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
