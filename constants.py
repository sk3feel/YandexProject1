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
bid_desireSt = True
base_served = 0
codes = ['0', '1', '2']

student_cod = '0'
teacher_cod = '1'
admin_cod = '2'
no_class = 'нет'

int_student_cod = 0
int_teacher_cod = 1
int_admin_cod = 2

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

d_inx_date = 0
d_inx_class_id = 1

base_date_status = False

titles_of_classes = ['10А', '10Б', '10В', '10Г', '10Д',
                     '11А', '11Б', '11В', '11Г', '11Д',
                     '9А', '9Б', '9В', '9Г', '9Д',
                     '8А', '8Б', '8В', '8Г', '8Д',
                     '7А', '7Б', '7В', '7Г']

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
SERVER = 'served'
ACT = 'act'
DATE = 'date'
PASSED = 'passed'
TITLE = 'title'
LOGIN_TEACHER = 'loginTeacher'
BAD_DAYS = 'baddays'

TABLES = {
    USERS: [USER_ID, SURNAME, NAME, FATHERNAME, STATUS, CLASS_ID,
            GENDER, PASSWORD, LOGIN, DESIRE_ST, SERVER, ACT],
    DUTYS: [DATE, CLASS_ID, PASSED],
    CLASSES: [CLASS_ID, TITLE, LOGIN_TEACHER, BAD_DAYS]
}


