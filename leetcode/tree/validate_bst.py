from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def is_sub_bst(self, node):

        if not node:
            return True

        if not node.left and not node.right:
            return True
        elif not node.left and node.right:
            if node.val < node.right.val:
                return True
            else:
                return False
        elif not node.right and node.left:
            if node.val > node.left.val:
                return True
            else:
                return False
        else:
            if node.left.val < node.val < node.right.val:
                return True
            else:
                return False

    def is_parent_bst(self, left, right, node):

        if not node:
            return True
        for l in left:
            if node.val >= l:
                return False
        for r in right:
            if node.val <= r:
                return False
        return True

    def check(self, left, right, node: TreeNode) -> int:

        if not node:
            return True

        h_l = self.check(left + [node.val], right, node.left)
        h_r = self.check(left, right + [node.val], node.right)

        if not h_l or not h_r or not self.is_sub_bst(node) or not self.is_parent_bst(left, right, node):
            return False
        # Otherwise returns a height
        else:
            return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check([], [], root)


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
    pre_order_traversal(root, "")
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
    pre_order_traversal(root, "")

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
    pre_order_traversal(root, "")

    print(solution.isValidBST(root))

test()
