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

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        return self.searchBST(root.left, val) or self.searchBST(root.right, val)


def test():
    solution = Solution()
    # test method
    root = TreeNode(5, None, None)
    node3 = TreeNode(3, None, None)
    root.left = node3
    node6 = TreeNode(6, None, None)
    root.right = node6

    node2 = TreeNode(2, None, None)
    node3.left = node2
    node4 = TreeNode(4, None, None)
    node3.right = node4

    node7 = TreeNode(7, None, None)
    node6.left = node7

    pre_order_traversal(root, "")

    print(solution.searchBST(root, 7))
    print(solution.searchBST(root, 5))
    print(solution.searchBST(root, 8))

test()
