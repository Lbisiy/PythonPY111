"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        Начало очереди слева, конец - справа
        """
        self.queue = []

    def enqueue(self, elem: Any) -> None:  # O(1)
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self.queue.append(elem)

    def dequeue(self) -> Any:  # O(1)
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if not self.queue:
            raise IndexError("Очередь пуста")

        return self.queue.pop(0)

    def peek(self, ind: int = 0) -> Any:  # O(1)
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("Указан неверный тип индекса")

        if not 0 <= ind <= len(self.queue):
            raise IndexError("Индекс вне границ очереди")

        return self.queue[ind]

    def clear(self) -> None:  # O(1)
        """ Очистка очереди. """
        self.queue.clear()

    def __len__(self):   # O(N)
        """ Количество элементов в очереди. """
        len_ = 0
        for _ in self.queue:
            len_ += 1

        return len_
