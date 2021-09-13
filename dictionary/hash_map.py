from dictionary.adt import Dictionary, DictionaryException
from dictionary.sorted_array_dict import OrderedArrayDict
from list.array_sequence import ArraySequence

class HashMapDictionary(Dictionary):
    CAPACITY = 37

    def __init__(self):
        self.bucket_array = ArraySequence(HashMapDictionary.CAPACITY)
        for index in range(HashMapDictionary.CAPACITY):
            self.bucket_array.sequence[index] = OrderedArrayDict()
            self.bucket_array.sequence_size += 1

    def size(self) -> int:
        pass

    def is_empty(self) -> bool:
        pass

    def find_element(self, key: object) -> object:
        rank = self.hash_function(key)
        bucket_dict = self.bucket_array.elem_at_rank(rank)
        return bucket_dict.find_element(key)

    def find_all_elements(self, key: object) -> list:
        pass

    def insert_item(self, key: object, element: object):
        # Hash the key to the integer
        rank = self.hash_function(key)
        # If it is the last element
        bucket_dict = self.bucket_array.elem_at_rank(rank)
        bucket_dict.insert_item(key, element)

    def remove(self, key: object) -> object:
        pass

    def remove_all(self, key: object) -> list:
        pass

    @staticmethod
    def hash_function(key: object) -> int:
        return key % HashMapDictionary.CAPACITY

    def print_dict(self):
        for bucket_dict in self.bucket_array.sequence:
            bucket_dict.print_dict()


dict = HashMapDictionary()
dict.insert_item(5, 'E')
dict.insert_item(6, 'F')
dict.insert_item(1, 'A')
dict.insert_item(3, 'C')
dict.insert_item(4, 'D')
dict.insert_item(34, 'B')
dict.insert_item(8, 'H')
dict.insert_item(42, 'G')
dict.insert_item(36, 'I')
dict.insert_item(62, 'J')
dict.print_dict()


print(dict.find_element(42))
print(dict.find_element(7))
print(dict.find_element(6))
