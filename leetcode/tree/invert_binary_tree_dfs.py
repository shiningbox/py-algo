from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:

    def swap_children(self, root):
        stack = [root]
        while stack and len(stack) > 0:
            # Process node
            node = stack.pop()

            if not node:
                continue
            else:
                if not node.left and not node.right:
                    continue
                else:
                    # swap the left and right child of root
                    temp = node.left
                    node.left = node.right
                    node.right = temp

                    # Continue with next level nodes
                    stack.append(node.left)
                    stack.append(node.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.swap_children(root)
        return root

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
    root = TreeNode(4, None, None)
    node11 = TreeNode(2, None, None)
    root.left = node11
    node12 = TreeNode(7, None, None)
    root.right = node12
    node21 = TreeNode(1, None, None)
    node11.left = node21
    node22 = TreeNode(3, None, None)
    node11.right = node22
    node23 = TreeNode(6, None, None)
    node12.left = node23
    node24 = TreeNode(9, None, None)
    node12.right = node24

    pre_order_traversal(root, "")
    result = solution.invertTree(root)
    pre_order_traversal(result, "")


test()
