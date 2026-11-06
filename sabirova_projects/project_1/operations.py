'''расчеты: количество теплоты Q и класс нагрева'''
from typing import Annotated
from connstans import t_small_limit, t_normal_limit

def calc_heat(
        m: Annotated[float, 'масса, кг'],
        c: Annotated[float, 'удельная теплоемкость, Дж(кг*C)'],
        t1: Annotated[float, 'начальная температура, C'],
        t2: Annotated[float, 'конечная температура, C'],
) -> float:
    '''рассчитать количество теплоты Q = m * c * (t2 - t1), Дж'''
    return m * c * (t2 - t1)

def heat_class(
        t: Annotated[float, 'разность температур t = t2 - t1']
) -> str:
    '''классифицировать нагрев через if-elif-else'''
    if t < t_small_limit:
        return 'малый нагрев'
    elif t <= t_normal_limit:
        return 'нормальный нагрев'
    else:
        return 'интенсивный нагрев'