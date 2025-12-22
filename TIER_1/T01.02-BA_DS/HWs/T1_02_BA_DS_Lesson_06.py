from collections import deque
import matplotlib.pyplot as plt
import networkx as nx


# TASK 1
# Build a graph: Black Sea ports connections
# Nodes: ports
# Edges: possible direct sea legs between ports
# Weight: "distance" (in nm)

weighted_edges = [
    ("Odesa", "Chornomorsk", 10),
    ("Chornomorsk", "Constanta", 230),
    ("Odesa", "Constanta", 240),
    ("Constanta", "Varna", 110),
    ("Varna", "Burgas", 60),
    ("Burgas", "Istanbul", 160),
    ("Constanta", "Istanbul", 420),
    ("Istanbul", "Samsun", 360),
    ("Samsun", "Trabzon", 180),
    ("Trabzon", "Batumi", 120),
    ("Batumi", "Poti", 40),
    ("Odesa", "Istanbul", 800),
    ("Istanbul", "Trabzon", 520),
    ("Samsun", "Batumi", 420),
]

G = nx.Graph()
G.add_weighted_edges_from(weighted_edges)             # stores "weight" on edges


print("=== TASK 1: BASIC GRAPH STATS ===")
print("Number of nodes (V):", G.number_of_nodes())
print("Number of edges (E):", G.number_of_edges())

degrees = dict(G.degree())                           # degree = number of edges connected to the node
print("\nDegrees (node -> degree):")

for node, deg in degrees.items():
    # Loop through each (node, degree) pair
    # node: the port name (string)
    # deg: how many direct connections this port has in the graph
    print(f"  {node:12s} -> {deg}")


# Visualization (with distances on edges)
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G, pos,
    with_labels=True,
    node_size=900,
    width=2,
    font_size=9
)

edge_labels = {(u, v): f"{data['weight']}" for u, v, data in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

plt.title("Black Sea Ports Network (edge labels = distances)")
# Baplt.gcf().set_constrained_layout(True)
plt.show()



# TASK 2
# DFS and BFS (iterative) to find paths in the same graph

def build_adj_list(edge_list):
    """
    Build an adjacency list from a weighted edge list

    Input format:
      edge_list = [(u, v, w), (u2, v2, w2), ...]
      where:
        u, v = node names (ports)
        w    = edge weight (distance) - ignored here
    """
    # Create an empty dictionary:
    # keys   -> nodes
    # values -> lists of neighbors
    graph = {}

    # Iterate through edges
    for u, v, _w in edge_list:
        # Ensure u exists in graph; if not, create empty list, then add v
        graph.setdefault(u, []).append(v)

        # For an UNDIRECTED graph, we also add the reverse connection v -> u
        graph.setdefault(v, []).append(u)

    # Sort neighbor lists to make traversal deterministic (same order every run)
    for node in graph:
        graph[node] = sorted(graph[node])

    return graph


# Build an unweighted adjacency list from the weighted edges.
# We keep weights for Dijkstra, but BFS/DFS will use this adjacency list.
graph_unweighted = build_adj_list(weighted_edges)


def dfs_iterative_path(graph, start_vertex, goal_vertex):    # DFS stack (list): LIFO
    visited = set()
    stack = [start_vertex]
    parent = {start_vertex: None}

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)

            if vertex == goal_vertex:
                break

            for neigh in reversed(graph[vertex]):
                if neigh not in visited and neigh not in parent:
                    parent[neigh] = vertex      # memorises parent nodes
                    stack.append(neigh)         # stacks neighbours

    if goal_vertex not in parent:
        return []

    path = []              # Create an empty list to store the path
    cur = goal_vertex      # Start backtracking from the goal vertex (starting point)
    while cur is not None: # parent[start] is None, so the loop stops at start
        path.append(cur)   # Add current vertex to path (goes backwards)
        cur = parent[cur]  # Move to the parent (previous vertex on the known route)
    path.reverse()  
    return path


def bfs_iterative_path(graph, start, goal):             # BFS queue (deque): FIFO
    visited = set()
    queue = deque([start])
    parent = {start: None}

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.add(vertex)

            if vertex == goal:
                break

            for neigh in graph[vertex]:
                if neigh not in visited and neigh not in parent:
                    parent[neigh] = vertex
                    queue.append(neigh)

    if goal not in parent:
        return []

    # restore path
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path


