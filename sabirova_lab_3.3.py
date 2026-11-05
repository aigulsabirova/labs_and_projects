g = True
while g:
    try:
        n = int(input('введите количество элементов: '))
        if n > 0:
            g = False
        else:
            print('ошибка')
    except ValueError:
        print('неверный ввод')
D = []
for i in range(n):
    x1 = False
    while not x1:
        try:
            x = int(input(f'введите элемент {i}: '))
            x1 = True
        except ValueError:
            print('неверный ввод')
    D.append(x)
s = 0
for i in range(n):
    if i % 2 != 0:
        s += D[i]
print('массив D: ', D)
print('сумма элементов с нечетными индексами: ', s)