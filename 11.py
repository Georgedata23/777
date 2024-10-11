# Выполнил: Мальцев Георгий Павлович

def robot():
    try:
        o = str(input('Введите оператор: '))
        a = int(input('Введите число a: '))
        b = int(input('Введите число b: '))
    except ValueError:
        print('Ошибка, вводите числа и строки где необходимо')
    else:
        match o:
            case '*': print(a*b)
            case '/': print(a/b)
            case '-': print(a-b)
            case '+': print(a+b)
            case _: print('Неизвестный оператор')
robot()