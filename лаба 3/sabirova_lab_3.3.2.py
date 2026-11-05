s = []
for i in range(8):
    x1 = False
    while not x1:
        try:
            x = int(input(f'введите элемент {i + 1}: '))
            x1 = True
        except ValueError:
            print('ошибка')
    s.append(x)
for i in range(8):
    if s[i] < 15:
        s[i] = s[i] * 2
print('готовый массив: ', s)
