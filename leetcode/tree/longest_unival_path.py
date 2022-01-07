from typing import List
from typing import Optional



# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

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


class Solution:

    max = 0

    def find_path(self, node):

        if not node:
            return 0

        left = right = False

        left_path = self.find_path(node.left)
        if node.left:
            if node.val == node.left.val:
                left = True
                left_path += 1
            else:
                left_path = 0

        right_path = self.find_path(node.right)
        if node.right:
            if node.val == node.right.val:
                right = True
                right_path += 1
            else:
                right_path = 0

        if left and right:
            path = left_path + right_path
        else:
            path = max(left_path, right_path)

        if self.max <= path:
            self.max = path

        return max(left_path, right_path)


    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        self.find_path(root)
        return self.max

def test():
    solution = Solution()
    # test method
    root1 = TreeNode(6, None, None)
    node11 = TreeNode(2, None, None)
    root1.left = node11
    node12 = TreeNode(2, None, None)
    root1.right = node12
    node21 = TreeNode(2, None, None)
    node11.left = node21
    node22 = TreeNode(2, None, None)
    node11.right = node22
    node31 = TreeNode(2, None, None)
    node22.left = node31
    node32 = TreeNode(2, None, None)
    node22.right = node32
    node23 = TreeNode(7, None, None)
    node12.left = node23
    node24 = TreeNode(9, None, None)
    node12.right = node24

    pre_order_traversal(root1, "")

    print(solution.longestUnivaluePath(root1))
    #print(solution.binaryTreePaths(root2))

    root2 = TreeNode(1, None, None)
    node11 = TreeNode(2, None, None)
    root2.left = node11
    node12 = TreeNode(8, None, None)
    root2.right = node12
    node21 = TreeNode(2, None, None)
    node11.left = node21
    node22 = TreeNode(2, None, None)
    node11.right = node22
    node31 = TreeNode(2, None, None)
    node22.left = node31
    node32 = TreeNode(5, None, None)
    node22.right = node32
    node23 = TreeNode(7, None, None)
    node12.left = node23
    node24 = TreeNode(9, None, None)
    node12.right = node24

    #print(solution.longestUnivaluePath(root2))



test()
