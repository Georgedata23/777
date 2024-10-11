# Выполнил: Мальцев Георгий Павлович

import logging

logging.basicConfig(level=logging.INFO, filename="py_log_2.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')


def srav():
    try:
        a = int(input('Введите число a: '))
        b = int(input('Введите число b: '))
    except ValueError:
        print('Используйте числа!')
        logging.info("Вели неверное значение")
    except Exception:
        print('Что-то пошло не так')
        logging.error("Что-то не так?")
    else:
        if a <= b:
            print(b)
        else:
            print(a)
        logging.info("Success!")
srav()