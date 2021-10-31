from typing import List
from typing import Optional

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# Print the tree
def pre_order_traversal(node: Node, indent):
    # Root
    if node:
        print(f"{indent}'{node.val}'")
    else:
        return
    indent = indent + "-"

    if node.children:
        for child in node.children:
            pre_order_traversal(child, indent)


class Solution:
    def __init__(self):
        self.results = []

    def pre_order(self, root):
        # Root
        if root:
            self.results.append(root.val)
        else:
            return

        if root.children:
            for child in root.children:
                self.pre_order(child)

    def preorder(self, root: 'Node') -> List[int]:
        self.pre_order(root)
        return self.results


def test():
    solution = Solution()
    # test method
    root = Node(1, None)
    node2 = Node(2, None)
    node3 = Node(3, None)
    node4 = Node(4, None)
    r_children = []
    r_children.append(node2)
    r_children.append(node3)
    r_children.append(node4)
    root.children = r_children

    node5 = Node(5, None)
    node6 = Node(6, None)
    node_children = []
    node_children.append(node5)
    node_children.append(node6)
    node3.children = node_children
    print(solution.preorder(root))


test()
