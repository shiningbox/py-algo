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

def dfs_stack(visited):
    # Start with node1
    stack = [1]
    while stack:
        top = stack.pop()
        visited[top] = True
        # Push top's children into a stack
        # If top has adjacent neighbors
        if top in graph:
            for neighbor in graph[top]:
                # If neighbor is not visited
                if neighbor not in visited:
                    stack.append(neighbor)

def dfs_recursion(node, visited):
    if not node:
        return None

    # Visit this node
    visited[node] = True

    # If the node has outgoing adjacent neighbors
    if node in graph:
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_recursion(neighbor, visited)


print(graph)
visited = {}
dfs_stack(visited)
print(visited.keys())

visited = {}
dfs_recursion(1, visited)
print(visited.keys())
