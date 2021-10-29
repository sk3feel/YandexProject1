import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import csv
import sqlite3
from PyQt5.QtWidgets import QInputDialog
import funsions


class Registr(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('A12_register_widget.ui', self)
        self.setWindowTitle('Регистрация')
        self.btn_create_account.clicked.connect(self.create_account)
        self.btn_class.clicked.connect(self.pick_class)
        self.btn_sex.clicked.connect(self.pick_sex)
        self.clas, self.gender = 0, 0

    def pick_class(self):
        clas, ok_pressed = QInputDialog.getItem(
            self, "Выберите ваш класс", "Какой класс?",
            (
                '7А', '7Б', '7В', '7Г',
                '8А', '8Б', '8В', '8Г', '8Д',
                '9А', '9Б', '9В', '9Г', '9Д',
                '10А', '10Б', '10В', '10Г', '10Д',
                '11А', '11Б', '11В', '11Г', '11Д'
            ), 0, False)
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

    def create_account(self):
        self.login = self.ledit_login.text()

        if self.login != funsions.check_login(self.login):
            self.statusBar().showMessage(funsions.check_login(self.login))
            return None

        self.code = self.ledit_cod.text()

        if self.code != funsions.check_code(self.code):
            self.statusBar().showMessage(funsions.check_code(self.code))
            return None

        self.surname = self.ledit_lastname.text()

        if self.surname != funsions.check_surname(self.surname):
            self.statusBar().showMessage(funsions.check_surname(self.surname))
            return None

        self.name = self.ledit_name.text()

        if self.name != funsions.check_name(self.name):
            self.statusBar().showMessage(funsions.check_name(self.name))
            return None

        self.fathername = self.ledit_fathername.text()

        if self.fathername != funsions.check_fathername(self.fathername):
            self.statusBar().showMessage(funsions.check_fathername(self.fathername))
            return None

        self.password = self.ledit_password.text()

        if self.password != funsions.check_pass(self.password):
            self.statusBar().showMessage(funsions.check_pass(self.password))
            return None

        if self.code == '2':
            self.clas = -1
            self.btn_class.setText('админ')

        if self.clas == 0:
            self.statusBar().showMessage('Вы не выбрали класс')
            return None

        if self.gender == 0:
            self.statusBar().showMessage('Вы не выбрали пол')
            return None

        con = sqlite3.connect('duty_db.sqlite')
        cur = con.cursor()

        # для проверки на одинаковый логин
        result = cur.execute(
            '''SELECT * FROM Users WHERE login=?''', (self.login,)
        ).fetchone()

        if result is None:
            if self.clas != -1:
                class_id = cur.execute(
                    '''SELECT classId FROM Classes WHERE title = ?''', (self.clas,)
                ).fetchone()[0]
            else:
                class_id = 25

            loginTeacher = cur.execute(
                '''SELECT loginTeacher FROM Classes WHERE classId = ?''', (class_id,)
            ).fetchone()[0]


            if not (self.code == '1' and loginTeacher != None):
                cur.execute(
                    '''INSERT INTO Users
                    (surname,name, patronymic,status,classId,gender,password,login, desireSt)
                     VALUES(?,?,?,?,?,?,?,?,?)''',
                    (self.surname, self.name, self.fathername, self.code,
                     class_id, self.gender, self.password, self.login, False,)
                ).fetchall()
                con.commit()

                if self.code == '1':
                    cur.execute(
                        '''UPDATE Classes SET loginTeacher = ? WHERE classId = ?''', (self.login, class_id,)
                    )

                    con.commit()

                con.close()
                self.statusBar().showMessage('Вы успешно создали аккаунт')
                self.close()
            else:
                self.statusBar().showMessage('Классный руководитель этого класса уже зарегистрирован')
                con.close()
        else:
            self.statusBar().showMessage('Пользователь с таким логином уже существует')
            con.close()



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Registr()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
