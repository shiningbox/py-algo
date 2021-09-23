from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    class Solution:

        def swap_root(self, p, q):
            stack = [(p, q)]

            while stack and len(stack) > 0:
                # Process node
                node1, node2 = stack.pop()
                # swap
                temp = node1
                node1 = node2
                node2 = temp
                if not node1 and not node2:
                    continue
                elif None in [node1, node2]:
                    return False
                else:
                    if node1.val != node2.val:
                        return False
                    else:
                        # Continue with next level nodes
                        stack.append([node1.right, node2.left])
                        stack.append([node1.left, node2.right])

        def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
            self.swap_root(root.left, root.right)
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
    root = TreeNode(3, None, None)
    node11 = TreeNode(9, None, None)
    root.left = node11
    node12 = TreeNode(20, None, None)
    root.right = node12
    node21 = TreeNode(15, None, None)
    node12.left = node21
    node22 = TreeNode(7, None, None)
    node12.right = node22
    pre_order_traversal(root, "")

    root2 = TreeNode(1, None, None)
    node11 = TreeNode(2, None, None)
    root2.left = node11
    node12 = TreeNode(2, None, None)
    root2.right = node12
    node21 = TreeNode(3, None, None)
    node11.left = node21
    node22 = TreeNode(3, None, None)
    node11.right = node22
    node31 = TreeNode(4, None, None)
    node32 = TreeNode(4, None, None)
    node21.left = node31
    node21.right = node32
    pre_order_traversal(root2, "")

    solution.invertTree(root)
    pre_order_traversal(root, "")

    solution.invertTree(root2)
    pre_order_traversal(root2, "")


test()
