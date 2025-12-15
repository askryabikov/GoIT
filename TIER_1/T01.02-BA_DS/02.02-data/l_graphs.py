import networkx as nx
import matplotlib.pyplot as plt
# 1. Створюємо граф
G = nx.Graph()

# 2. Додаємо вершини (станції)
stations = ["Центральна", "Студентська", "Зелена", "Історична", "Наукова"]
G.add_nodes_from(stations)

# 3. Додаємо ребра (маршрути між станціями)
routes = [
    ("Центральна", "Студентська", {"time": 2}),
    ("Студентська", "Зелена", {"time": 3}),
    ("Зелена", "Історична", {"time": 4}),
    ("Історична", "Наукова", {"time": 2}),
    ("Центральна", "Наукова", {"time": 20}),
]
G.add_edges_from(routes)

# 4. Візуалізуємо граф
def visualize_graph(G):
    
    pos = nx.spring_layout(G)  # Розташування вершин
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=1500, font_size=10)
    edge_labels = nx.get_edge_attributes(G, "time")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Транспортна мережа міста")
    plt.show()

# 5. Пошук найкоротшого шляху (алгоритм Дейкстри)
def find_shortest_path(start, end):
    path = nx.shortest_path(G, source=start, target=end, weight="time")
    path_time = nx.shortest_path_length(G, source=start, target=end, weight="time")
    print(f"Найкоротший шлях між {start} та {end}: {' -> '.join(path)} (час: {path_time} хв)")
if __name__ == "__main__":
    # Приклад використання
    find_shortest_path("Центральна", "Наукова")
    find_shortest_path("Студентська", "Історична")
    visualize_graph(G)
