from typing import List
from typing import Optional


class LRUCache:

    class Node:

        def __init__(self, key=None, val=None):
            self.key = key
            self.val = val

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [] * capacity
        self.idx_dict = {}

    def get(self, key: int) -> int:
        # Move
        idx = - 1
        if key in self.idx_dict:
            idx = self.idx_dict[key]
        else:
            return idx

        if idx < 0 or idx >= len(self.array):
            return -1
        else:
            # Put the node to front
            node = self.array[idx]
            self.array.remove(node)
            self.array.insert(0, node)
            self.reindex()
            return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.idx_dict:
            idx = self.idx_dict[key]
            node = self.array[idx]
            self.array.remove(node)
            node.val = value
            self.array.insert(0, node)
            self.reindex()
            return

        node = LRUCache.Node(key, value)
        size = len(self.array)
        if size < self.capacity:
            self.array.insert(0, node)
            self.reindex()
        else:
            # Evict the first and insert
            self.evict()
            self.array.insert(0, node)
            self.reindex()

    def reindex(self):
        for i in range(len(self.array)):
            self.idx_dict[self.array[i].key] = i

    def evict(self):
        # Pop the last
        top = self.array.pop()
        # Update index
        del self.idx_dict[top.key]

    def print_dict(self):
        for node in self.array:
            print(node.key, node.val, end="->")
        print(self.idx_dict)
        print("")




"""

["LRUCache","get","put","get","put","put","get","get"]
[[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]"""

lRUCache = LRUCache(2)
print(lRUCache.get(2))  # cache is {1=1}
lRUCache.put(2, 6)  # cache is {1=1, 2=2}
print(lRUCache.get(1))  # cache is {1=1}
print(lRUCache.print_dict())
lRUCache.put(1, 5)  # cache is {1=1, 2=2}
print(lRUCache.print_dict())
lRUCache.put(1, 2)  # cache is {1=1, 2=2}
print(lRUCache.print_dict())
print(lRUCache.get(1))  # cache is {1=1}
print(lRUCache.get(2))  # cache is {1=1}
