from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def check(self, node: TreeNode) -> int:
        # Use -1 to mark imbalanced node
        # and other values to mark balanced heights
        if not node:
            return 0
        else:
            h_l = self.check(node.left)
            h_r = self.check(node.right)
            # If children is not balanced then parent is not balanced
            # If children are balanced but their height difference are larger than 1
            if h_l == -1 or h_r == -1 or abs(h_l - h_r) > 1:
                return -1
            # Otherwise returns a height
            else:
                return max(h_l, h_r) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check(root) != -1


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
    root = TreeNode(3, None, None)
    node11 = TreeNode(9, None, None)
    root.left = node11
    node12 = TreeNode(20, None, None)
    root.right = node12
    node21 = TreeNode(15, None, None)
    node12.left = node21
    node22 = TreeNode(7, None, None)
    node12.right = node22
    #pre_order_traversal(root, "")

    root2 = TreeNode(1, None, None)
    node11 = TreeNode(2, None, None)
    root2.left = node11
    node12 = TreeNode(2, None, None)
    root2.right = node12
    node21 = TreeNode(3, None, None)
    node11.left = node21
    node22 = TreeNode(3, None, None)
    node11.right = node22
    node31 = TreeNode(4, None, None)
    node32 = TreeNode(4, None, None)
    node21.left = node31
    node21.right = node32
    #pre_order_traversal(node2, "")

    print(solution.isBalanced(root))
    print(solution.isBalanced(root2))
    #print(solution.check(node31))

test()
