# генератор пароля вида aaaXXXaa
# где а-строчная буква, x-цифра
import random
import string


def passgen():
    digit = 0
    pass_list = []
    while digit <= 7:
        if (digit < 3):
            pass_list.append(random.choice(string.ascii_lowercase))
            digit += 1
        elif (digit >= 3 and digit < 6):
            pass_list.append(str(random.randrange(0, 10, 1))) # str - приведение числа в строку
            digit += 1
        else:
            pass_list.append(random.choice(string.ascii_lowercase))
            digit += 1
    pass_string = ''.join(pass_list)
    return pass_string