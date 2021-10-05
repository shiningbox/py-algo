from abc import ABC, abstractmethod
from list.linked_sequence import LinkedSequence

class DictionaryException(Exception):
    """Base class for other exceptions"""
    pass

class Node(ABC):
    @abstractmethod
    def element(self) -> object:
        pass

    @abstractmethod
    def container(self) -> object:
        pass

class Graph(ABC):
    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def elements(self) -> enumerate:
        pass

    @abstractmethod
    def nodes(self) -> enumerate:
        pass

    @abstractmethod
    def swap(self, node1: Node, node2: Node):
        pass

    @abstractmethod
    def replace(self, node1: Node, element: object):
        pass

    # Graph related nodes
    @abstractmethod
    def num_vertices(self) -> int:
        pass

    @abstractmethod
    def num_edges(self) -> int:
        pass

    @abstractmethod
    def vertices(self) -> list:
        pass

    @abstractmethod
    def edges(self) -> list:
        pass

    # vertex and edge related methods
    @abstractmethod
    def degree(self, v: Node) -> int:
        pass

    @abstractmethod
    def adjacent_vertices(self, v: Node) -> list:
        pass

    @abstractmethod
    def incident_edges(self, v: Node) -> list:
        pass

    @abstractmethod
    def end_vertices(self, edge: Node) -> list:
        pass

    @abstractmethod
    def opposite(self, edge: Node) -> Node:
        pass

    @abstractmethod
    def are_adjacent(self, v: Node, w: Node) -> bool:
        pass

    # Directed edge related methods
    @abstractmethod
    def directed_edges(self) -> list:
        pass

    @abstractmethod
    def undirected_edges(self) -> list:
        pass

    @abstractmethod
    def in_degree(self, v: Node) -> int:
        pass

    @abstractmethod
    def out_degree(self, v: Node) -> int:
        pass

    @abstractmethod
    def in_incident_edges(self, v: Node) -> list:
        pass

    @abstractmethod
    def out_incident_edges(self, v: Node) -> list:
        pass

    @abstractmethod
    def in_adjacent_vertices(self, v: Node) -> list:
        pass

    @abstractmethod
    def out_adjacent_vertices(self, v: Node) -> list:
        pass

    @abstractmethod
    def destination(self, e: Node) -> Node:
        pass

    @abstractmethod
    def origin(self, e: Node) -> Node:
        pass

    @abstractmethod
    def is_directed(self, e: Node) -> bool:
        pass

    #Updating graphs
    @abstractmethod
    def insert_edge(self, v: Node, w: Node, o: object) -> Node:
        pass

    @abstractmethod
    def insert_directed_edge(self, v: Node, w: Node, o: object) -> Node:
        pass

    @abstractmethod
    def insert_vertex(self, o: object) -> Node:
        pass

    @abstractmethod
    def remove_vertex(self, e: Node) -> Node:
        pass

    @abstractmethod
    def make_undirected(self, e: Node):
        pass

    @abstractmethod
    def reverse_direction(self, e: Node):
        pass

    @abstractmethod
    def set_direction_from(self, e: Node, v: Node):
        pass

    @abstractmethod
    def set_direction_to(self, e: Node, v: Node):
        pass

