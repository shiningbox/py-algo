from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    # DFS with stack
    # BFS with queue
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p and q:
            return p.val == q.val and (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))

        if p == q:
            return True
        else:
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

    root2 = TreeNode(1, None, None)
    node2 = TreeNode(2, None, None)
    root2.right = node2
    node3 = TreeNode(3, None, None)
    node2.left = node3
    node4 = TreeNode(4, None, None)
    node2.right = node4
    node5 = TreeNode(5, None, None)
    node4.left = node5

    root3 = TreeNode(1, None, None)
    node2 = TreeNode(2, None, None)
    root3.right = node2

    print(solution.isSameTree(root1, root2))
    print(solution.isSameTree(root1, root3))
    print(solution.isSameTree(root2, root3))
    print(solution.isSameTree(None, None))


test()
