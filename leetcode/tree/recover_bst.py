from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def in_order_traversal(self, node: TreeNode, res):
        # Root
        if not node:
            return
        # Left
        self.in_order_traversal(node.left, res)
        res.append(node)
        # Right
        self.in_order_traversal(node.right, res)

    def print_list(self, res):
        for num in res:
            print(num.val, end="")
        print()

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        res = []
        self.in_order_traversal(root, res)
        i = 0
        length = len(res)
        while i < length:
            j = 0
            while j < length - i - 1:
                if res[j].val > res[j + 1].val:
                    res[j].val, res[j + 1].val = res[j + 1].val, res[j].val
                j += 1
            i += 1


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


def test():
    solution = Solution()

    # test method
    root = TreeNode(1, None, None)
    node11 = TreeNode(3, None, None)
    root.left = node11
    node12 = TreeNode(2, None, None)
    node11.right = node12
    solution.recoverTree(root)
    pre_order_traversal(root, "")

    root = TreeNode(5, None, None)
    node11 = TreeNode(1, None, None)
    root.left = node11
    node12 = TreeNode(4, None, None)
    root.right = node12
    node21 = TreeNode(3, None, None)
    node12.left = node21
    node22 = TreeNode(6, None, None)
    node12.right = node22

    solution.recoverTree(root)
    pre_order_traversal(root, "")


test()
