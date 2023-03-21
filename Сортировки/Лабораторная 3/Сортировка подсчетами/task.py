from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """

    if len(container) == 0:
        return container

    count_list = [0] * (max(container) + 1)
    new_list = []

    for i in container:
        count_list[i] += 1

    for i, val in enumerate(count_list):
        if val > 0:
            new_list.extend([i] * val)

    return new_list


if __name__ == "__main__":
    list_ = [9, 5, 7, 2, 5, 4, 3, 1]
    print(sort(list_))
