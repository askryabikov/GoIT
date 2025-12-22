# Not oriented graphs

import networkx as nx

G =nx. Graph ()

G.add_node("A")

G.add_nodes_from(["B", "C", "D"])

G.add_edge("A", "B")

G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])

print(G.nodes())  # ['A', 'B', 'C', 'D']

print(G.edges())  # [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D')]

print(list(G.neighbors("A")))  # ['B', 'C']

G.remove_node("A")

G.remove_nodes_from(["B", "C"])

G.remove_edge("A", "B")

G.remove_edges_from([("A", "C"), ("B", "D")])

