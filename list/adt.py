from abc import ABC, abstractmethod


class QueueFullException(Exception):
    """Base class for other exceptions"""
    pass


class StackException(Exception):
    """Base class for other exceptions"""
    pass


class DequeException(Exception):
    """Base class for other exceptions"""
    pass


class SequenceException(Exception):
    """Base class for other exceptions"""
    pass


class Queue(ABC):

    @abstractmethod
    def enqueue(self, obj: object):
        pass

    @abstractmethod
    def dequeue(self) -> object:
        pass

    @abstractmethod
    def size(self) -> int:
        raise QueueFullException()

    @abstractmethod
    def front(self) -> object:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def print(self):
        raise QueueFullException()


class Stack(ABC):

    @abstractmethod
    def push(self, obj: object):
        pass

    @abstractmethod
    def pop(self) -> object:
        raise StackException()

    @abstractmethod
    def size(self) -> int:
        raise StackException()

    @abstractmethod
    def is_empty(self) -> bool:
        raise StackException()

    @abstractmethod
    def top(self) -> object:
        raise StackException()

    @abstractmethod
    def print(self):
        raise StackException()


# Node for linked linkedlist
class Node:

    def __init__(self):
        self.element = None
        self.next = None

    def print(self):
        print(str(self.element))


class DLNode:

    def __init__(self, element, prev_element, next_element):
        self.element = element
        self.prev = prev_element
        self.next = next_element


class Node:

    def __init__(self, element, container):
        self.element = element
        self.container = container
        self.rank = 0


class Position(DLNode):

    def __init__(self, element, prev_element, next_element, container):
        super(Position, self).__init__(element, prev_element, next_element)
        self.container = container


# header -> starting_node -> starting_node -> trailer
# Header and trailer are convenient for insert/remove from first and last elements
# Suppose insert/delete at the both end of the queue with O(1) time
class Deque(ABC):

    @abstractmethod
    def insert_first(self, obj: object):
        raise DequeException()

    @abstractmethod
    def first(self) -> object:
        raise DequeException()

    @abstractmethod
    def remove_first(self) -> object:
        raise DequeException()

    @abstractmethod
    def remove_last(self) -> object:
        raise DequeException()

    @abstractmethod
    def insert_last(self, obj: object):
        raise DequeException()

    @abstractmethod
    def last(self) -> object:
        raise DequeException()

    @abstractmethod
    def size(self) -> int:
        raise DequeException()

    @abstractmethod
    def is_empty(self) -> bool:
        raise DequeException()


class Sequence(ABC):

    @abstractmethod
    def elem_at_rank(self, rank: int) -> object:
        # If rank < 0 and rank > N-1, raise exception
        raise SequenceException

    @abstractmethod
    def position_at_rank(self, rank: int) -> Position:
        raise SequenceException

    @abstractmethod
    def rank_of_position(self, pos: Position) -> int:
        raise SequenceException

    # Return the element formly at rank
    @abstractmethod
    def replace_elem_rank(self, rank: int, element: object) -> object:
        # If rank < 0 and rank > N-1, raise exception
        raise SequenceException

    # Return the element formly at position p
    @abstractmethod
    def replace_elem_rank(self, position: Position, element: object) -> object:
        # If rank < 0 and rank > N-1, raise exception
        raise SequenceException

    # O(1), swap elements
    @abstractmethod
    def swap(self, p: Position, q: Position):
        raise SequenceException

    @abstractmethod
    def insert_elem_rank(self, rank: int, element: object):
        # If rank < 0 and rank > N-1, raise exception
        raise SequenceException

    @abstractmethod
    def insert_first(self, element: object) -> object:
        raise SequenceException

    @abstractmethod
    def insert_before(self, pos: Position, element: object) -> object:
        raise SequenceException

    @abstractmethod
    def before(self, pos: Position) -> object:
        raise SequenceException

    @abstractmethod
    def after(self, pos: Position) -> object:
        raise SequenceException

    @abstractmethod
    def insert_after(self, pos: Position, element: object) -> object:
        raise SequenceException

    @abstractmethod
    def insert_last(self, element: object) -> object:
        raise SequenceException

    @abstractmethod
    def remove_elem_rank(self, rank: int) -> object:
        # If rank < 0 and rank > N-1, raise exception
        raise SequenceException

    @abstractmethod
    def first(self) -> object:
        raise SequenceException

    @abstractmethod
    def is_first(self, pos: Position) -> bool:
        raise SequenceException

    @abstractmethod
    def last(self) -> object:
        raise SequenceException

    @abstractmethod
    def is_last(self, pos: Position) -> bool:
        raise SequenceException

    @abstractmethod
    def remove(self, pos: Position) -> object:
        raise SequenceException

    @abstractmethod
    def size(self) -> int:
        raise SequenceException

    @abstractmethod
    def is_empty(self) -> bool:
        raise SequenceException


class PositionalContainer(ABC):

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