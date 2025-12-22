import networkx as nx
import matplotlib.pyplot as plt

G = nx.complete_graph(8)
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True)
plt.title("Circular Layout")
plt.show()
