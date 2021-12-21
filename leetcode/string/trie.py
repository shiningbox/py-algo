from typing import List
from typing import Optional

class Node:
    def __init__(self):
        # Note that using a dictionary for children (as in this implementation)
        # would not by default lexicographically sort the children, which is
        # required by the lexicographic sorting in the Sorting section.
        # For lexicographic sorting, we can instead use an array of Nodes.
        self.children = {}  # mapping from character to Node
        self.value = None


def insert(node: Node, key: str, value) -> None:
    """Insert key/value pair into node."""
    for char in key:
        # Create a new node
        if char not in node.children:
            node.children[char] = Node()
        # Move to next
        node = node.children[char]
    node.value = value

def find(node: Node, key: str):
    """Find value by key in node."""
    for char in key:
        if char in node.children:
            node = node.children[char]
        else:
            return None
    return node.value

def print_tires(node, indent):

    if not node:
        return None

    if not node.children:
        return None

    str_val = "".join(node.children.keys())
    print(indent + str_val)

    for child in node.children.values():
        print_tires(child, indent + "-")


def pre_order_traversal(node, indent):

    if not node:
        return None

    if not node.children:
        return None

    str_val = "".join(node.children.keys())
    print(indent + str_val)

    for child in node.children.values():
        pre_order_traversal(child, indent + "-")


def test():
    root = Node()
    wordDict = ["apple", "pen"]
    for word in wordDict:
        insert(root, word, 0)
    pre_order_traversal(root, "-")

test()
