from graph.adt import Graph, Node

class Vertex(Node):

    def __init__(self, element, container):
        self.element = element
        self.container = container
        self.num_incident_edges = 0
        self.num_incoming_edges = 0
        self.num_outgoing_edges = 0

    def element(self) -> object:
        return self.element()

    def container(self) -> object:
        return self.container


class Edge(Node):

    def __init__(self, element, container):
        self.element = element
        self.container = container
        self.directed = False
        self.vertices = []

    def element(self) -> object:
        return self.element()

    def container(self) -> object:
        return self.container


class EdgeListGraph(Graph):

    def __init__(self):
        self.vertices = {}
        self.edges = {}
        self.v_key = 0
        self.e_key = 0

    def size(self) -> int:
        return len(self.vertices) + len(self.edges)

    def is_empty(self) -> bool:
        pass

    def elements(self) -> enumerate:
        pass

    def nodes(self) -> enumerate:
        pass

    def swap(self, node1: Node, node2: Node):
        pass

    def replace(self, node1: Node, element: object):
        pass

    def num_vertices(self) -> int:
        pass

    def num_edges(self) -> int:
        pass

    def vertices(self) -> set:
        pass

    def edges(self) -> set:
        pass

    def degree(self, v: Node) -> int:
        pass

    def adjacent_vertices(self, v: Node) -> list:
        pass

    def incident_edges(self, v: Node) -> list:
        pass

    def end_vertices(self, edge: Node) -> list:
        pass

    def opposite(self, edge: Node) -> Node:
        pass

    def are_adjacent(self, v: Node, w: Node) -> bool:
        pass

    def directed_edges(self) -> list:
        pass

    def undirected_edges(self) -> list:
        pass

    def in_degree(self, v: Node) -> int:
        pass

    def out_degree(self, v: Node) -> int:
        pass

    def in_incident_edges(self, v: Node) -> list:
        pass

    def out_incident_edges(self, v: Node) -> list:
        pass

    def in_adjacent_vertices(self, v: Node) -> list:
        pass

    def out_adjacent_vertices(self, v: Node) -> list:
        pass

    def destination(self, e: Node) -> Node:
        pass

    def origin(self, e: Node) -> Node:
        pass

    def is_directed(self, e: Node) -> bool:
        pass

    def insert_edge(self, v: Node, w: Node, o: object) -> Node:
        # Add e key by 1
        pass

    def insert_directed_edge(self, v: Node, w: Node, o: object) -> Node:
        pass

    def insert_vertex(self, o: object) -> Node:
        # Add origin_v key by 1
        pass

    def remove_vertex(self, e: Node) -> Node:
        pass

    def make_undirected(self, e: Node):
        pass

    def reverse_direction(self, e: Node):
        pass

    def set_direction_from(self, e: Node, v: Node):
        pass

    def set_direction_to(self, e: Node, v: Node):
        pass


graph = EdgeListGraph()
print(graph.size())
