from typing import List
from typing import Optional

# Definition for a binary tree node.
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

    res = None

    def in_order_traversal(self, node: TreeNode, k, arr):

        if len(arr) > k:
            return

        # Root
        if not node:
            return None

        # Left
        self.in_order_traversal(node.left, k, arr)

        arr.append(node.val)

        # Right
        self.in_order_traversal(node.right, k, arr)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        self.in_order_traversal(root, 3, arr)
        print(arr)
        return arr[k-1]


def test():
    solution = Solution()
    # test method
    root = TreeNode(5, None, None)
    node3 = TreeNode(3, None, None)
    root.left = node3
    node6 = TreeNode(6, None, None)
    root.right = node6

    node2 = TreeNode(2, None, None)
    node3.left = node2
    node4 = TreeNode(4, None, None)
    node3.right = node4

    node1 = TreeNode(1, None, None)
    node2.left = node1

    #pre_order_traversal(root, "")

    print(solution.kthSmallest(root, 3))


test()
