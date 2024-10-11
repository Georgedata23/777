# Выполнил: Мальцев Георгий Павлович

import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')


def srav_min():
    try:
        a = int(input('Введите число a: '))
        b = int(input('Введите число b: '))
        c = int(input('Введите число c: '))
    except ValueError:
        print('Используйте числа!')
        logging.info("Вели неверное значение")
    else:
        if a<=b<=c:
            print(a)
        elif a<=c<=b:
            print(a)
        elif c<=b:
            print(c)
        else:
            print(b)
srav_min()