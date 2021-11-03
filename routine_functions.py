from constants import *
from function_bd import *


def check_dict_on_emptiness(dict):
    for key in dict:
        if dict[key] == '':
            return False
    return True


def get_class_id_by_login(login):
    classid = get_users_info_by_log(login)[us_inx_classid]
    return classid


def check_correct_status_code(code):
    return code in codes


def code_and_class_can_exist(code, clas):
    if (code != admin_cod and clas == no_class) \
            or (code == admin_cod and clas != no_class):
        return False
    return True


def get_class_title_by_log(login):
    result = get_users_info_by_log(login)
    return get_class_title_by_class_id(result[us_inx_classid])


def get_near_day_of_duty(arr):
    arr = [i[0] for i in arr]
    res_arr = []
    if arr:
        for i in arr:
            i = [int(j) for j in i.split()][::-1]
            res_arr.append(i)
        res_arr.sort()
        date = res_arr[0][::-1]
        for i in range(len(date)):
            if len(str(date[i])) == 1:
                date[i] = '0' + str(date[i])
            else:
                date[i] = str(date[i])
        return ' '.join(date)


def is_duty_in_date(date, date_and_classid):
    return any(list(map(lambda x: date in x, date_and_classid)))


def get_students_lines(arr):
    res_arr = []
    for surname, name, n, desire, login in arr:
        line = f'{surname} {name} - {n} дежурств, {login}'
        if desire:
            line = 'Хочет дежурить: ' + line
        else:
            line = 'Не хочет дежурить: ' + line
        res_arr.append(line)
    return res_arr


served_inx = 2


def sort_studends_by_dutys(arr):
    global served_inx
    return sorted(arr, key=lambda x: x[served_inx])
