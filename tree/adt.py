from abc import ABC, abstractmethod
from list.adt import PositionalContainer, Node


class TreeException(Exception):
    """Base class for other exceptions"""
    pass


class LinkTreeNode(Node):

    def __init__(self, element: object, parent: Node, children: list, container: PositionalContainer):
        super(LinkTreeNode, self).__init__(element, container)
        self.parent = parent
        self.children = children


class ArrayTreeNode:

    def __init__(self, element, rank, container):
        # Element can be a primitive element such as int, str
        # Or composite element such as an item (Key, Element)
        self.element = element
        self.container = container
        self.rank = rank
        self.height = 0
        self.depth = 0
        self.is_balanced = False

class Tree(PositionalContainer):

    @abstractmethod
    def root(self) -> LinkTreeNode:
        pass

    @abstractmethod
    def is_root(self, node: LinkTreeNode) -> bool:
        pass

    @abstractmethod
    def is_internal(self, node: LinkTreeNode) -> bool:
        pass

    @abstractmethod
    def is_external(self, node: LinkTreeNode) -> bool:
        pass

    @abstractmethod
    def parent(self, node: LinkTreeNode) -> LinkTreeNode:
        pass

    # Ordered list if it is for an ordered tree
    @abstractmethod
    def children(self, node: LinkTreeNode) -> list:
        pass

    @abstractmethod
    def set_children(self, node: LinkTreeNode, children: list):
        pass

    @abstractmethod
    def print_subtree(self, node: LinkTreeNode):
        pass
