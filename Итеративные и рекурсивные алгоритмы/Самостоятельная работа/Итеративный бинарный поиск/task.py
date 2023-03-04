from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """

    left_border = 0
    right_border = len(seq) - 1

    while left_border <= right_border:
        mid_ind = right_border - left_border // 2
        mid_border = seq[mid_ind]

        if mid_border == value:
            while True:
                if not 0 < mid_ind < len(seq) or seq[mid_ind - 1] != value:
                    break
                mid_ind -= 1
            return mid_ind

        elif mid_border < value:
            left_border = mid_ind + 1

        elif mid_border > value:
            right_border = mid_ind - 1

    raise ValueError()
