import sqlite3
from constants import *

con = sqlite3.connect('duty_db.sqlite')
cur = con.cursor()


def us_get_class_id_by_class_title(class_title):
    class_id = cur.execute(
        '''SELECT classId FROM Classes WHERE title = ?''', (class_title,)
    ).fetchone()[0]
    return class_id


def us_is_login_unique(login):
    result = cur.execute(
        '''SELECT * FROM Users WHERE login=?''', (login,)
    ).fetchone()
    return result is None


def cl_is_exist_teacher(class_id):
    loginteacher = cur.execute(
        '''SELECT loginTeacher FROM Classes WHERE classId = ?''', (class_id,)
    ).fetchone()[0]
    return not (loginteacher is None)


def us_add_user(surname, name, fathername,
                code, class_id, gender, password, login):
    cur.execute(
        '''INSERT INTO Users
        (surname,name, patronymic,status,classId,gender,password,login, desireSt, served)
         VALUES(?,?,?,?,?,?,?,?,?,?)''',
        (surname, name, fathername, code,
         class_id, gender, password, login, base_desireSt, base_served)
    ).fetchall()
    con.commit()


def cl_add_class_teacher_login(login, class_id):
    cur.execute('''UPDATE Classes SET loginTeacher = ? WHERE classId = ?''',
                (login, class_id,))
    con.commit()
