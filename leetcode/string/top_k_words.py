from typing import List
from typing import Optional
from typing import List
from typing import Optional


class Node:

    def __init__(self, key=None):
        # For lexicographic sorting, we can instead use an array of Nodes.
        self.children = []  # mapping from character to Node
        self.key = key
        self.count = None

    def sorted_insert(self, node):
        index = len(self.children)
        # Searching for the position
        for i in range(len(self.children)):
            if self.children[i].key > node.key:
                index = i
                break
        # Inserting node in the list
        if index == len(self.children):
            res = self.children[:index] + [node]
        else:
            res = self.children[:index] + [node] + self.children[index:]
        self.children = res

    def print(self):
        print(self.key)
        for child in self.children:
            print(child.key, end=" ")
        print()


class SortedTire:

    def __init__(self):
        self.root = Node("-")
        self.node_counts = []

    def insert(self, key: str) -> None:
        node = self.root
        new_child = None
        for char in key:
            found = False
            # If char already in node's children
            for child in node.children:
                if child.key == char:
                    node = child
                    found = True
                    break

            # If it is a new child
            if not found:
                new_child = Node(char)
                node.sorted_insert(new_child)
                # Move to next
                node = new_child

        if node.count:
            node.count += 1
        else:
            node.count = 1

    def dfs_tires(self, node, path):

        if not node:
            return None

        if node.key != "-":
            path += node.key

        if node.count:
            idx = node.count
            if not self.node_counts[idx]:
                self.node_counts[idx] = [path]
            else:
                self.node_counts[idx].append(path)

        for child in node.children:
            self.dfs_tires(child, path)

    def find_counts(self, n):
        self.node_counts = [None] * (n + 1)
        self.dfs_tires(self.root, "")


class Solution:

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        tires = SortedTire()

        for key in words:
            tires.insert(key)

        tires.find_counts(len(words))
        counts = tires.node_counts
        res = []
        for i in range(len(counts) - 1, -1, -1):
            if counts[i]:
                for word in counts[i]:
                    if len(res) < k:
                        res.append(word)
                    else:
                        return res
        return res


def test():
    solution = Solution()
    # test method
    print(solution.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
    print(solution.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))
    print(solution.topKFrequent(["the", "the"], 1))
    print(solution.topKFrequent(["the"], 1))



test()
