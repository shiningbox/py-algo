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

    def convert_binary_num(self, arr):
        sum = 0
        for i in range(len(arr) - 1, -1, -1):
            sum += arr[i] * (2 ** (len(arr) - i - 1))
        return sum

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        stack = [(root, [root.val])]
        all_nodes = []
        leaf_sum = 0
        while stack:

            top, pre_path = stack.pop()

            # end of a path
            if not top.left and not top.right:
                leaf_sum += self.convert_binary_num(pre_path)

            if top.right:
                right_path = [node for node in pre_path]
                right_path.append(top.right.val)
                stack.append((top.right, right_path))

            if top.left:
                left_path = [node for node in pre_path]
                left_path.append(top.left.val)
                stack.append((top.left, left_path))
        return leaf_sum

def test():
    solution = Solution()
    # test method
    root = TreeNode(1, None, None)
    node2 = TreeNode(0, None, None)
    root.left = node2
    node4 = TreeNode(1, None, None)
    root.right = node4

    node1 = TreeNode(1, None, None)
    node2.left = node1

    node3 = TreeNode(0, None, None)
    node4.left = node3
    node6 = TreeNode(1, None, None)
    node4.right = node6

    node5 = TreeNode(1, None, None)
    node6.left = node5

    node9 = TreeNode(0, None, None)
    node6.right = node9

    pre_order_traversal(root, "")

    print(solution.sumRootToLeaf(root))

test()
