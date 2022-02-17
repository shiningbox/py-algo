from typing import List
from typing import Optional

# Definition for a binary tree node.
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

    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        # O(logn)
        max_depth = self.max_depth(root)

        if max_depth == 0:
            return 1

        non_leaves = 2 ** max_depth - 1
        # Now try to get the number of leaves
        stack = [(root, 0)]
        leaves_count = 0
        while stack:
            top, depth = stack.pop()

            if depth < max_depth - 1:
                # continue dfs
                stack.append((top.right, depth + 1))
                stack.append((top.left, depth + 1))
            elif depth == max_depth - 1:
                if top.left:
                    leaves_count += 1
                if top.right:
                    leaves_count += 1
                continue
            else:
                break

        return leaves_count + non_leaves

    def max_depth(self, node: TreeNode):

        # Leaf node
        if not node.left and not node.right:
            return 0

        return self.max_depth(node.left) + 1



def test():
    solution = Solution()
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


    node6 = TreeNode(6, None, None)
    node3.left = node6

    pre_order_traversal(root, "")
    print(solution.countNodes(root))


test()
