from collections import deque


class WeightedGraph:
    """Класс для представления взвешенного направленного графа."""

    def __init__(self):
        """Инициализация пустого взвешенного графа."""
        self.nodes = {}

    def add_node(self, value):
        """Добавляет узел в граф, если его еще нет."""
        if value not in self.nodes:
            self.nodes[value] = []  # Каждый элемент списка - кортеж (сосед, вес)

    def add_edge(self, from_node, to_node, weight):
        """Добавляет направленное взвешенное ребро от from_node к to_node."""
        if from_node in self.nodes and to_node in self.nodes:
            self.nodes[from_node].append((to_node, weight))


def dfs(graph, start_node, visited=None):
    """
    Рекурсивный обход графа в глубину (DFS).

    Args:
        graph: объект взвешенного графа
        start_node: начальный узел
        visited: множество посещенных узлов (опционально)

    Note:
        Веса рёбер игнорируются при обходе, используются только связи между узлами.
    """
    if visited is None:
        visited = set()

    visited.add(start_node)
    print(start_node, end=" ")

    for neighbor, weight in graph.nodes[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def bfs(graph, start_node):
    """
    Обход графа в ширину (BFS) с использованием deque.

    Args:
        graph: объект взвешенного графа
        start_node: начальный узел

    Note:
        Веса рёбер игнорируются при обходе, используются только связи между узлами.
    """
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor, weight in graph.nodes[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


def create_weighted_graph():
    """Создает и возвращает тестовый взвешенный граф."""
    graph = WeightedGraph()

    # Добавляем узлы 1-10
    for i in range(1, 11):
        graph.add_node(i)

    # Определяем взвешенные рёбра
    weighted_edges = [
        (1, 2, 5), (1, 3, 3), (1, 4, 7),
        (2, 5, 4), (2, 6, 6),
        (3, 5, 2), (3, 7, 8),
        (4, 8, 5), (4, 9, 4),
        (5, 10, 3), (6, 10, 7),
        (7, 10, 4), (8, 10, 6),
        (9, 10, 5),
        (5, 2, 4), (10, 5, 3)  # Обратные рёбра
    ]

    # Добавляем все рёбра
    for from_node, to_node, weight in weighted_edges:
        graph.add_edge(from_node, to_node, weight)

    return graph


def print_graph_info(graph):
    """Выводит информацию о графе в удобочитаемом формате."""
    print("Структура взвешенного графа:")
    print("-" * 30)

    for node in sorted(graph.nodes.keys()):
        connections = graph.nodes[node]
        if connections:
            connections_str = ", ".join([f"{neighbor}(вес={weight})"
                                         for neighbor, weight in connections])
            print(f"Узел {node:2} -> {connections_str}")
        else:
            print(f"Узел {node:2} -> нет исходящих рёбер")

    print("-" * 30)


def main():
    """Основная функция для демонстрации работы с графом."""
    # Создаем граф
    graph = create_weighted_graph()

    # Выводим информацию о графе
    print_graph_info(graph)
    print()

    # Выполняем обход в глубину
    print("Обход в глубину (DFS), начиная с узла 1:")
    dfs(graph, 1)
    print("\n")

    # Выполняем обход в ширину
    print("Обход в ширину (BFS), начиная с узла 1:")
    bfs(graph, 1)
    print()


if __name__ == "__main__":
    main()