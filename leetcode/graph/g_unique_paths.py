# Quick way is use a dict as a graph
# Or a Graph class
# key is the original node, values is the destiny nodes
# Suppose it is uni-direction from edges[0] to edges[1]
edges = [(1, 2), (2, 3), (2, 4), (3, 6), (4, 5), (5, 7), (5, 6), (6, 8)]
def convert_edges_graph():
    for edge in edges:
        visited[edge[0]] = False
        visited[edge[1]] = False
        if edge[0] not in graph:
            graph[edge[0]] = []
        graph[edge[0]].append(edge[1])


graph = {}
visited = {}
convert_edges_graph()
paths = []

def dfs_recursion(node, end, path):
    if not node:
        return None

    # Visit this node
    visited[node] = True
    path.append(node)
    # If found the end
    if node == end:
        paths.append(list(path))
    else:
        # If the node has outgoing adjacent neighbors
        # Visit its neighbors (and recursively visit neighbors of neighbors)
        # Add any valid paths from start to end
        if node in graph:
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs_recursion(neighbor, end, path)

    # Now the node and all its neighbors have been visited
    # and all paths starting with this
    # mark it as unvisited
    path.pop()
    visited[node] = False


def dfs_stack(start, end):
    stack = [(start, [])]
    while stack:
        # Visit node
        node, path = stack.pop()
        visited[node] = True
        new_path = path + [node]
        del path
        # Create a new path based on the node
        # Delete the previous node
        if node == end:
            visited[end] = False
            paths.append(new_path)
        else:
            # If node has neighbors
            if node in graph:
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        # Continue explore neighbor
                        stack.append((neighbor, new_path))

def get_paths(start, end):
    dfs_recursion(start, end, [])


print(graph)
dfs_stack(1, 6)
print(paths)

