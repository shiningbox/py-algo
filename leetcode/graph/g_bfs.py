from collections import deque

# Quick way is use a dict as a graph
# Or a Graph class
# key is the original node, values is the destiny nodes
graph = {}
# Suppose it is uni-direction from edges[0] to edges[1]
edges = [(1, 2), (2, 3), (2, 4), (3, 6), (4, 5), (5, 7), (5, 6), (6, 8)]
def convert_edges_graph():
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = []
        graph[edge[0]].append(edge[1])

convert_edges_graph()


def bfs_deque(visited):
    # Start with 1
    queue = deque()
    queue.append(1)

    while queue:
        # current nodes
        size = len(queue)
        # pop all nodes at the same level
        for _ in range(size):
            top = queue.popleft()
            visited[top] = True
            # if top has adjacent neighbors
            if top in graph:
                for neighbor in graph[top]:
                    if neighbor not in visited:
                        queue.append(neighbor)


print(graph)
visited = {}
bfs_deque(visited)
print(visited.keys())
