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

    def print_stack(self, stack):
        for node in stack:
            print(node.val, end=",")
        print()

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        stack = [root]
        prev = TreeNode(-1)
        while stack:
            head = stack.pop(0)

            if head.right:
                stack.insert(0, head.right)
            if head.left:
                stack.insert(0, head.left)

            prev.right = head
            prev.left = None
            prev = head


def test():
    solution = Solution()
    # test method
    root = TreeNode(1, None, None)
    node2 = TreeNode(2, None, None)
    root.left = node2
    node5 = TreeNode(5, None, None)
    root.right = node5

    node3 = TreeNode(3, None, None)
    node2.left = node3
    node4 = TreeNode(4, None, None)
    node2.right = node4

    node6 = TreeNode(6, None, None)
    node5.right = node6

    #pre_order_traversal(root, "")
    solution.flatten(root)
    pre_order_traversal(root, "")

    solution.flatten(None)

    solution.flatten(0)


test()
