s = ''
while not s:
    s = input('введите строку: ')
    if not s:
        print('неверно')
c = s.count('.')
r = s.replace('.', '')
print(f'строка без точек: {r}')
print(f'удалено точек: {c}')
