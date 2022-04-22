# Quick way is use a dict as a graph
# Or a Graph class
# key is the original node, values is the destiny nodes
graph = {}

# Suppose it is uni-direction from edges[0] to edges[1]
def convert_edges_graph(self, edges):
    for edge in edges:
        if edge[0] in self.graph:
            graph[edge[0]] = []
        graph[edge[0]].append(edge[1])


def bfs_deque():
    pass