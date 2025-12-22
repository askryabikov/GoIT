import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання міст і доріг
G.add_edge('A', 'B', weight=5)
G.add_edge('A', 'C', weight=10)
G.add_edge('B', 'D', weight=3)
G.add_edge('C', 'D', weight=2)
G.add_edge('D', 'E', weight=4)

# Візуалізація графа
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()


def print_table(distances, visited):
    # Верхній рядок таблиці
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)
    
    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)
        
        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print("\\n")

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
        
        # Вивід таблиці після кожного кроку
        print_table(distances, visited)

    return distances

# Приклад графа у вигляді словника
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 10, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}

# Виклик функції для вершини A
dijkstra(graph, 'A')


# {'A': 0, 'B': 5, 'C': 10, 'D': 8, 'E': 12}



# Функция 1. single_source_dijkstra_path используется для нахождения кратчайших путей от одного выходного узла до всех других узлов в графе с помощью алгоритма Дейкстры.
# networkx.single_source_dijkstra_path(G, source, cutoff =None, weight = 'weight' )
# Где:
# G— обязательный параметр, это граф, для которого нужно найти кратчайшие пути.
# source– тоже обязательный параметр, это выходной узел, с которого начинаются поиски путей.
# cutoff– (необязательный), длина максимального пути. Если длина пути превышает это значение, то путь не рассматривается. По умолчанию отсутствует.
# weight– (необязательный), атрибут ребра (или функция), используемый для получения веса. По умолчанию используется weight.


# Функция 2. single_source_dijkstra_path_length используется для вычисления длин кратчайших путей 
# от указанного выходного узла до всех других узлов в графе, используя алгоритм Дейкстры.
# Синтаксис этой функции имеет те же параметры, что и предыдущая функция.
# networkx.single_source_dijkstra_path_length(G, source, cutoff =None, weight = 'weight' )
# Эта функция возвращает словарь, где ключи – это узлы графа, а значение – это длины кратчайших путей от исходного узла к каждому узлу.