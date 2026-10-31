s = []
for i in range(8):
    x = int(input(f'введите элемент {i + 1}: '))
    s.append(x)
for i in range(8):
    if s[i] < 15:
        s[i] = s[i] * 2
print('готовый массив: ', s)