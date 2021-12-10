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


class Solution:

    def buildTree(self, inorder, postorder):
        if inorder:
            last = postorder.pop()
            idx = inorder.index(last)
            root = TreeNode(inorder[idx])
            root.right = self.buildTree(inorder[idx + 1:], postorder)
            root.left = self.buildTree(inorder[0:idx], postorder)
            return root

def test():
    solution = Solution()
    # test method
    root = solution.buildTree([9,3,15,20,7], [9,15,7,20,3])
    pre_order_traversal(root, "")


test()
