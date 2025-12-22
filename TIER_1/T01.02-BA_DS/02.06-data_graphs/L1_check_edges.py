from typing import List, Union

Number = Union[int, float]

def edge_exists(adj_matrix: List[List[Number]], u: int, v: int) -> int:
    """
    Returns 1 if there is an edge from u to v, otherwise -1.
    Works for:
      - unweighted adjacency matrices (0/1)
      - weighted adjacency matrices (0 = no edge, non-zero = edge)
    """
    n = len(adj_matrix)

    # Basic validation (helps catch mistakes early)
    if n == 0:
        raise ValueError("Adjacency matrix is empty.")
    if any(len(row) != n for row in adj_matrix):
        raise ValueError("Adjacency matrix must be square (n x n).")
    if not (0 <= u < n and 0 <= v < n):
        raise ValueError("Vertex indices are out of range.")

    return 1 if adj_matrix[u][v] != 0 else -1


adj_matrix = [
    [0, 1, 0, 1],  # A (0)
    [1, 0, 1, 0],  # B (1)
    [0, 1, 0, 1],  # C (2)
    [1, 0, 1, 0],  # D (3)
]

print(edge_exists(adj_matrix, 0, 1))  # A -> B  => 1
print(edge_exists(adj_matrix, 0, 2))  # A -> C  => -1
print(edge_exists(adj_matrix, 2, 3))  # C -> D  => 1


# Матрица смежности обеспечивает быстрый доступ к наличию ребер, но требует больше памяти. 
# Список смежности более эффективен с точки зрения использования памяти, особенно для разреженных графов, 
# но он может быть более медленным для некоторых операций, таких как проверка наличия ребер.