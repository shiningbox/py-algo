from typing import List
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def expand_trees(self, nums, i):

        # Stop expanding
        if len(nums) == 1:
            return 1

        left_children = nums[:i]
        right_children = nums[i + 1:]

        # If has left children
        left_res = 0
        if left_children:
            for j in range(len(left_children)):
                left_res += self.expand_trees(left_children, j)

        right_res = 0
        if right_children:
            for k in range(len(right_children)):
                right_res += self.expand_trees(right_children, k)

        if left_res == 0:
            return right_res
        elif right_res == 0:
            return left_res
        else:
            return left_res * right_res

    def numTrees(self, n: int) -> int:

        nums = list(range(1, n + 1))
        res = 0
        for i in range(len(nums)):
            res += self.expand_trees(nums, i)
        return res

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

def test():
    solution = Solution()
    # test method
    print(solution.numTrees(1))
    print(solution.numTrees(2))
    print(solution.numTrees(3))
    print(solution.numTrees(4))
    print(solution.numTrees(5))
    print(solution.numTrees(6))
    print(solution.numTrees(7))
    print(solution.numTrees(8))
    print(solution.numTrees(20))


test()
