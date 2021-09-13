from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def max_depth(self, node: TreeNode):

        if not node:
            return 0

        return max(self.max_depth(node.left),
                   self.max_depth(node.right)) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.max_depth(root)


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

    root2 = TreeNode(1, None, None)
    node2 = TreeNode(2, None, None)
    root2.right = node2
    node3 = TreeNode(3, None, None)
    node2.left = node3
    node4 = TreeNode(4, None, None)
    node2.right = node4

    root3 = TreeNode(1, None, None)

    print(solution.max_depth(root1))
    print(solution.max_depth(root2))
    print(solution.max_depth(root3))


test()
