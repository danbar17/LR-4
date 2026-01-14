class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = []

    def add_edge(self, from_node, to_node):
        if from_node in self.nodes and to_node in self.nodes:
            self.nodes[from_node].append(to_node)


def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph.nodes[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


def bfs(graph, start_node):
    visited = set()
    queue = [start_node]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph.nodes[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


# Создание графа
graph_test = Graph()

for i in range(1, 16):
    graph_test.add_node(i)

edges = [
    (1, 2), (1, 3), (1, 4), (1, 5),
    (2, 6), (6, 7), (7, 2),
    (3, 8), (8, 9), (9, 10), (10, 8),
    (4, 11), (11, 12), (12, 11),
    (5, 13), (13, 14), (14, 15), (15, 13),
    (7, 9), (10, 12), (12, 14)
]

for from_node, to_node in edges:
    graph_test.add_edge(from_node, to_node)

# Вывод графа
for node in graph_test.nodes:
    print(f"{node} -> {graph_test.nodes[node]}")

print("Обход в глубину:")
dfs(graph_test, 1)
print()

print("Обход в ширину:")
bfs(graph_test, 1)