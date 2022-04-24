from heapq import *


class Node:

    def __init__(self, key):
        self.key = key
        self.cluster = set()

class Edge:

    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def __lt__(self, other):
        self.weight < other.weight


# A minimum spanning tree (MST) or minimum weight spanning tree is a subset of the edges of a connected,
# edge-weighted undirected graph that connects all the vertices together,
# without any cycles and with the minimum possible total edge weight
edge_list = [(0, 1, 1), (1, 2, 2), (2, 5, 10), (1, 3, 3), (3, 4, 3), (1, 6, 7), (4, 6, 3), (4, 5, 3), (5, 7, 1)]

edges = []
g = {}
for edge in edge_list:
    node1 = Node(edge[0])
    node1.cluster.add(node1.key)
    node2 = Node(edge[1])
    node2.cluster.add(node2.key)
    weight = edge[2]
    edges.append(Edge(node1.key, node2.key, weight))
    g[node1.key] = node1
    g[node2.key] = node2

def print_edges(edges):
    for edge in edges:
        print(f"{edge.node1} -> {edge.node2}", end=", ")

def mst(edges):
    min_heap = []
    # Results are the edges
    res = []
    # Add all edges to a priority queue
    for edge in edges:
        heappush(min_heap, (edge.weight, edge))

    # First, each node was assigned with its own all-connected cluster
    # Then for each edge with min weight:
    # - Check if their nodes are already in a connected cluster or not, if yes, continue
    # - If not, merge the clusters of the two nodes
    # Continue till all edges are visited

    while min_heap:
        _, edge = heappop(min_heap)
        src_node = g[edge.node1]
        dest_node = g[edge.node2]
        # if two nodes are in different connected cluster
        # connect the two cluster with the min edge
        if src_node.cluster != dest_node.cluster:
            res.append(edge)
            # Merge the two clusters
            new_set = src_node.cluster.union(dest_node.cluster)
            # Update the nodes' cluster
            for idx in new_set:
                node = g[idx]
                node.cluster = new_set
        else:
            continue
    return res

res = mst(edges)
print_edges(res)
