import sqlite3

titles_of_classes = ['10А', '10Б', '10В', '10Г', '10Д',
                     '11А', '11Б', '11В', '11Г', '11Д',
                     '9А', '9Б', '9В', '9Г', '9Д',
                     '8А', '8Б', '8В', '8Г', '8Д',
                     '7А', '7Б', '7В', '7Г']

user_inx_surname = 1
user_inx_name = 2
user_inx_fathername = 3
user_inx_code = 4
user_inx_classid = 5
user_inx_gender = 6
user_inx_password = 7
user_inx_login = 8
user_inx_desirest = 9
user_inx_served = 10
user_inx_act = 11


def get_users_info(login):
    con = sqlite3.connect('duty_db.sqlite')
    cur = con.cursor()
    result = cur.execute(
        '''SELECT * FROM Users WHERE login=?''', (login,)
    ).fetchone()
    con.close()
    return result


def get_class_id(clas):
    con = sqlite3.connect('duty_db.sqlite')
    cur = con.cursor()
    result = cur.execute(
        '''SELECT classId FROM Classes WHERE title=?''', (clas,)
    ).fetchone()
    con.close()
    return result[0]


def get_class_title(classid):
    con = sqlite3.connect('duty_db.sqlite')
    cur = con.cursor()
    result = cur.execute(
        '''SELECT title FROM Classes WHERE classId=?''', (classid,)
    ).fetchone()
    con.close()
    return result[0]


def get_students(classid):
    con = sqlite3.connect('duty_db.sqlite')
    cur = con.cursor()
    result = cur.execute(
        '''SELECT * FROM Users WHERE classId=? AND status=?''', (classid, 0,)
    ).fetchall()
    con.close()
    res_arr = sorted(result, key=lambda x: int(x[user_inx_served]))
    res_arr = sorted(res_arr, key=lambda x: x[user_inx_desirest],reverse=True)
    return res_arr



def users_get_class_id(login):
    result = get_users_info(login)
    return get_class_title(result[user_inx_classid])


def get_day_of_duty(classid):
    con = sqlite3.connect('duty_db.sqlite')
    cur = con.cursor()
    result = cur.execute(
        '''SELECT date FROM Dutys WHERE classId=? AND passed='0' ''', (classid,)
    ).fetchall()
    con.close()
    return result


def get_near_day_of_duty(classid):
    arr = get_day_of_duty(classid)
    arr = [i[0] for i in arr]
    res_arr = []
    if arr:
        for i in arr:
            i = [int(j) for j in i.split()][::-1]
            res_arr.append(i)
        res_arr.sort()
        return ' '.join([str(i) for i in res_arr[0]][::-1])
    return '-'


def get_teachers_act(classid):
    con = sqlite3.connect('duty_db.sqlite')
    cur = con.cursor()
    result = cur.execute(
        '''SELECT act FROM Users WHERE login=(SELECT loginTeacher FROM Classes WHERE classId = ?)''', (classid,)
    ).fetchone()
    return result

# def make_array_of_studs(classid):
#
