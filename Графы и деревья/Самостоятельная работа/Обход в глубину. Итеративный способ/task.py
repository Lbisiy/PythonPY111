from typing import Hashable, List
from collections import deque

import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в глубину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """

    visited = {node: False for node in g.nodes}
    queue = deque()
    path = []

    queue.append(start_node)
    visited[start_node] = True

    while queue:
        node = queue.pop()
        path.append(node)
        for nod in g.neighbors(node):
            if visited[nod] is False:
                visited[nod] = True
                queue.append(nod)

    return path


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ACBFEDG")
    graph.add_edges_from([
        ("A", "C"),
        ("A", "B"),
        ("C", "F"),
        ("B", "E"),
        ("B", "D"),
        ("E", "G"),
    ])
    print(dfs(graph, "A"))
