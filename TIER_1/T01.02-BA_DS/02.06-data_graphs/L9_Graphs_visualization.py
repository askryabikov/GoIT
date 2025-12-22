import matplotlib.pyplot as plt
import networkx as nx

G = nx.complete_graph(8)
nx.draw(G, with_labels=True)
plt.show()

# Функція nx.complete_graph в бібліотеці NetworkX використовується для створення повного графа. 
# Повний граф — це специфічний тип графа, в якому кожен вузол пов'язаний з кожним іншим вузлом. Іншими словами, між будь-якою парою вузлів існує ребро.