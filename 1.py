# Выполнил: Мальцев Георгий Павлович

import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')


def plus_num():
    try:
        t = 0
        a = int(input('Введите число a: '))
        b = int(input('Введите число b: '))
        c = int(input('Введите число c: '))
    except ValueError:
        print('Используйте числа!')
        logging.info("Вели неверное значение")
    else:
        if a > 0:
            t += 1
        if b > 0:
            t += 1
        if c > 0:
            t += 1
        print(f"Ответ: {t}")
        logging.info("Success!")
plus_num()
