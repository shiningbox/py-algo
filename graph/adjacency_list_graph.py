from graph.adt import Graph, Node

class Vertex(Node):

    def __init__(self, element, container):
        self.elem = element
        self.container = container
        self.incident_edges = {}
        self.num_incident_edges = 0
        self.incoming_edges = {}
        self.num_incoming_edges = 0
        self.outgoing_edges = {}
        self.num_outgoing_edges = 0
        self.toplogical_index = 0
        self.distance = 0

    def element(self) -> object:
        return self.elem

    def container(self) -> object:
        return self.container


class Edge(Node):

    def __init__(self, element, container, directed):
        self.elem = element
        self.weight = element
        self.container = container
        self.directed = directed
        self.vertices = []
        self.discovered = ""

    def element(self) -> object:
        return self.elem

    def container(self) -> object:
        return self.container


class AdjacencyListGraph(Graph):

    def __init__(self):
        self.vertices_dict = {}
        self.edges_dict = {}

    def size(self) -> int:
        return len(self.vertices_dict) + len(self.edges_dict)

    def is_empty(self) -> bool:
        return self.size() == 0

    def elements(self) -> enumerate:
        pass

    def nodes(self) -> enumerate:
        pass

    def swap(self, node1: Node, node2: Node):
        pass

    def replace(self, node1: Node, element: object):
        pass

    def num_vertices(self) -> int:
        return len(self.vertices_dict)

    def num_edges(self) -> int:
        return len(self.edges_dict)

    def vertices(self) -> set:
        return self.vertices_dict.values()

    def edges(self) -> set:
        return self.edges_dict.values()

    def degree(self, key: str) -> int:
        vertex = self.get_vertex(key)
        if vertex is not None:
            return vertex.num_incident_edges

    def adjacent_vertices(self, key: str) -> list:
        edge = self.get_edge(key)
        if edge is not None:
            return edge.vertices

    def incident_edges(self, key: str) -> list:
        vertex = self.get_vertex(key)
        if vertex is not None:
            return vertex.incident_edges.values()

    def end_vertices(self, key: str) -> list:
        pass

    def opposite(self, v_key: str, e_key: str) -> Node:
        edge = self.get_edge(e_key)
        if edge is not None:
            v_origin = edge.vertices[0]
            v_destiny = edge.vertices[1]
            if v_origin.element() == v_key:
                return v_destiny
            elif v_destiny.element() == v_key:
                return v_origin
            else:
                return None

    def are_adjacent(self, key1: str, key2: str) -> bool:
        node_u = self.get_vertex(key1)
        is_adjacent = False
        if node_u is not None:
            for edge in node_u.incident_edges.values():
                for vertex in edge.vertices:
                    if vertex.element() == key2:
                        is_adjacent = True
        return is_adjacent

    def directed_edges(self) -> list:
        pass

    def undirected_edges(self) -> list:
        pass

    def get_vertex(self, key: str) -> Node:
        if key is not None and key in self.vertices_dict:
            return self.vertices_dict[key]
        else:
            return None

    def get_edge(self, key: str) -> Node:
        if key is not None and key in self.edges_dict:
            return self.edges_dict[key]
        else:
            return None

    def in_degree(self, key: str) -> int:
        vertex = self.get_vertex(key)
        return vertex.num_incoming_edges

    def out_degree(self, key: str) -> int:
        vertex = self.get_vertex(key)
        return vertex.num_outgoing_edges

    def in_incident_edges(self, key: str) -> list:
        vertex = self.get_vertex(key)
        return vertex.incoming_edges.values()

    def out_incident_edges(self, key: str) -> list:
        vertex = self.get_vertex(key)
        return vertex.outgoing_edges.values()

    def adjacent_edges(self, key: str) -> list:
        vertex = self.get_vertex(key)
        return vertex.incident_edges.values()

    def in_adjacent_vertices(self, key: str) -> list:
        vertex = self.get_vertex(key)
        in_vertices = []
        if vertex is not None:
            for edge in vertex.incoming_edges.values():
                if len(edge.vertices) == 2:
                    in_vertices.append(edge.vertices[0])
        return in_vertices

    def out_adjacent_vertices(self, key: str) -> list:
        vertex = self.get_vertex(key)
        out_vertices = []
        if vertex is not None:
            for edge in vertex.outgoing_edges.values():
                if len(edge.vertices) == 2:
                    out_vertices.append(edge.vertices[1])
        return out_vertices

    def destination(self, e: Node) -> Node:
        if e is not None:
            return e.vertices[1]

    def origin(self, e: Node) -> Node:
        pass

    def is_directed(self, e: Node) -> bool:
        pass

    def insert_edge(self, key1: object, key2: object, data: object) -> Node:
        vertex_u = self.vertices_dict[key1]
        vertex_v = self.vertices_dict[key2]
        new_edge = Edge(data, self, directed=True)
        new_edge.weight = data
        new_edge.vertices.append(vertex_u)
        vertex_u.outgoing_edges[data] = new_edge
        vertex_u.incident_edges[data] = new_edge
        vertex_u.num_incident_edges += 1
        vertex_u.num_outgoing_edges += 1

        new_edge.vertices.append(vertex_v)
        vertex_v.incoming_edges[data] = new_edge
        vertex_v.incident_edges[data] = new_edge
        vertex_v.num_incident_edges += 1
        vertex_v.num_incoming_edges += 1

        self.edges_dict[data] = new_edge
        return new_edge

    def insert_directed_edge(self, v: Node, w: Node, data: object) -> Node:
        pass

    def insert_vertex(self, data: object) -> Node:
        new_vertex = Vertex(data, self.vertices_dict)
        self.vertices_dict[data] = new_vertex

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


