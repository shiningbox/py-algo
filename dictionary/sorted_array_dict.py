from dictionary.adt import OrderedDictionary, DictionaryException
from priority_queue.adt import Item, Comparator


class OrderedArrayDict(OrderedDictionary):

    CAPACITY = 1000

    def __init__(self):
        self.sequence_size = 0
        self.array = [None] * OrderedArrayDict.CAPACITY

    def element_at_i(self, i):
        return self.array[i]

    def closest_key_before(self, key: object) -> object:
        pass

    def closest_element_before(self, key: object) -> object:
        pass

    def closest_key_after(self, key: object) -> object:
        for item in self.array:
            if item.key >= key:
                return item.key

    def closest_element_after(self, key: object) -> object:
        key = self.closest_key_after(key)
        return self.find_element(key)

    def size(self) -> int:
        return self.sequence_size

    def is_empty(self) -> bool:
        return self.sequence_size == 0

    # O(logn)
    def binary_search(self, key: object, low: int, high: int) -> object:

        #print(f'{low}, {high}')
        if low > high:
            return 'NO_SUCH_KEY'

        mid = int((low + high) / 2)
        low_key = self.array[low].key
        high_key = self.array[high].key

        mid_key = self.array[mid].key

        # Find the key
        if Comparator.is_equal_to(key, mid_key):
            return self.array[mid]

        if Comparator.is_equal_to(key, low_key):
            return self.array[low]

        if Comparator.is_equal_to(key, high_key):
            return self.array[high]

        if Comparator.is_greater_than_equal_to(key, mid_key):
            return self.binary_search(key, mid + 1, high)
        elif Comparator.is_less_than_equal_to(key, mid_key):
            return self.binary_search(key, low, mid-1)

    def find_element(self, key: object) -> object:
        return self.binary_search(key, 0, self.size() - 1)

    # O(n)
    def iterate_and_find(self, key: object) -> object:
        element = None
        for index in range(self.size()):
            if self.array[index].key == key:
                element = self.array[index].element
        if element is None:
            return 'NO_SUCH_KEY'
        else:
            return element

    def find_all_elements(self, key: object) -> list:
        pass

    def insert_item(self, key: object, element: object) -> object:
        new_item = Item(key, element)
        if self.is_empty():
            self.array[0] = new_item
            self.sequence_size += 1
            return new_item

        index_insert = -1
        # Find an existing key which larger than the new key
        for index in range(self.size()):
            if Comparator.is_greater_than_equal_to(self.array[index].key, new_item.key):
                index_insert = index
                break

        # If it is the last item
        if index_insert == -1:
            self.array[self.sequence_size] = new_item
            self.sequence_size += 1
            new_item.rank = self.sequence_size - 1
            return new_item
        else:
            # Shift item from k to n-1 by 1
            for index in range(self.sequence_size-1, index_insert-1, -1):
                self.array[index + 1] = self.array[index]
            self.array[index_insert] = new_item
            new_item.rank = index_insert
            self.sequence_size += 1
            return new_item

    def insert_last(self, key: object, element: object) -> object:
        new_item = Item(key, element)
        self.array[self.sequence_size] = new_item
        self.sequence_size += 1

    def remove(self, key: object) -> object:
        pass

    def remove_all(self, key: object) -> list:
        pass

    def print_dict(self):
        if not self.is_empty():
            for i in range(self.size()):
                print(f"{self.array[i].key}, {self.array[i].element}", end=">")
            print("")
        else:
            print("Empty dictionary")

def simple_test():
    dict = OrderedArrayDict()
    dict.insert_item(5, 'E')
    dict.insert_item(6, 'F')
    dict.insert_item(1, 'A')
    dict.insert_item(3, 'C')
    dict.insert_item(4, 'D')
    dict.insert_item(2, 'B')
    dict.insert_item(8, 'O')
    dict.insert_item(5, 'E1')
    dict.insert_item(5, 'E2')
    dict.insert_item(7, 'G')
    dict.insert_item(9, 'P')
    #print(dict.find_element(5))
    #print(dict.find_element(3))
    dict.print_dict()


    print("find keys 1, 2, 3, 4, 5, 6, 7, 8, 9")
    print(dict.find_element(1))
    print(dict.find_element(2))
    print(dict.find_element(3))
    print(dict.find_element(4))
    print(dict.find_element(5))
    print(dict.find_element(6))
    print(dict.find_element(7))
    print(dict.find_element(8))
    print(dict.find_element(9))

    print(dict.closest_key_after(4.5))
    print(dict.closest_key_after(6))

#simple_test()