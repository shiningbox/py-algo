from abc import ABC, abstractmethod


class DictionaryException(Exception):
    """Base class for other exceptions"""
    pass

class Item:

    def __init__(self, key, element):
        self.key = key
        self.element = element


class Dictionary(ABC):

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    # Find element by key
    # If can not find element, return NO_SUCH_KEY
    @abstractmethod
    def find_element(self, key: object) -> object:
        pass

    @abstractmethod
    def find_all_elements(self, key: object) -> list:
        pass

    @abstractmethod
    def insert_item(self, key: object, element: object):
        pass

    @abstractmethod
    def remove(self, key: object) -> object:
        pass

    @abstractmethod
    def remove_all(self, key: object) -> list:
        pass


class OrderedDictionary(Dictionary):

    @abstractmethod
    def closest_key_before(self, key: object) -> object:
        pass

    @abstractmethod
    def closest_element_before(self, key: object) -> object:
        pass

    @abstractmethod
    def closest_key_after(self, key: object) -> object:
        pass

    @abstractmethod
    def closest_element_after(self, key: object) -> object:
        pass

    @abstractmethod
    def binary_search(self, key: object, low: int, high: int) -> object:
        pass