from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """

    if len(container) == 0:
        return container

    j = len(container) - 1
    while j != 0:
        i = 0
        while i != (len(container) - 1):
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = container[i + 1], container[i]
            i += 1
        j -= 1

    return container


if __name__ == "__main__":
    list_ = [9, 5, 7, 2, 5, 4, 3, 1]
    sort(list_)
