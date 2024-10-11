# Выполнил: Мальцев Георгий Павлович


def dekart():
    try:
        x = int(input('Введите координату x: '))
        y = int(input('Введите координату y: '))
    except ValueError:
        print('Используйте числа!')
    else:
        if (x >= 0) & (y >=0):
            print('Четверть 1')
        if (x <= 0) & (y >= 0) :
            print('Четверть 2')
        if (x <= 0) & (y <= 0) :
            print('Четверть 3')
        if (x >= 0) & (y <= 0) :
            print('Четверть 4')
dekart()