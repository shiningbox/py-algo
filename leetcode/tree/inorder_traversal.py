from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:

    def traversal(self, values, root):

        if root is None:
            return None

        self.traversal(values, root.left)
        values.append(root.val)
        self.traversal(values, root.right)

    # left -> root -> right
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.traversal(values, root)
        return values


def test():
    solution = Solution()
    # test method
    root1 = TreeNode(1, None, None)
    node2 = TreeNode(2, None, None)
    root1.right = node2
    node3 = TreeNode(3, None, None)
    node2.left = node3
    print(solution.inorderTraversal(root1))
    print(solution.inorderTraversal(None))


test()
