A = int(input('введите число: '))
f = True
while f:
    try:
        B = int(input('введите число: '))
        if A < B:
            f = False
    except ValueError:
        print('неверно введено число')

s = 0
for i in range(A, B + 1):
    s += i * i

print('сумма квадратов: ', s)