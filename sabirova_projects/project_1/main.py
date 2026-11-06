from validation import input_mass, input_t1, input_t2
from menu import show_menu, select_medium
from operations import calc_heat, heat_class

def main() -> None:
    '''главный сценарий'''
    print('=== расчет теплоты на нагрев среды ===')

    while True:
        show_menu()
        medium_data = select_medium()

        if medium_data is None:
            print('работа завершена')
            break

        c, medium_name = medium_data

        m = input_mass()
        t1 = input_t1()
        t2 = input_t2(t1)

        q = calc_heat(m, c, t1, t2)
        t = t2 - t1
        heat_class_name = heat_class(t)

        print('\n результаты')
        print(f'среда: {medium_name}')
        print(f'масса: {m} кг')
        print(f'температуры: t1 = {t1} C, t2 = {t2} C')
        print(f'разность температур: {t} C')
        print(f'теплота: Q = {q:.2f} Дж')
        print(f'класс нагрева: {heat_class_name}')
        print('\n')

if __name__ == '__main__':
    main()