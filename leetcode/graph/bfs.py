from adjacency_list_graph import Node, AdjacencyListGraph
from adt import Graph
from graph_viz import create_simple_graph, visualize_ungraph


class BFS:

    def __init__(self):
        self.graph = None
        self.levels = []
        self.marked_vertices = {}
        self.marked_edges = {}
        self.spanning_tree = []

    def mark_edge(self, edge: Node):
        edge_key = edge.element()
        self.marked_edges[edge_key] = edge

    def mark_vertex(self, vertex: Node):
        vertex_key = vertex.element()
        self.marked_vertices[vertex_key] = vertex

    def is_marked(self, n: Node):
        key = n.element()
        return key in self.marked_edges or key in self.marked_vertices

    def execute(self, graph: AdjacencyListGraph, start: Node, data: object):
        self.graph = graph
        return None

    def start_visit(self, node: Node):
        pass

    def end_visit(self, node: Node):
        pass

    def traverse_back(self, edge: Node, vertex: Node):
        edge.discovered = "cross"

    def bfs_visit(self, origin_v: Node):
        level = 0
        level_0 = []
        self.mark_vertex(origin_v)
        self.spanning_tree.append(origin_v)
        level_0.append(origin_v)
        self.levels.append(level_0)
        while len(self.levels[level]) > 0:
            next_level = []
            for vertex in self.levels[level]:
                edges = self.graph.incident_edges(vertex.element())
                for edge in edges:
                    if not self.is_marked(edge):
                        self.mark_edge(edge)
                        next_v = self.graph.opposite(vertex.element(), edge.element())
                        # If v is not marked, mark the edge and vertex as discovered
                        if not self.is_marked(next_v):
                            edge.discovered = "discovery"
                            next_level.append(next_v)
                            self.spanning_tree.append(next_v)
                            self.mark_vertex(next_v)
                        else:
                            self.traverse_back(edge, next_v)
            self.levels.append(next_level)
            level += 1
        return self.spanning_tree

    def print_spanning_tree(self):
        result = ""
        for vertex in self.spanning_tree:
            result += vertex.element() + ">"
        result = result[:-1]
        print(result)

    def is_done(self):
        return False

def simple_test():
    simple_graph = create_simple_graph()
    starting_node = simple_graph.get_vertex("A")
    search = BFS()
    search.execute(simple_graph, starting_node, None)
    search.bfs_visit(starting_node)
    search.print_spanning_tree()
    visualize_ungraph(simple_graph)

simple_test()