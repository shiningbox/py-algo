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

    def __init__(self):
        self.global_max = 0

    def max_depth(self, root):

        if not root.left and not root.right:
            return 1

        left_max = 0
        right_max = 0

        if root.left:
            left_max = self.max_depth(root.left)
        if root.right:
            right_max = self.max_depth(root.right)

        root_max = max(left_max, right_max) + 1

        max_path = left_max + right_max

        if max_path >= self.global_max:
            self.global_max = max_path

        return root_max

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.global_max = 0
        root_max = self.max_depth(root)
        print(root_max)
        return self.global_max


def test():
    solution = Solution()
    # test method
    root = TreeNode(3, None, None)
    node2 = TreeNode(2, None, None)
    root.left = node2
    node4 = TreeNode(4, None, None)
    root.right = node4

    node1 = TreeNode(1, None, None)
    node2.left = node1

    node3 = TreeNode(3, None, None)
    node4.left = node3
    node6 = TreeNode(6, None, None)
    node4.right = node6

    node5 = TreeNode(5, None, None)
    node6.left = node5

    node9 = TreeNode(9, None, None)
    node6.right = node9

    pre_order_traversal(root, "")

    print(solution.diameterOfBinaryTree(root))

    # test method
    root = TreeNode(1, None, None)
    node2 = TreeNode(2, None, None)
    root.left = node2
    node3 = TreeNode(3, None, None)
    root.right = node3

    node4 = TreeNode(4, None, None)
    node2.left = node4
    node5 = TreeNode(5, None, None)
    node2.right = node5

    pre_order_traversal(root, "")

    print(solution.diameterOfBinaryTree(root))


test()
