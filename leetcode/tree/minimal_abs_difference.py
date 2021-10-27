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
        self.min_diff = 10 ** 5
        self.prev = None

    def in_order(self, root):

        if not root:
            return None

        # Find the previous in_order of root
        self.in_order(root.left)

        if self.prev and abs(root.val - self.prev.val) <= self.min_diff:
            self.min_diff = abs(root.val - self.prev.val)

        self.prev = root

        self.in_order(root.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = 10 ** 5
        if not root:
            return None
        self.in_order(root)
        return self.min_diff


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

    #pre_order_traversal(root, "")
    print(solution.getMinimumDifference(root))

    root = TreeNode(1, None, None)
    node3 = TreeNode(3, None, None)
    root.right = node3
    node5 = TreeNode(5, None, None)
    node3.right = node5

    pre_order_traversal(root, "")

    print(solution.getMinimumDifference(root))

    root = TreeNode(1, None, None)
    node5 = TreeNode(5, None, None)
    root.right = node5
    node3 = TreeNode(3, None, None)
    node5.left = node3

    pre_order_traversal(root, "")

    print(solution.getMinimumDifference(root))

    root = TreeNode(1, None, None)
    node2 = TreeNode(2, None, None)
    root.right = node2

    pre_order_traversal(root, "")

    print(solution.getMinimumDifference(root))

    root = TreeNode(5, None, None)
    node4 = TreeNode(4, None, None)
    node7 = TreeNode(7, None, None)
    root.left = node4
    root.right = node7

    pre_order_traversal(root, "")

    print(solution.getMinimumDifference(root))

    root = TreeNode(236, None, None)
    node4 = TreeNode(104, None, None)
    node1 = TreeNode(701, None, None)
    root.left = node4
    root.right = node1

    node7 = TreeNode(227, None, None)
    node4.right = node7
    node11 = TreeNode(911, None, None)
    node1.right = node11

    pre_order_traversal(root, "")

    print(solution.getMinimumDifference(root))


    root = TreeNode(1564, None, None)
    node34 = TreeNode(1434, None, None)
    node1 = TreeNode(1, None, None)
    root.left = node34
    node34.left = node1

    node48 = TreeNode(3048, None, None)
    root.right = node48
    node84 = TreeNode(3184, None, None)
    node48.right = node84

    pre_order_traversal(root, "")

    print(solution.getMinimumDifference(root))

    root = TreeNode(0, None, None)
    node36 = TreeNode(2236, None, None)
    root.right = node36

    node77 = TreeNode(1277, None, None)
    node36.left = node77
    node19 = TreeNode(519, None, None)
    node77.left = node19

    node76 = TreeNode(2776, None, None)
    node36.right = node76

    pre_order_traversal(root, "")

    print(solution.getMinimumDifference(root))

test()
