from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def build_bst(self, nums, low, high):

        if low > high:
            return None
        else:
            mid = (low + high) // 2
            root = TreeNode(nums[mid])
            root.left = self.build_bst(nums, low, mid - 1)
            root.right = self.build_bst(nums, mid + 1, high)
            return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build_bst(nums, 0, len(nums) - 1)

    def pre_order_traversal(self, node: TreeNode, indent):
        # Root
        if node:
            print(f"{indent}'{node.val}'")
        else:
            return
        indent = indent + "-"
        # Left
        self.pre_order_traversal(node.left, indent)
        # Right
        self.pre_order_traversal(node.right, indent)


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
    node6 = TreeNode(6, None, None)
    node4.right = node6

    root = solution.sortedArrayToBST([-10, -3, 0, 5, 9])
    solution.pre_order_traversal(root, "")
    root = solution.sortedArrayToBST([1, 3])
    solution.pre_order_traversal(root, "")
    root = solution.sortedArrayToBST([1])
    solution.pre_order_traversal(root, "")
    root = solution.sortedArrayToBST([])
    solution.pre_order_traversal(root, "")

test()
