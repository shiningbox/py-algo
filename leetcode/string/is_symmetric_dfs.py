from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def is_mirror(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack and len(stack) > 0:

            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue
            elif None in [node1, node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                else:
                    #Continue with next level nodes
                    stack.append([node1.right, node2.left])
                    stack.append([node1.left, node2.right])

        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_mirror(root.left, root.right)


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

    print(solution.isSymmetric(root1))


test()
