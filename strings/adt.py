from abc import ABC, abstractmethod


class String(ABC):

    @abstractmethod
    def length(self) -> int:
        pass

    @abstractmethod
    def char_at(self, index: int) -> chr:
        pass

    @abstractmethod
    def concat(self, string):
        pass

    @abstractmethod
    def ends_with(self, string) -> bool:
        pass

    @abstractmethod
    def starts_with(self, string) -> bool:
        pass

    @abstractmethod
    def equals(self, string) -> bool:
        pass

    @abstractmethod
    def index_of(self, string) -> int:
        pass

    @abstractmethod
    def sub_string(self, i: int, j: int):
        pass

    @abstractmethod
    def append(self, string):
        "Mutable method"
        pass

    @abstractmethod
    def insert(self, index, string):
        "Mutable method"
        pass

    @abstractmethod
    def reverse(self):
        "Mutable method"
        pass

    @abstractmethod
    def set_char(self, index, char):
        "Mutable method"
        pass
