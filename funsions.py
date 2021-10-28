def check_pass(password):
    count = 0
    repetition = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']
    if len(password) < 9:
        return 'длина пароля меньше 9 символов'
    if password.islower() or password.isupper():
        return 'в пароле все символы одного регистра'
    if password.isalpha():
        return 'в пароле нет ни одной цифры'
    if password.isdigit():
        return 'в пароле все символы одного регистра'
    for i in '1234567890':
        if i in password:
            count += 1
    if count == 0:
        return 'в пароле нет ни одной цифры'

    for i in repetition:
        for j in range(len(i) - 2):
            if i[j: j + 3] in password.lower():
                return 'в пароле есть комбинация симоволов, стоящих рядом в строке клавиатуры'
    return password


def check_login(login):
    if len(login) < 5:
        return 'длина логина меньше 5 символов'
    if ' ' in login:
        return 'в логине есть символ пробела'
    return login


def check_code(code):
    if code not in ['0', '1', '2']:
        return 'такого кода не существует'
    return code


def check_surname(surname):
    if len(surname) < 2:
        return 'слишком короткая фамилия'
    if not surname.isalpha():
        return 'в фамилии могут присутствовать только буквы'
    return surname


def check_name(name):
    if len(name) < 2:
        return 'слишком короткое имя'
    if not name.isalpha():
        return 'в имени могут присутствовать только буквы'
    return name


def check_fathername(fathername):
    if len(fathername) < 2:
        return 'слишком короткое отчество'
    if not fathername.isalpha():
        return 'в отчестве могут присутствовать только буквы'
    return fathername
