g = True
while g:
    try:
        A = int(input('введите число: '))
        g = False
    except ValueError:
        print('неверный ввод')
f = True
while f:
    try:
        B = int(input('введите число: '))
        if A < B:
            f = False
        else:
            print('неверно введено число')
    except ValueError:
        print('неверный ввод')

s = 0
for i in range(A, B + 1):
    s += i * i

print('сумма квадратов: ', s)
