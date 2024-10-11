# Выполнил: Мальцев Георгий Павлович


def sravv():
    try:
        a = int(input('Введите число a: '))
        b = int(input('Введите число b: '))
    except ValueError:
        print('Используйте числа!')
    else:
        if a <= b:
            print(b)
            print(a)
        else:
            print(b)
            print(a)
sravv()
