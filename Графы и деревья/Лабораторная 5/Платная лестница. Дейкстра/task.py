from typing import Union
import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """

    path = nx.dijkstra_path_length(graph, 0, len(graph) - 1)
    return path


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)

    def stairway_graph(stairway: tuple) -> nx.DiGraph:
        graph_list = []

        for i in range(len(stairway) - 1):
            graph_list.append((i, i + 1, stairway[i]))
            graph_list.append((i, i + 2, stairway[i + 1]))
        graph_list.append((i + 1, i + 2, stairway[-1]))

        graph_ = nx.DiGraph()
        graph_.add_weighted_edges_from(graph_list)
        return graph_

    graph = stairway_graph(stairway)
    print(stairway_path(graph))  # 72

    # graph_list = [
    #     (0, 1, 5),
    #     (0, 2, 11),
    #     (1, 2, 11),
    #     (1, 3, 43),
    #     (2, 3, 43),
    #     (2, 4, 2),
    #     (3, 4, 2),
    #     (3, 5, 23),
    #     (4, 5, 23),
    #     (4, 6, 43),
    #     (5, 6, 43),
    #     (5, 7, 22),
    #     (6, 7, 22),
    #     (6, 8, 12),
    #     (7, 8, 12),
    #     (7, 9, 6),
    #     (8, 9, 6),
    #     (8, 10, 8),
    #     (9, 10, 8),
    # ]
    # graph = nx.DiGraph()
    # graph.add_weighted_edges_from(graph_list)
