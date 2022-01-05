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

    x_node = []
    y_node = []

    def pre_order_traversal(self, parent, node: TreeNode, depth, x, y):

        # Root
        if node:
            if node.val == x:
                self.x_node.append(parent)
                self.x_node.append(depth)
            if node.val == y:
                self.y_node.append(parent)
                self.y_node.append(depth)
        else:
            return

        depth += 1
        # Left
        self.pre_order_traversal(node, node.left, depth, x, y)
        # Right
        self.pre_order_traversal(node, node.right, depth, x, y)

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.x_node = []
        self.y_node = []
        self.pre_order_traversal(None, root, 0, x, y)
        return self.x_node[0] != self.y_node[0] and self.x_node[1] == self.y_node[1]


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

    print(solution.isCousins(root, 1, 9))

    root = TreeNode(1, None, None)
    node2 = TreeNode(2, None, None)
    root.left = node2
    node3 = TreeNode(3, None, None)
    root.right = node3

    node4 = TreeNode(4, None, None)
    node2.right = node4

    node5 = TreeNode(5, None, None)
    node3.right = node5

    # pre_order_traversal(root, "")

    print(solution.isCousins(root, 4, 5))

    root = TreeNode(1, None, None)
    node2 = TreeNode(2, None, None)
    root.left = node2
    node3 = TreeNode(3, None, None)
    root.right = node3

    node4 = TreeNode(4, None, None)
    node2.right = node4


    # pre_order_traversal(root, "")
    print(solution.isCousins(root, 2, 3))

test()
