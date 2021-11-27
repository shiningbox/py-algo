from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def sum_left_leaves(self, root):
        sum = 0

        if not root:
            return sum

        # If root has left_stack child
        # and left_stack child is a leaf
        if root.left and not root.left.left and not root.left.right:
            sum += root.left.val

        sum += self.sum_left_leaves(root.left)
        sum += self.sum_left_leaves(root.right)

        return sum

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.sum_left_leaves(root)

def test():
    solution = Solution()
    # test method
    root = TreeNode(6, None, None)
    node2 = TreeNode(2, None, None)
    root.left = node2
    node8 = TreeNode(8, None, None)
    root.right = node8

    node9 = TreeNode(9, None, None)
    node8.left = node9
    node11 = TreeNode(11, None, None)
    node8.right = node11

    node1 = TreeNode(1, None, None)
    node2.left = node1
    node4 = TreeNode(4, None, None)
    node2.right = node4

    node3 = TreeNode(3, None, None)
    node4.left = node3
    node5 = TreeNode(5, None, None)
    node4.right = node5

    root2 = TreeNode(1, None, None)

    print(solution.sumOfLeftLeaves(root))
    print(solution.sumOfLeftLeaves(root2))


test()
