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

    def find(self, key: str):
        node = self.root
        """Find value by key in node."""
        for char in key:
            found = False
            # If char is in one of children
            # Move to its children
            for child in node.children:
                if child.key == char:
                    found = True
                    node = child
                    break

            if not found:
                return None

        return node.count

    def print_tires(self, node, indent):

        if not node:
            return None

        if node.count:
            print(indent + node.key + " " + str(node.count))
        else:
            print(indent + node.key)

        for child in node.children:
            self.print_tires(child, indent + "-")

    def dfs_tires(self, node, path):

        if not node:
            return None

        path += node.key

        if node.count:
            if not self.node_counts[node.count]:
                self.node_counts[node.count] = [node.key]
            else:
                self.node_counts[node.count].append(path)

        for child in node.children:
            self.dfs_tires(child, path)

    def find_counts(self, n):
        self.node_counts = [None] * n
        self.dfs_tires(self.root, "")


class Solution:

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pass


def test():
    solution = Solution()
    # test method
    #print(solution.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
    root = Node("-")
    insert(root, "coding")
    insert(root, "i")
    insert(root, "i")
    insert(root, "love")
    insert(root, "love")
    print_tires(root, "")

test()
