import heapq
import networkx as nx
import matplotlib.pyplot as plt


# 1. Build a weighted graph + visualize it
G = nx.Graph()

# Add edges in format: node1, node2, weight
G.add_edge('A', 'B', weight=5)
G.add_edge('A', 'C', weight=10)
G.add_edge('B', 'D', weight=3)
G.add_edge('C', 'D', weight=2)
G.add_edge('D', 'E', weight=4)

# Create positions for nodes (layout) with fixed seed for reproducibility
pos = nx.spring_layout(G, seed=42)

# Draw nodes and edges
nx.draw(
    G, pos,
    with_labels=True,
    node_size=700,
    node_color="skyblue",
    font_size=15,
    width=2
)

# Draw edge weights as labels
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()


# 2. Print a table of distances and visited status
def print_table(distances, visited):
    print("{:<10} {:<10} {:<10}".format("Vertex", "Distance", "Visited"))
    print("-" * 30)

    for vertex in distances:
        d = distances[vertex]
        distance_str = "∞" if d == float("inf") else str(d)
        status = "Yes" if vertex in visited else "No"
        print("{:<10} {:<10} {:<10}".format(vertex, distance_str, status))

    print()


# 3. Dijkstra using a binary heap
def dijkstra(graph, start):
    # shortest_paths[v] = best known distance from start to v
    shortest_paths = {vertex: float("inf") for vertex in graph}
    shortest_paths[start] = 0

    # created a heap - priority_queue stores pairs (distance, vertex)
    priority_queue = [(0, start)]

    # visited = vertices already finalized
    visited = set()

    while priority_queue:
        # Pop the vertex with the smallest distance from the heap
        cur_dist, u = heapq.heappop(priority_queue)

        # Skip outdated heap entries
        if cur_dist > shortest_paths[u]:
            continue

        # Skip if this vertex was already finalized
        if u in visited:
            continue
        visited.add(u)

        # Print progress after each step
        print_table(shortest_paths, visited)

        # Try to improve distances to all neighbors of u
        for neighbor, weight in graph[u].items():
            # If neighbor is already finalized, we don't need to update it
            if neighbor in visited:
                continue
            
            # New candidate distance to neighbor via u:
            new_dist = cur_dist + weight
            # Update if this path is shorter than the best known
            if new_dist < shortest_paths[neighbor]:
                shortest_paths[neighbor] = new_dist
                heapq.heappush(priority_queue, (new_dist, neighbor))

    return shortest_paths


# 4. Convert networkx graph to a simple format
graph = {node: {} for node in G.nodes()}

for u, v, data in G.edges(data=True):
    w = data["weight"]
    graph[u][v] = w
    graph[v][u] = w


# Dijkstra
shortest_paths = dijkstra(graph, "A")
print("Result:", shortest_paths)

# Expected:
# {'A': 0, 'B': 5, 'C': 10, 'D': 8, 'E': 12}
