import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None              # посилання на лівого нащадка
        self.right = None             # посилання на правого нащадка
        self.val = key                # значення вузла
        self.color = color            # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())   # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Додає вузли та ребра у граф NetworkX БЕЗ рекурсії
    Одночасно рахує позиції pos для малювання дерева
    """
    if node is None:
        return graph

    # Використання id та збереження значення вузла
    graph.add_node(node.id, color=node.color, label=node.val)

    # 1. якщо є лівий нащадок — додаємо ребро і позицію ліворуч
    if node.left:
        graph.add_edge(node.id, node.left.id)
        left_x = x - 1 / 2 ** layer           # зсув ліворуч залежно від рівня
        pos[node.left.id] = (left_x, y - 1)   # нижче на 1 по y
        add_edges(graph, node.left, pos, x=left_x, y=y - 1, layer=layer + 1)

    # 2. якщо є правий нащадок — додаємо ребро і позицію праворуч
    if node.right:
        graph.add_edge(node.id, node.right.id)
        right_x = x + 1 / 2 ** layer          # зсув праворуч залежно від рівня
        pos[node.right.id] = (right_x, y - 1) # на 1 нижче по y
        add_edges(graph, node.right, pos, x=right_x, y=y - 1, layer=layer + 1)

    return graph


def draw_tree(tree_root, title="Tree"):
    """
    Малює дерево, починаючи з кореня tree_root.
    """
    tree = nx.DiGraph()                     # орієнтований граф
    pos = {tree_root.id: (0, 0)}            # позиція кореня
    add_edges(tree, tree_root, pos)         # заповнюємо граф вузлами/ребрами

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    # Використовуємо значення вузла для міток
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def heap_to_tree(heap_values):
    """
    Будує бінарне дерево з масиву, який представляє бінарну купу
    Для індексу i:
    - лівий нащадок:  2*i + 1
    - правий нащадок: 2*i + 2
    """
    if not heap_values:
        return None

    # створюємо список Node для всіх значень
    nodes = [Node(v) for v in heap_values]

    # з'єднуємо вузли за правилами індексів купи
    for i in range(len(nodes)):
        left_i = 2 * i + 1
        right_i = 2 * i + 2

        if left_i < len(nodes):
            nodes[i].left = nodes[left_i]
        if right_i < len(nodes):
            nodes[i].right = nodes[right_i]

    return nodes[0]


if __name__ == "__main__":
    heap_values = [0, 4, 1, 5, 10, 3]  
    heap_root = heap_to_tree(heap_values)

    draw_tree(heap_root)
