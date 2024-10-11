# Выполнил: Мальцев Георгий Павлович


import logging

logging.basicConfig(level=logging.INFO, filename="py_log_6.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')


def calendar():
    try:
        k = int(input('Введите номер месяца: '))
    except ValueError:
        print('Ошибка, вводите числа')
        logging.info('Ввели не число')
    else:
        match k:
            case 1|3|5|7|8|10|12: print(31)
            case 2: print(28)
            case 4|6|9|11: print(30)
            case _:print('Ошибка')
        logging.info('Успех!')
calendar()