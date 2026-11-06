'''валидация пользовательского ввода'''
from __future__ import annotations
from connstans import m_min, m_max, t1_min, t1_max, t2_min, t2_max
from logger import log_error

def validate_range(value: float, low: float, high: float) -> tuple[bool, str]:
    '''проверка попадания value в [low, high] через if-elif-else'''
    if value < low:
        return False, f'ошибка: значение меньше нижней границы ({low}).'
    elif value > high:
        return False, f'ошибка: значение больше верхней границы({high}).'
    else:
        return True, ''

def input_number(prompt: str, low: float, high: float) -> float:
    '''запрос числа, пока не будет корректного.'''
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError as e:
            msg = str(e.args[0]) if e.args else str(e)
            msg = f"ошибка: введено не число ('{raw}'). {msg}"
            log_error(msg)
            continue

        ok, msg = validate_range(value, low, high)
        if ok:
            return value

        print(msg + 'повторите ввод.')
        log_error(msg)

def input_mass() -> float:
    '''циклический ввод массы m(кг), допустимо 0.1...1000.'''
    return input_number('введите массу m, кг (0.1...1000): ', m_min, m_max)

def input_t1() -> float:
    '''циклический ввод начальной температуры t1 (C), допустимо -50...100.'''
    return input_number('введите начальную температуру t1, C (-50...100): ', t1_min, t1_max)

def input_t2(t1: float) -> float:
    '''циклический ввод конечной температуры t2 (C), с проверкой t2 > t1.'''
    print('внимание: конечная температура должна быть больше начальной')
    while True:
        t2 = input_number('введите конечную температуру t2, C (0...1000): ', t2_min, t2_max)
        if t2 > t1:
            return t2
        else:
            msg = 'ошибка: конечная температура t2 должна быть больше t1.'
            print(msg)
            log_error(msg)