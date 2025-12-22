# Oriented graphs - имеют направление

import networkx as nx

DG = nx.DiGraph()
 
DG.add_edge("A", "B")  # по направлению - от А до В

DG.add_edge("B", "A")


# CONVERT not oriented graph into oriented
# G = nx.Graph()
# G.add_edges_from([("A", "B"), ("B", "C")])
# DG = nx.DiGraph(G)


# CONVERT oriented graph into not oriented
# DG = nx.DiGraph()
# DG.add_edges_from([("A", "B"), ("B", "C")])
# G = nx.Graph(DG)

# Ребра являють собою пари вузлів. Вони можуть мати додаткові атрибути, такі як вага, етикетка тощо:
G.add_edge(1, "A", weight=2.5, label="connection")

# Ви можете додавати атрибути до вузлів і ребер під час їх створення або після:
G.nodes[1]["color"] = "red"
G.edges[1, "A"]["label"] = "bridge"


# Щоб дізнатися, які вузли з'єднані з конкретним вузлом, використовуйте індексацію графа за допомогою імені вузла:
neighbors_of_A = G["A"] # {'B': {}, 'C': {}}

# Щоб отримати інформацію про ребро між двома вузлами, використовуйте подвійну індексацію:
edge_info = G["A"]["B"]  # {}

# Якщо в ребра є атрибути, ви можете отримати доступ до них через третій рівень індексації:
edge_weight = G["A"]["B"]["weight"]

# Ви можете додавати атрибути до графа через його атрибут graph:
G.graph["name"] = "My Graph"

# Щоб додати атрибут до конкретного вузла, використовуйте атрибут nodes графа:
G.nodes["A"]["color"] = "blue"

# Щоб додати атрибут до ребра, використовуйте індексацію графа за допомогою імен вузлів, які формують це ребро:
G["A"]["B"]["weight"] = 5

# Також можна додавати атрибути під час створення вузлів і ребер:
G.add_node("A", color="red")
G.add_edge("A", "B", weight=4)











