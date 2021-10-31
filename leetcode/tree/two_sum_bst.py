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

    def binary_search(self, root: Optional[TreeNode], node, k) -> bool:
        if not root:
            return False
        if root.val == k and root != node:
            return True
        return self.binary_search(root.left, node, k) or self.binary_search(root.right, node, k)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue = [root]
        result = False
        while queue and not result:
            head = queue.pop(0)
            result = self.binary_search(root, head, k - head.val)
            if head.left:
                queue.append(head.left)
            if head.right:
                queue.append(head.right)

        return result

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

    print(solution.findTarget(root, 9))
    print(solution.findTarget(root, 6))
    print(solution.findTarget(root, 4))

test()
