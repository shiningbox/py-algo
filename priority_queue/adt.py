from abc import abstractmethod, ABC
from list.adt import Sequence, SequenceException


class PriorityQueueException(Exception):
    """Base class for other exceptions"""
    pass


class PriorityQueue(Sequence):

    @abstractmethod
    def insert_item(self, key: object, element: object) -> object:
        pass

    @abstractmethod
    def min_element(self) -> object:
        raise PriorityQueueException

    @abstractmethod
    def min_key(self) -> object:
        raise PriorityQueueException

    @abstractmethod
    def remove_min_element(self):
        raise PriorityQueueException


class Item:

    def __init__(self, key, element):
        self.key = key
        self.element = element
        self.rank = 0

class Comparator:

    # a < b
    @staticmethod
    def is_less_than(a: object, b: object) -> bool:
        return a < b

    # a <= b
    @staticmethod
    def is_less_than_equal_to(a: object, b: object) -> bool:
        return a <= b

    # a == b
    @staticmethod
    def is_equal_to(a: object, b: object) -> bool:
        return a == b

    # a > b
    @staticmethod
    def is_greater_than(a: object, b: object) -> bool:
        return a > b

    # a >=b
    @staticmethod
    def is_greater_than_equal_to(a: object, b: object) -> bool:
        return a >= b

    # Specific comparable classes only
    @staticmethod
    def is_comparable(self, a: object) -> bool:
        pass
