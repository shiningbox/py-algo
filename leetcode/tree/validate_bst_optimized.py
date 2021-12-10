from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def in_order_traversal(self, node: TreeNode,  res):
        # Root
        if not node:
            return

        # Left
        self.in_order_traversal(node.left,  res)
        res.append(node.val)
        # Right
        self.in_order_traversal(node.right, res)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        self.in_order_traversal(root, res)
        sorted_res = list(res)
        sorted_res.sort()
        equal_unique = True

        for i in range(len(res)):
            if i > 0 and res[i] == res[i - 1]:
                return False
            if res[i] != sorted_res[i]:
                return False

        return equal_unique


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
    root = TreeNode(2, None, None)
    node11 = TreeNode(1, None, None)
    root.left = node11
    node12 = TreeNode(3, None, None)
    root.right = node12
    print(solution.isValidBST(root))

    root = TreeNode(5, None, None)
    node11 = TreeNode(1, None, None)
    root.left = node11
    node12 = TreeNode(4, None, None)
    root.right = node12
    node21 = TreeNode(3, None, None)
    node12.left = node21
    node22 = TreeNode(6, None, None)
    node12.right = node22

    print(solution.isValidBST(root))

    root = TreeNode(5, None, None)
    node11 = TreeNode(4, None, None)
    root.left = node11
    node12 = TreeNode(6, None, None)
    root.right = node12
    node21 = TreeNode(3, None, None)
    node12.left = node21
    node22 = TreeNode(7, None, None)
    node12.right = node22

    print(solution.isValidBST(root))

test()
