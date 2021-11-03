import sqlite3
from constants import *

con = sqlite3.connect('duty_db.sqlite')
cur = con.cursor()


# def select_table(table_name, **fields):
#     value = f"""SELECT {', '.join(fields)} FROM {table_name}"""
#     return cur.execute(value).fetchall()
#
# def select_one_with_aspect(table_name,field,field_value,*fields):
#     value = f"""SELECT {', '.join(fields)} FROM {table_name} WHERE{field}=?"""
#     return cur.execute(value,(field_value,)).fetchone()
#
# def select_all_with_aspect(table_name,field,field_value,*fields):
#     value = f"""SELECT {', '.join(fields)} FROM {table_name} WHERE{field}=?"""
#     return cur.execute(value,(field_value,)).fetchall()



def get_class_id_by_class_title(class_title):
    class_id = cur.execute(
        '''SELECT classId FROM Classes WHERE title = ?''', (class_title,)
    ).fetchone()[0]
    return class_id

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

def is_login_exist(login):
    result = cur.execute(
        '''SELECT * FROM Users WHERE login=?''', (login,)
    ).fetchone()
    if result is None:
        return False
    return True


def corr_password(login, password):
    result = cur.execute(
        '''SELECT * FROM Users WHERE login=?''', (login,)
    ).fetchone()
    if str(result[us_inx_password]) == str(password):
        return True


def get_users_info_by_log(login):
    result = cur.execute(
        '''SELECT * FROM Users WHERE login=?''', (login,)
    ).fetchone()
    return result


def get_class_title_by_class_id(classid):
    result = cur.execute(
        '''SELECT title FROM Classes WHERE classId=?''', (classid,)
    ).fetchone()
    return result[0]


def get_days_of_duty(classid):
    result = cur.execute(
        '''SELECT date FROM Dutys WHERE classId=? AND passed='0' ''', (classid,)
    ).fetchall()
    return result



def desire_true_by_login(login):
    cur.execute('''
            UPDATE Users SET desireSt=? WHERE login= ?''', (True, login,))
    con.commit()


def is_teacher_decided(classid):
    result = cur.execute(
        '''SELECT act FROM Users WHERE login=(SELECT loginTeacher FROM Classes WHERE classId = ?)''', (classid,)
    ).fetchone()
    if result[0]:
        return True
    return False


def get_db_dutys():
    res = cur.execute('''SELECT * FROM Dutys''').fetchall()
    return res


def change_class_in_date(clas, date, base):
    cur.execute('''
    UPDATE Dutys SET classId=? WHERE date = ?''', (clas, date,))
    con.commit()


def put_class_in_date(date, class_id, date_status):
    cur.execute(
        '''INSERT INTO Dutys
        (date, classId, passed)
         VALUES(?,?,?)''',
        (date, class_id, date_status,)
    ).fetchall()
    con.commit()

def d_get_class_title_by_date(date):
    result = cur.execute(
        '''SELECT classId FROM Dutys WHERE date=?''',
        (date,)
    ).fetchall()[0][0]
    class_title = get_class_title_by_class_id(result)
    return class_title
