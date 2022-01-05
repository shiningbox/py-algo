from typing import List
from typing import Optional

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

# Print the tree
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


class Solution(object):

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def build_max_bst(nums, l, h):

            if l > h:
                return

            max_index = nums.index(max(nums[l:h+1]))
            root = TreeNode(nums[max_index])
            root.left = build_max_bst(nums, l, max_index - 1)
            root.right = build_max_bst(nums, max_index + 1, h)

            return root

        return build_max_bst(nums, 0, len(nums) - 1)


def test():
    solution = Solution()
    root = solution.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
    pre_order_traversal(root, "")


test()
