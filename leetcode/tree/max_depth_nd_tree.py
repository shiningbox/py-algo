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

    def max_depth(self, node: 'Node'):

        if not node:
            return 0

        # Root
        if not node.children:
            return 1
        child_max = 0
        for child in node.children:
               child_depth = self.max_depth(child)
               if child_depth >= child_max:
                   child_max = child_depth
        return child_max + 1

    def maxDepth(self, root: 'Node') -> int:
        return self.max_depth(root)


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
    pre_order_traversal(root, "")

    print(solution.maxDepth(root))
    print(solution.maxDepth(None))

test()
