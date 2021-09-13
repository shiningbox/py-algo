from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        stack = []

        if root:
            stack = [(root, root.val)]

        while stack and len(stack) > 0:
            top, top_val = stack.pop()
            # If top is a leaf node
            if not top.left and not top.right:
                if top_val == targetSum:
                    return True
            else:
                if top.right:
                    stack.append((top.right, top.right.val + top_val))
                if top.left:
                    stack.append((top.left, top.left.val + top_val))

        return False

def test():
    solution = Solution()
    # test method
    root1 = TreeNode(1, None, None)
    node2 = TreeNode(2, None, None)
    root1.right = node2
    node3 = TreeNode(3, None, None)
    node2.left = node3
    node4 = TreeNode(4, None, None)
    node2.right = node4
    node5 = TreeNode(5, None, None)
    node4.left = node5
    # pre_order_traversal(root, "")

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

    print(solution.hasPathSum(root1, 6))
    print(solution.hasPathSum(root2, 10))
    print(solution.hasPathSum(root2, 11))
    print(solution.hasPathSum(None, 11))

test()
