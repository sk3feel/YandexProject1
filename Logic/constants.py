# Ключи словаря который используется при регистрации
Login = 'логин'
Surname = 'фамилия'
Name = 'имя'
Fathername = 'отчество'
Password = 'пароль'
Code = 'код пользователя'
Gender = 'гендер'
Class = 'класс'
ClassId = 'классId'

# Базовое значение desireSt
base_desireSt = False
not_base_desireSt = True
bid_desireSt = True

# Базовое значение served
base_served = 0

# Значения кодов пользователя
codes = ['0', '1', '2']
no_login_teacher = ''

student_cod = '0'
teacher_cod = '1'
admin_cod = '2'
no_class = 'нет'

# Коды пользователей
int_student_cod = 0
int_teacher_cod = 1
int_admin_cod = 2

# При селекте всех элементов таблицы Users соответствующие индексы
us_inx_surname = 1
us_inx_name = 2
us_inx_fathername = 3
us_inx_code = 4
us_inx_classid = 5
us_inx_gender = 6
us_inx_password = 7
us_inx_login = 8
us_inx_desirest = 9
us_inx_served = 10
us_inx_act = 11

# При селекте всех элементов таблицы Dutys соответствующие индексы
d_inx_date = 0
d_inx_class_id = 1

# Базовые и не базовые значения Pass в таблице Dutys
base_date_status = False
not_base_date_status = True

# Базовые и не базовые значения act в таблице Users
base_act = False
not_base_act = True

# Cписок классов
titles_of_classes = ['10А', '10Б', '10В', '10Г', '10Д',
                     '11А', '11Б', '11В', '11Г', '11Д',
                     '9А', '9Б', '9В', '9Г', '9Д',
                     '8А', '8Б', '8В', '8Г', '8Д',
                     '7А', '7Б', '7В', '7Г']

# Дни недели
title_of_baddays = [
    'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'нет'
]

# Значения в базе данных
USERS = 'Users'
DUTYS = 'Dutys'
CLASSES = 'Classes'

USER_ID = 'UserId'
SURNAME = 'surname'
NAME = 'name'
FATHERNAME = 'patronymic'
STATUS = 'status'
CLASS_ID = 'classId'
GENDER = 'gender'
PASSWORD = 'password'
LOGIN = 'login'
DESIRE_ST = 'desireSt'
SERVED = 'served'
ACT = 'act'
DATE = 'date'
PASSED = 'passed'
TITLE = 'title'
LOGIN_TEACHER = 'loginTeacher'
BAD_DAYS = 'baddays'

TABLES = {
    USERS: [USER_ID, SURNAME, NAME, FATHERNAME, STATUS, CLASS_ID,
            GENDER, PASSWORD, LOGIN, DESIRE_ST, SERVED, ACT],
    DUTYS: [DATE, CLASS_ID, PASSED],
    CLASSES: [CLASS_ID, TITLE, LOGIN_TEACHER, BAD_DAYS]
}

NEW_SIZE_IMAGE = [100, 100]
IMAGE_POSITION = [25, 52]
IMAGE = 'pict.png'
NEW_IMAGE = 'new_pict.png'

# Значение не определено
UNDEFINED = None

# Именя UI файлов
LOGIN_UI_FILE = '../Designs/A12_login_form.ui'
REGISTRATION_UI_FILE = '../Designs/A12_register_widget.ui'
STUDENT_UI_FILE = '../Designs/A12_student_form.ui'
TEACHER_UI_FILE = '../Designs/A12_teacher_form.ui'
ADMIN_UI_FILE = '../Designs/A12_admin_form.ui'
