from typing import List, Sequence

def _check_window(window: int, n: int) -> None:
    if not isinstance(window, int) or window < 1:
        raise ValueError('window должно быть целым числом больше 0')
    if window > n:
        raise ValueError('window не может быть больше длины ряда')

def simple_moving_average(data: Sequence[float], window: int) -> List[float]:
    '''SMA через бегущую сумму'''
    if not data:
        raise ValueError('ряд пуст, расчет SMA невозможен')
    _check_window(window, len(data))

    running = sum(data[:window])
    result = [running / window]
    for i in range(window, len(data)):
        running += data[i] - data[i - window]
        result.append(running / window)
    return result

def centered_moving_average(data: Sequence[float], window: int) -> List[float]:
    '''центрированное MA (окно нечетное)'''
    if window % 2 == 0:
        raise ValueError('centered_moving_average требует нечетное окно')
    return simple_moving_average(data, window)

def exponential_moving_average(data: Sequence[float], alpha: float) -> List[float]:
    '''EMA'''
    if not (0 < alpha <= 1):
        raise ValueError('alpha должен лежать в промежутке(0;1])')
    if not data:
        raise ValueError('пустой ряд, расчет невозможен')

    result = [float(data[0])]
    for i in range(1, len(data)):
        result.append(alpha * data[i] + (1 - alpha) * result[-1])
        return result