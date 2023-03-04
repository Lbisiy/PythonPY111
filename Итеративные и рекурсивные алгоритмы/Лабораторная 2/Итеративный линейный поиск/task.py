"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """

    if len(arr) == 0:
        raise ValueError("Последовательность пуста")

    elif len(arr) == 1:
        return arr[0]

    else:
        min_ = arr[0]
        index_ = 0
        for i, val in enumerate(arr):
            if val < min_:
                min_, index_ = val, i

    return index_
