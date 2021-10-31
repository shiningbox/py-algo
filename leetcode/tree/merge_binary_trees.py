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

    def mergeTrees_recursive(self, t1, t2):

        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2


    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root1:
            return root2
        if not root2:
            return root1

        queue = [(None, None, root1, root2)]

        while queue:

            head = queue.pop(0)
            parent_left = head[0]
            parent_right = head[1]
            node1 = head[2]
            node2 = head[3]

            if not node1 and not node2:
                continue

            if node1 and node2:
                node1.val = node1.val + node2.val
            elif not node1 and node2:
                node1 = TreeNode(node2.val, None, None)
                if parent_left and parent_right:
                    if node2 == parent_right.right:
                        parent_left.right = node1
                    else:
                        parent_left.left = node1

            if node2:
                queue.append((node1, node2, node1.right, node2.right))
                queue.append((node1, node2, node1.left, node2.left))
            else:
                queue.append((node1, node2, node1.right, None))
                queue.append((node1, node2, node1.left, None))

        return root1


def test():
    solution = Solution()
    # test method
    root = TreeNode(1, None, None)
    node3 = TreeNode(3, None, None)
    root.left = node3
    node2 = TreeNode(2, None, None)
    root.right = node2

    node5 = TreeNode(5, None, None)
    node3.left = node5

    root2 = TreeNode(2, None, None)
    node1 = TreeNode(1, None, None)
    root2.left = node1
    node3 = TreeNode(3, None, None)
    root2.right = node3

    node4 = TreeNode(4, None, None)
    node1.right = node4

    node7 = TreeNode(7, None, None)
    node3.right = node7

    #pre_order_traversal(root, "")
    #pre_order_traversal(root2, "")

    root = solution.mergeTrees(root, root2)
    pre_order_traversal(root, "")

    root = None
    root2 = TreeNode(1, None, None)
    root = solution.mergeTrees(root, root2)
    pre_order_traversal(root, "")

test()
