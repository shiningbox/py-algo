# Python3 program to print DFS traversal
# from a given given graph

# This class represents a directed graph using
# adjacency list representation

class Graph:

    # Constructor
    def __init__(self, vertices):

        # No. of vertices
        self.vertices = vertices

        # default dictionary to store graph
        self.graph = {}
        for v in self.vertices:
            self.graph[v] = []

        self.paths = []

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_visit(self, v, visited):
        visited.add(v)
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_visit(neighbor, visited)

    # The function to do DFS traversal. It uses
    def dfs(self, v):
        visited = set()
        self.dfs_visit(v, visited)
        return visited

    def dfs_path(self, u, v, visited, path):

        # Mark the current node as visited
        visited[u] = True
        path.append(u)
        if u == v:
            self.paths.append(list(path))
        else:
            # Recur for all the vertices
            # adjacent to this vertex
            for n in self.graph[u]:
                if not visited[n]:
                    self.dfs_path(n, v, visited, path)

        # Now vertex u has all been visited
        # mark it as unvisited
        path.pop()
        visited[u] = False

    def dfs_paths(self, u, v):
        visited = [False] * len(self.vertices)
        self.dfs_path(u, v, visited, [])

# Create a graph given
# in the above diagram
g = Graph([0, 1, 2, 3, 4, 5, 6, 7])
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(1, 4)
g.add_edge(4, 7)
g.add_edge(1, 5)
g.add_edge(5, 7)
g.add_edge(5, 6)
g.add_edge(6, 7)

#visited = g.dfs(0)
#print(visited)
print(g.graph)
g.dfs_paths(0, 7)
print(g.paths)

# This code is contributed by Neelam Yadav