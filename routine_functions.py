from constants import *


def check_dict_on_emptiness(dict):
    for key in dict:
        if dict[key] == '':
            return False
    return True


def check_correct_status_code(code):
    return code in codes


def code_and_class_can_exist(code, clas):
    if (code != admin_cod and clas == no_class) \
            or (code == admin_cod and clas != no_class):
        return False
    return True


def sort_days(arr):
    arr = [i[0] for i in arr]
    res_arr = []
    for date in arr:
        date = [int(j) for j in date.split()][::-1]
        res_arr.append(date)
    res_arr.sort()
    result = []
    for year, month, day in res_arr:
        year, month, day = str(year), str(month), str(day)
        if len(month) == 1:
            month = '0' + month
        if len(day) == 1:
            day = '0' + day
        result.append(f'{day} {month} {year}')
    return result


def get_near_day_of_duty(arr):
    arr = sort_days(arr)
    return arr[0]


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


def sort_studends_by_dutys(arr):
    served_inx = 2
    return sorted(arr, key=lambda x: x[served_inx])
