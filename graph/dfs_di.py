from adjacency_list_graph import Node, AdjacencyListGraph
from adt import Graph
from graph_viz import create_flight_graph, visualize_digraph


class DiDFS:

    def __init__(self):
        self.graph = None
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
        edge.discovered = "back"

    def dfs_visit(self, origin_v: Node):
        origin_v_key = origin_v.element()
        self.mark_vertex(origin_v)
        self.spanning_tree.append(origin_v)
        self.start_visit(origin_v)
        out_edges = self.graph.out_incident_edges(origin_v_key)
        for next_edge in out_edges:
            edge_key = next_edge.element()
            if not self.is_marked(next_edge):
                # Visit the edge only once
                self.mark_edge(next_edge)
                destination_v = self.graph.destination(next_edge)
                if not self.is_done():
                    # If the edge's opposite vertex is not covered, mark the edge as discover
                    if not self.is_marked(destination_v):
                        next_edge.discovered = "tree"
                        self.dfs_visit(destination_v)
                    else:
                    # If the edge's opposite vertex is already covered, mark the edge as discover
                    # and traverse back
                        self.traverse_back(next_edge, origin_v)
        # All node v's edges have been explored
        self.end_visit(origin_v)
        return self.spanning_tree

    def print_spanning_tree(self):
        result = ""
        for vertex in self.spanning_tree:
            result += vertex.element() + ">"
        result = result[:-1]
        print(result)

    def print_edges(self):
        result = ""
        for edge in self.graph.edges():
            result += edge.element() + " : " + edge.discovered + " "
        print(result)

    def is_done(self):
        return False

def simple_test():
    flight_graph = create_flight_graph()
    starting_node = flight_graph.get_vertex("BOS")
    search = DiDFS()
    search.execute(flight_graph, starting_node, None)
    search.dfs_visit(starting_node)
    search.print_spanning_tree()
    search.print_edges()
    visualize_digraph(flight_graph)


#simple_test()

