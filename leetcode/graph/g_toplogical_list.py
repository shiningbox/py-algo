from collections import deque


def convert_list_to_matrix(g_list):
    nodes = set()
    for edge in g_list:
        nodes.add(edge[0])
        nodes.add(edge[1])
    graph_2d = [[0 for _ in range(len(nodes))] for _ in range(len(nodes))]
    for edge in g_list:
        s = edge[0]
        d = edge[1]
        graph_2d[s][d] = 1
    return graph_2d


# Toplogical sort a graph
# Use
def toplogical_sorting(graph) -> list:
    # Use an incoming array to track the incomings for each node
    node_size = len(graph)
    ins = [0] * node_size
    res = []

    # Use a stack to store the node with incoming == 0, as the starting point
    queue = deque()
    for i in range(node_size):
        col = [row[i] for row in graph]
        ins[i] = sum(col)
        # This node has no incoming
        if ins[i] == 0:
            queue.append(i)

    # For each node whose
    while queue:
        # Pop the early inserted node with incoming == 0
        top = queue.popleft()
        res.append(top)
        # Disconnect it from all its neighbors
        for c in range(node_size):
            if graph[top][c] == 1:
                graph[top][c] = 0
                ins[c] -= 1
                if ins[c] == 0:
                    queue.append(c)

    return res


edge_list = [(0, 1), (1, 2), (2, 5), (1, 3), (3, 4), (1, 6), (4, 6), (4, 5), (5, 7)]
graph = convert_list_to_matrix(edge_list)
print(toplogical_sorting(graph))
