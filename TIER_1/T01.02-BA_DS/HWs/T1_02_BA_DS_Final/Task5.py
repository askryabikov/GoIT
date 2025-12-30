import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None              # посилання на лівого нащадка
        self.right = None             # посилання на правого нащадка
        self.val = key                # значення вузла
        self.color = color            # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())   # Унікальний ідентифікатор для кожного вузла


def add_edges_iterative(graph, root, pos):
    """
    Додає вузли та ребра у граф NetworkX БЕЗ рекурсії.
    Одночасно рахує позиції pos для малювання дерева.

    Оскільки стек працює за принципом LIFO, то щоб лівий вузол обробився першим,
    у стек спочатку додаємо правого нащадка, а потім лівого.
    """
    stack = [(root, 0, 0, 1)]  # (node, x, y, layer)

    while stack:
        node, x, y, layer = stack.pop()
        if node is None:
            continue

        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)

        # 1. якщо є лівий нащадок — додаємо ребро і позицію ліворуч
        if node.left:
            graph.add_edge(node.id, node.left.id)
            lx = x - 1 / (2 ** layer)        # зсув ліворуч залежно від рівня
            pos[node.left.id] = (lx, y - 1)  # на 1 нижче по y

        # .) якщо є правий нащадок — додаємо ребро і позицію праворуч
        if node.right:
            graph.add_edge(node.id, node.right.id)
            rx = x + 1 / (2 ** layer)         # зсув праворуч залежно від рівня
            pos[node.right.id] = (rx, y - 1)  # на 1 нижче по y

        # Кладемо дітей у стек так, щоб у результаті обробка була left-first:
        # - right кладемо першим
        # - left кладемо другим
        if node.right:
            rx = pos[node.right.id][0]        # беремо вже порахований x
            stack.append((node.right, rx, y - 1, layer + 1))

        if node.left:
            lx = pos[node.left.id][0]
            stack.append((node.left, lx, y - 1, layer + 1))

    return graph


def draw_tree(tree_root, title="", pause=0.6):
    """
    Малює дерево з поточними кольорами вузлів.
    Використовується для покрокової візуалізації обходу.
    """
    tree = nx.DiGraph()                          # орієнтований граф
    pos = {tree_root.id: (0, 0)}                 # позиція кореня
    add_edges_iterative(tree, tree_root, pos)    # заповнюємо граф вузлами/ребрами

    colors = [data["color"] for _, data in tree.nodes(data=True)]
    # Використовуємо значення вузла для міток
    labels = {node_id: data["label"] for node_id, data in tree.nodes(data=True)}

    plt.clf()
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    if title:
        plt.title(title)
    plt.axis("off")
    plt.pause(pause)


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



def reset_colors(root, color="skyblue"):
    """Скидає всі кольори вузлів у базовий колір"""
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        node.color = color
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def dfs_stack(root):
    """
    DFS-обхід без рекурсії
    Використовує стек. 
    Порядок: root -> left -> right (preorder)
    """
    order = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node is None:
            continue

        order.append(node)

        # спочатку додаємо right, потім left, щоб left обробився раніше
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return order


def bfs_queue(root):
    """
    BFS-обхід без рекурсії.
    Використовує чергу.
    """
    order = []
    q = deque([root])

    while q:
        node = q.popleft()
        if node is None:
            continue

        order.append(node)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return order


def hex_to_rgb(h):
    """Перетворює '#RRGGBB' -> (R, G, B)."""
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def rgb_to_hex(r, g, b):
    """Перетворює (R, G, B) -> '#RRGGBB'."""
    return "#{:02X}{:02X}{:02X}".format(r, g, b)


def gradient_colors(n, start_hex="#0B2A4A", end_hex="#BFE8FF"):
    """
    Генерує n кольорів від темного до світлого (HEX #RRGGBB).
    """
    if n <= 1:
        return [start_hex]

    r1, g1, b1 = hex_to_rgb(start_hex)
    r2, g2, b2 = hex_to_rgb(end_hex)

    colors = []
    for i in range(n):
        t = i / (n - 1)  # 0..1
        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)
        colors.append(rgb_to_hex(r, g, b))

    return colors


def visualize_traversal(root, order, title_prefix, pause=0.6):
    """
    Покроково фарбує вузли у порядку обходу та перемальовує дерево.
    """
    reset_colors(root, color="skyblue")

    colors = gradient_colors(len(order))  # з темного на світлий
    for i, node in enumerate(order):
        node.color = colors[i]            # кожен вузол отримує унікальний HEX-колір
        draw_tree(root, title=f"{title_prefix}: step {i+1}/{len(order)} (visit {node.val})", pause=pause)


if __name__ == "__main__":
    heap_values = [0, 4, 1, 5, 10, 3]
    root = heap_to_tree(heap_values)

    # Вибір у терміналі
    choice = input("Choose traversal: 1-DFS, 2-BFS, 3-Both: ").strip()

    plt.ion()
    plt.figure(figsize=(9, 6))

    if choice in ("1", "3"):
        order_dfs = dfs_stack(root)
        visualize_traversal(root, order_dfs, "DFS (stack)", pause=0.7)

    if choice in ("2", "3"):
        order_bfs = bfs_queue(root)
        visualize_traversal(root, order_bfs, "BFS (queue)", pause=0.7)

    plt.ioff()
    plt.show()