print("\n=== TASK 2: DFS vs BFS PATHS ===")
start_fixed, goal_fixed = "Odesa", "Trabzon"

path_dfs = dfs_iterative_path(graph_unweighted, start_fixed, goal_fixed)
path_bfs = bfs_iterative_path(graph_unweighted, start_fixed, goal_fixed)

print("DFS path:", path_dfs, "| edges:", max(len(path_dfs) - 1, 0))
print("BFS path:", path_bfs, "| edges:", max(len(path_bfs) - 1, 0))

# BFS: returns a path with the minimum number of edges (hops) in an unweighted graph.
# DFS: returns a path depending on neighbor order; it goes deep along one branch first.



# TASK 3
# Implement Dijkstra: shortest paths by total distance (weights)
# Find shortest paths between all vertices of the graph

def build_weighted_dict(edge_list):
    """
    Convert (u, v, w) -> dict-of-dict:
      g[u][v] = w
    """
    g = {}
    for u, v, w in edge_list:
        g.setdefault(u, {})[v] = w
        g.setdefault(v, {})[u] = w
    return g


def dijkstra(graph, start):
    """
    Dijkstra:
    - distances dict
    - unvisited list
    - choose min-distance unvisited vertex each step
    Returns:
      distances: shortest distance from start to every vertex
      parent: to restore the shortest path start -> goal
    """
    distances = {vertex: float("infinity") for vertex in graph}
    parent = {vertex: None for vertex in graph}
    distances[start] = 0

    unvisited = list(graph.keys())

    while unvisited:
        current = min(unvisited, key=lambda v: distances[v])

        if distances[current] == float("infinity"):
            break

        for neighbor, weight in graph[current].items():   # Check distance through nodes
            cand = distances[current] + weight
            if cand < distances[neighbor]:
                distances[neighbor] = cand
                parent[neighbor] = current

        unvisited.remove(current)

    return distances, parent


def restore_path(parent, start, goal):
    """
    Restore path start - goal using parent pointers from Dijkstra
    If goal is unreachable, returns []
    """
    if start == goal:
        return [start]
    if parent[goal] is None:
        return []

    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        if cur == start:
            break
        cur = parent[cur]
    path.reverse()

    if not path or path[0] != start:
        return []

    return path


weighted_dict = build_weighted_dict(weighted_edges)


print("\n=== TASK 3: ALL-PAIRS SHORTEST PATHS (DIJKSTRA) ===")

# Run Dijkstra from every node (all-pairs shortest distances)
all_pairs = {}
for s in weighted_dict:
    dist, parent = dijkstra(weighted_dict, s)
    all_pairs[s] = {"dist": dist, "parent": parent}

# Print distances from each start node
for s in weighted_dict:
    print(f"\nFrom {s}:")
    for t, d in all_pairs[s]["dist"].items():
        d_str = "∞" if d == float("infinity") else str(d)
        print(f"  to {t:12s} = {d_str}")


# Optional interactive part: lecturer can input two ports and get BFS/DFS/Dijkstra paths
def choose_port(prompt, allowed):
    """
    Ask user for a port name
    allowed: set of valid node names
    """
    while True:
        s = input(prompt).strip()
        if s in allowed:
            return s
        print(f"Unknown port. Available: {', '.join(sorted(allowed))}")


print("\n=== EXTRA: INTERACTIVE PATHS FOR TWO PORTS ===")
nodes = set(G.nodes())

start = choose_port("Enter START port: ", nodes)
goal = choose_port("Enter GOAL port: ", nodes)

# BFS/DFS paths (ignore weights)
bfs_path = bfs_iterative_path(graph_unweighted, start, goal)
dfs_path = dfs_iterative_path(graph_unweighted, start, goal)

print("\nBFS path (min hops):", bfs_path, "| hops:", max(len(bfs_path) - 1, 0))
print("DFS path (depends on order):", dfs_path, "| hops:", max(len(dfs_path) - 1, 0))

# Dijkstra shortest path by weights
dist_start, parent_start = dijkstra(weighted_dict, start)
dij_path = restore_path(parent_start, start, goal)
dij_dist = dist_start[goal]

print("\nDijkstra path (min total distance):", dij_path)
print("Dijkstra total distance:", dij_dist)