'''меню выбора среды через match-case'''
from __future__ import annotations
from  connstans import c_water, c_oil, c_steel

def show_menu() -> None:
    '''вывести меню сред'''
    print('\n выберите технологическую среду: ')
    print('  1 - вода (c = 4200 Дж/(кг*C))')
    print('  2 - масло (c = 2000 Дж/(кг*C))')
    print('  3 - сталь (c = 500 Дж/(кг*C))')
    print('  0 - выход')

def select_medium() -> tuple[float, str] | None:
    '''циклически запрашивать среду и возвращать кортеж (c, название)'''
    while True:
        choice = input('введите номер среды (от 0 до 3): ').strip()
        match choice:
            case '1':
                return c_water, 'вода'
            case '2':
                return c_oil, 'масло'
            case '3':
                return c_steel, 'сталь'
            case '0':
                return None
            case _:
                print("ошибка: неверный пункт меню. повторите ввод")