from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        stack = []
        res = []
        if root:
            stack = [(root, [root.val])]

        while stack and len(stack) > 0:
            top, path = stack.pop()
            # If top is a leaf node
            if not top.left and not top.right:
                if sum(path) == targetSum:
                    res.append(path)
            else:
                if top.right:
                    stack.append((top.right, path + [top.right.val]))
                if top.left:
                    stack.append((top.left, path + [top.left.val]))

        return res

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

    print(solution.pathSum(root1, 6))


test()
