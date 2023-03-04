from typing import Union
from itertools import count
from math import factorial


DELTA = 0.000001


def sinx(x: Union[int, float]) -> float:
    """
    Вычисление sin(x) с помощью разложения в ряд Тейлора

    :param x: x значение в радианах
    :return: значение sin(x)
    """

    result = 0

    for n in count():
        val = pow(-1, n) * pow(x, 2 * n + 1) / factorial(2 * n + 1)
        result += val
        if abs(val) < DELTA:
            return result
