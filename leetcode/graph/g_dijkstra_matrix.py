from collections import deque
edge_list = [(0, 1, 1), (1, 2, 2), (2, 5, 10), (1, 3, 3), (3, 4, 3), (1, 6, 7), (4, 6, 3), (4, 5, 3), (5, 7, 1)]

def convert_list_to_matrix(g_list):
    nodes = set()
    for edge in g_list:
        nodes.add(edge[0])
        nodes.add(edge[1])
    graph_2d = [[0 for _ in range(len(nodes))] for _ in range(len(nodes))]
    for edge in g_list:
        s = edge[0]
        d = edge[1]
        w = edge[2]
        graph_2d[s][d] = w
    return graph_2d

# Gradually building a min distance cloud
# - Starting with the start node s, update the size of the cloud to the distance of its nearest neighbor
# - Move to its nearest neighbor i, continue expanding the cloud with its nearest neighbor j
# - Continue the process
def dijkstra(start, graph: list) -> list:
    node_size = len(graph)
    # Initial an array to save the min distance
    min_ds = [10000] * node_size
    # Set d[start] to be zero, as it is same node
    min_ds[start] = 0
    visited = [False] * node_size
    # Use a queue for BFS
    queue = deque()
    queue.append(start)
    # Current distance from source now
    while queue:
        # Try to expand the cloud of current level
        # For all nodes in the current level
        # min expanding distance
        level_size = len(queue)
        for _ in range(level_size):
            # Visit the node
            head = queue.popleft()
            visited[head] = True
            # For all its neighbors
            for neighbor in range(node_size):
                # If the neighbor
                neighbor_dist = graph[head][neighbor]
                if neighbor_dist > 0 and not visited[neighbor]:
                    # Update the min distance from source
                    min_ds[neighbor] = min(min_ds[neighbor], min_ds[head] + neighbor_dist)
                    queue.append(neighbor)
    return min_ds


graph = convert_list_to_matrix(edge_list)
graph2 = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7],
          [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

print(graph)
d = dijkstra(0, graph)
d = dijkstra(0, graph2)