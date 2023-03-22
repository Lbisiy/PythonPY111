from typing import Tuple
from functools import lru_cache


def calculate_paths(shape: Tuple[int, int]) -> int:
    """
    Дано поле с размером rows*cols посчитать количество ходов коня из верхнего левого угла в нижний правый

    :param shape: размер доски в виде кортежа
    :return: количество путей согласно заданным условиям
    """

    m, n = shape

    @lru_cache
    def recursion(x, y):
        if x == 0 and y == 0:
            return 1

        if not 0 <= x < n or not 0 <= y < m:
            return 0

        return recursion(x - 2, y - 1) + recursion(x - 2, y + 1) + recursion(x - 1, y - 2) + recursion(x + 1, y - 2)

    return recursion(n - 1, m - 1)


if __name__ == '__main__':
    print(calculate_paths((4, 4)))  # 2
    print(calculate_paths((7, 15)))  # 13309
