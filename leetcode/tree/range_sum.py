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

    def __init__(self):
        self.sum = 0

    def range_sum(self, root, low, high):

        if not root:
            return None

        if low <= root.val <= high:
            self.sum += root.val
            self.range_sum(root.left, low, high)
            self.range_sum(root.right, low, high)
        elif root.val > high:
            self.range_sum(root.left, low, high)
        else:
            self.range_sum(root.right, low, high)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0
        self.range_sum(root, low, high)
        return self.sum


def test():
    solution = Solution()
    # test method
    root = TreeNode(3, None, None)
    node2 = TreeNode(2, None, None)
    root.left = node2
    node4 = TreeNode(4, None, None)
    root.right = node4

    node1 = TreeNode(1, None, None)
    node2.left = node1

    node3 = TreeNode(3, None, None)
    node4.left = node3
    node6 = TreeNode(6, None, None)
    node4.right = node6

    node5 = TreeNode(5, None, None)
    node6.left = node5

    node9 = TreeNode(9, None, None)
    node6.right = node9

    pre_order_traversal(root, "")

    print(solution.rangeSumBST(root, 2, 8))

test()
