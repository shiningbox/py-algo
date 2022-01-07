from typing import List
from typing import Optional


class Node:

    def __init__(self):
        self.value = None
        self.children = {}

class MapSum:

    def __init__(self):
        self.root = Node()
        self.res = 0

    def print_tree(self, node, indent):

        if not node:
            return None

        if not node.children:
            return None

        res = ""
        for key, child in node.children.items():
            if child.value:
                res += key + " " + str(child.value)
            else:
                res += key

        print(indent + res)

        for child in node.children.values():
            self.print_tree(child, indent + "-")

    def preorder_traversal(self, node):

        if not node:
            return None

        if not node.children:
            return None

        for key, child in node.children.items():
            if child.value:
                self.res += child.value

        for child in node.children.values():
            self.preorder_traversal(child)

    def find(self, node: Node, key: str):
        """Find value by key in node."""
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

    def insert(self, key: str, val: int) -> None:

        node = self.root
        """Insert key/value pair into node."""
        for char in key:
            # Create a new node
            if char not in node.children:
                node.children[char] = Node()
            # Move to next
            node = node.children[char]
        node.value = val

    def sum(self, prefix: str) -> int:
        self.res = 0
        # Find the root with key equals to the last char of prefix
        # e.g., app, find the node from root -> a -> p -> p
        root = self.find(self.root, prefix)
        if root:
            if root.value:
                self.res += root.value
        self.preorder_traversal(root)
        return self.res



# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("apple", 3)
obj.insert("app", 2)
obj.print_tree(obj.root, "-")
obj.sum("app")
# param_2 = obj.sum(prefix)