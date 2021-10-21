from typing import List
from typing import Optional



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

    def find_modes(self, nums):
        prev = None
        c_count = 0
        m_count = 0
        results = []
        for num in nums:
            if num != prev:
                c_count = 1
            else:
                c_count += 1
            # if c_count, the count of current num equals max count
            # add the current num as well
            if c_count == m_count:
                results.append(num)
            # if c_count of this num is larger than max count
            # then only need to add this num
            elif c_count > m_count:
                results = [num]
                m_count = c_count
            prev = num
        return results

    def in_order(self, root, results):

        if not root:
            return None

        self.in_order(root.left, results)
        # visit root
        results.append(root.val)
        self.in_order(root.right, results)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        self.in_order(root, results)
        return self.find_modes(results)

def test():
    solution = Solution()
    # test method
    root = TreeNode(3, None, None)
    node2 = TreeNode(2, None, None)
    root.left = node2
    node4 = TreeNode(4, None, None)
    root.right = node4

    node44 = TreeNode(4, None, None)
    node4.left = node44
    node5 = TreeNode(5, None, None)
    node4.right = node5

    node33 = TreeNode(3, None, None)
    node44.left = node33

    node444 = TreeNode(4, None, None)
    node44.right = node444

    print(solution.findMode(root))


test()
