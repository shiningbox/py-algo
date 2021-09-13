from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def min_depth(self, node: TreeNode):
        # Root
        if not node:
            return 0

        # Left
        d_l = self.min_depth(node.left)
        # Right
        d_r = self.min_depth(node.right)
        if 0 in [d_l, d_r]:
            return sum([d_l, d_r]) + 1
        else:
            return min(d_l, d_r) + 1

    # The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.min_depth(root)

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
    node12 = TreeNode(2, None, None)
    root2.right = node12
    node22 = TreeNode(3, None, None)
    node12.right = node22

    print(solution.minDepth(root))
    print(solution.minDepth(root2))



test()
