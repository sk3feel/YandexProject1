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
