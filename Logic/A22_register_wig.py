import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5.QtWidgets import QInputDialog

from Py_Designs.A12_register_widget_ui import Ui_wgt_registr

from routine_functions import *
from messages import *

from base_db_functions import *


class Registr(QMainWindow, Ui_wgt_registr):
    def __init__(self):
        super().__init__()
        # uic.loadUi(REGISTRATION_UI_FILE, self)
        self.setupUi(self)
        self.setWindowTitle(REGISTRATION)
        self.btn_create_account.clicked.connect(self.create_account)
        self.btn_class.clicked.connect(self.pick_class)
        self.btn_sex.clicked.connect(self.pick_sex)
        self.clas, self.gender = EMPTY_LINE, EMPTY_LINE
        self.datas_dict = UNDEFINED

    # Создание аккаунта и далее необходимые для этого функции
    def create_account(self):
        self.load_data()
        if self.check_corr_datas():
            self.load_class_id_to_dict()
            if self.is_login_unique():
                if self.check_exist_class_teacher():
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
        title = self.datas_dict[Class]
        class_id = select_one_with_aspect(CLASSES, TITLE, title, CLASS_ID)[0]
        self.datas_dict[ClassId] = class_id

    def is_login_unique(self):
        login = self.datas_dict[Login]
        account = select_one_with_aspect(USERS, LOGIN, login, *TABLES[USERS])
        if account is None:
            return True
        self.statusBar().showMessage(LOGIN_EXIST)
        return False

    def check_exist_class_teacher(self):
        class_id = self.datas_dict[ClassId]
        class_teacher = select_one_with_aspect(CLASSES, CLASS_ID, class_id, LOGIN_TEACHER)[0]
        if self.datas_dict[Code] == teacher_cod and class_teacher is not None:
            self.statusBar().showMessage(CLASS_HAVE_TEACHER)
            return False
        return True

    def check_cod_and_class(self):
        if code_and_class_can_exist(self.datas_dict[Code], self.datas_dict[Class]):
            return True
        self.statusBar().showMessage(COD_NOT_FIT_TO_CLASS)
        return False

    def add_user(self):
        d = self.datas_dict
        insert_for_users(
            d[Surname], d[Name], d[Fathername], d[Code],
            d[ClassId], d[Gender], d[Password], d[Login], base_desireSt, base_served
        )

        self.statusBar().showMessage(ACCOUNT_CREATED)

    def add_class_teacher_if_code_1(self):
        login = self.datas_dict[Login]
        class_id = self.datas_dict[ClassId]
        if self.datas_dict[Code] == teacher_cod:
            update_aspect(CLASSES, LOGIN_TEACHER, login, CLASS_ID, class_id)

    def pick_class(self):
        clas, ok_pressed = QInputDialog.getItem(
            self, PICK_YOUR_CLASS, WHICH_CLASS,
            tuple([no_class] + titles_of_classes), 1, False)
        if ok_pressed:
            self.btn_class.setText(clas)
            self.clas = clas

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
