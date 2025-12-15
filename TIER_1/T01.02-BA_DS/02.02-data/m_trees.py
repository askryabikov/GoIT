import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def build_tree():
    # Створюємо дерево: [8, 3, 10, 1, 6, 14, 4, 7]
    root = None
    for key in [8, 3, 10, 1, 6, 14, 4, 7]:
        root = insert(root, key)
    return root

def visualize_tree(root):
    G = nx.DiGraph()
    
    def add_edges(node, parent=None):
        if node:
            G.add_node(node.val)
            if parent:
                G.add_edge(parent.val, node.val)
            add_edges(node.left, node)
            add_edges(node.right, node)
    
    add_edges(root)
    pos = graphviz_layout(G, prog='dot')
    nx.draw(G, pos, with_labels=True, arrows=False, node_size=1000, node_color='skyblue')
    plt.show()

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

# Виконання
if __name__ == "__main__":
    # Створюємо дерево та візуалізуємо його
    tree_root = build_tree()
    # visualize_tree(tree_root)
    # tree_root = insert(tree_root, 5)
    
    # Пошук числа 6
    found = search(tree_root, 6)
    print(f"Знайдено: {found.val}" if found else "Не знайдено")
    print(f"Left: {found.left.val}" if found.left else "Left: None")
    print(f"Right: {found.right.val}" if found.right else "Right: None")
    
    visualize_tree(tree_root)
