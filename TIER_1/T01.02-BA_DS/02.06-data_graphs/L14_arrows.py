import networkx as nx
import matplotlib.pyplot as plt

# Створення орієнтованого графа
G = nx.DiGraph()

# Додавання ребер
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 3), (4, 1)])

# Малювання графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True)

plt.show()
