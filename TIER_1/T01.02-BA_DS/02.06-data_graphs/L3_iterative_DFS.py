def dfs_iterative(graph, start_vertex):
    visited = set()
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]  
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()  
        if vertex not in visited:
            print(vertex, end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(graph[vertex]))  

# Представлення графа за допомогою списку суміжності
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Виклик функції DFS
dfs_iterative(graph, 'A')

# В этом коде мы определяем функцию dfs_iterative, использующую стек для хранения вершин, которые нужно посетить. 
# Мы извлекаем вершину из стека, посещаем ее, а затем добавляем все ее посещенные соседние вершины к стеку. 
# Этот процесс повторяется, пока стек не станет пустым.