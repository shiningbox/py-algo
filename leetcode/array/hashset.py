from typing import List
from typing import Optional


class MyHashSet:

    def __init__(self):
        self.table_size = 1051
        self.table = [None] * self.table_size

    def hash_function(self, key: int):
        return (key * 2 + 1) % self.table_size

    def add(self, key: int) -> None:
        index = self.hash_function(key)
        if not self.table[index]:
            key_bucket = set()
            key_bucket.add(key)
            self.table[index] = key_bucket
        else:
            self.table[index].add(key)

    def remove(self, key: int) -> None:
        index = self.hash_function(key)
        if self.table[index]:
            if key in self.table[index]:
                self.table[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self.hash_function(key)
        if not self.table[index]:
            return False
        else:
            key_bucket = self.table[index]
            if key in key_bucket:
                return True
            else:
                return False

class Solution:
    pass


key = 1
obj = MyHashSet()
obj.add(key)
print(obj.contains(key))
obj.remove(key)
print(obj.contains(key))

param_3 = obj.contains(key)

