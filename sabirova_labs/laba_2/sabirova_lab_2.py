f = True
while f:
    try:
        m = float(input('введите массу: '))
        if (m > 0.1) and (m < 1000):
            f = False
    except ValueError:
        print('неверно введено число')

f1 = True
while f1:
    try:
        t1 = float(input('введите начальную температуру: '))
        if (t1 > -50) and (t1 < 100):
            f1 = False
    except ValueError:
        print('неверно введено число')

f2 = True
while f2:
    try:
        t2 = float(input('введите конечная температура: '))
        if (t2 > 0) and (t2 < 1000) and (t2 > t1):
            f2 = False
    except ValueError:
        print('неверно введено число')

print('1. вода, c = 4200 Дж/кг*C')
print('2. масло, c = 2000 Дж/кг*C')
print('3. сталь, c = 500 Дж/кг*C')

f3 = True
while f3:
    try:
        n = int(input('выберите среду: '))
        if (n == 1) or (n == 2) or (n == 3):
            f3 = False
    except ValueError:
        print('неверно введено число')

match n:
    case 1:
        c = 4200
        s = 'вода'
    case 2:
        c = 2000
        s = 'масло'
    case 3:
        c = 500
        s = 'сталь'

Q1 = m * c * (t2 - t1)
if (t2 - t1) < 10:
    print(s, ',', Q1, 'Дж', ',', 'малый нагрев')
elif ((t2 - t1) >= 10) and ((t2 - t1) <= 100):
    print(s, ',', Q1, 'Дж', ',', 'нормальный нагрев')
else:
    print(s, ',', Q1, 'Дж', ',', 'интенсивный нагрев')