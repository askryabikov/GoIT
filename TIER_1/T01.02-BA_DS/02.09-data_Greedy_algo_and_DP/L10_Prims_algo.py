from heapq import heappush, heappop
import networkx as nx


def prim_mst(graph):
    # Create an empty MST (Minimum Spanning Tree)
    mst = nx.Graph()

    # Start from an arbitrary node (first node in the graph)
    start_node = list(graph.nodes())[0]
    visited = {start_node}

    # Priority queue of candidate edges (weight, u, v)
    edges = []
    for u, v, weight in graph.edges(nbunch=visited, data="weight"):
        heappush(edges, (weight, u, v))

    # Keep adding edges until all nodes are in the MST
    while visited != set(graph.nodes()):
        # Take the smallest-weight edge that can expand the tree
        weight, u, v = heappop(edges)

        if v in visited:
            continue

        # Add the new node and edge to the MST
        visited.add(v)
        mst.add_edge(u, v, weight=weight)

        # Add all edges from the new node to the priority queue
        for new_u, new_v, new_weight in graph.edges(nbunch=[v], data="weight"):
            if new_v not in visited:
                heappush(edges, (new_weight, new_u, new_v))

    return mst


# Demo graph
G = nx.Graph()
G.add_edge("A", "B", weight=7)
G.add_edge("A", "D", weight=5)
G.add_edge("B", "C", weight=8)
G.add_edge("B", "D", weight=9)
G.add_edge("B", "E", weight=7)
G.add_edge("C", "E", weight=5)
G.add_edge("D", "E", weight=15)
G.add_edge("D", "F", weight=6)
G.add_edge("E", "F", weight=8)
G.add_edge("E", "G", weight=9)
G.add_edge("F", "G", weight=11)

# Run Prim's algorithm
mst = prim_mst(G)

# Print MST edges
print("Edges in the MST:")
for edge in mst.edges(data=True):
    print(edge)
