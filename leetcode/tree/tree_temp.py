from typing import List
from typing import Optional

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

# Print the tree
def pre_order_traversal(node: TreeNode, indent):
    # Root
    if node:
        print(f"{indent}'{node.val}'")
    else:
        return
    indent = indent + "-"
    # Left
    pre_order_traversal(node.left, indent)
    # Right
    pre_order_traversal(node.right, indent)


class Solution:
    pass


def test():
    solution = Solution()
    # test method
    root = TreeNode(3, None, None)
    node2 = TreeNode(2, None, None)
    root.left = node2
    node4 = TreeNode(4, None, None)
    root.right = node4

    node44 = TreeNode(4, None, None)
    node4.left = node44
    node5 = TreeNode(5, None, None)
    node4.right = node5

    node33 = TreeNode(3, None, None)
    node44.left = node33

    node444 = TreeNode(4, None, None)
    node44.right = node444
    # test method
    # print(solution.method("test"))


test()
