import sqlite3

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
        '''SELECT * FROM Users WHERE classId=?''', (classid,)
    ).fetchall()
    con.close()
    res_arr = []
    for i in result:
        pass
    return result


print(get_students(1))



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

