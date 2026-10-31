n = int(input('введите количество элементов: '))
D = []
for i in range(n):
    x = int(input(f'введите элемент {i}: '))
    D.append(x)
s = 0
for i in range(n):
    if i % 2 != 0:
        s += D[i]
print('массив D: ', D)
print('сумма элементов с нечетными индексами: ', s)