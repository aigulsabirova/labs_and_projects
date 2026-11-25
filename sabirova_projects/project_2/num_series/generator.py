import math
import random
from typing import List, Optional

def _validate_n(n: int) -> None:
    '''проверка, что n - положительное число'''
    try:
        is_positive_int = (n > 0) and (int(n) == n)
    except (TypeError, ValueError) as err:
        raise ValueError(
            f'n должно быть положительным целым числом '
            f'(получено: {n!r}; причина: {err.args[0]})'
       ) from err

    if not is_positive_int:
        raise ValueError(f'n должно быть целым положиельным числом (получено: {n!r})')

def random_series(n: int, low: float = -100.0, high: float = 100.0, seed: Optional[int] = None) -> List[float]:
    '''ряд из n равномерно распределенных чисел на [low, high]'''
    _validate_n(n)
    if low >= high:
        raise ValueError(f'low должно быть меньше high (получено: {low} >= {high})')
    rng = random.Random(seed)
    return [rng.uniform(low, high) for i in range(n)]

def sine_series(n: int, amplitude: float = 1.0, frequency: float = 1.0, noise: float = 0.0, seed: Optional[int] = None) -> List[float]:
    '''синусоидальный ряд с аддитивным шумом'''
    _validate_n(n)
    rng = random.Random(seed)
    return [
        amplitude * math.sin(2 * math.pi * frequency * i / n) + (rng.uniform(-noise, noise) if noise else 0.0)
        for i in range(n)
    ]

def trend_series(n: int, start: float = 0.0, step: float = 1.0, noise: float = 0.0, seed: Optional[int] = None) -> List[float]:
    '''линейный тренд'''
    _validate_n(n)
    rng = random.Random(seed)
    return [
        start + step * i + (rng.uniform(-noise, noise) if noise else 0.0)
        for i in range(n)
    ]

def v3_series(n: int = 1000, seed: Optional[int] = None) -> List[float]:
    """Аналитический ряд для Варианта 3: x[i] = sin(0.1*i) + uniform(-0.1, 0.1)."""
    _validate_n(n)
    rng = random.Random(seed)
    return [
        math.sin(0.1 * i) + rng.uniform(-0.1, 0.1)
        for i in range(n)
    ]