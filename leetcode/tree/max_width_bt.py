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


class Solution(object):

    def calculate_width(self, path):
        if not path:
            return 0
        width = 0
        for i in range(len(path) - 1, -1, -1):
            if path[i] == '1':
                width += 2 ** (len(path) - 1 - i)
        return width


    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root.left and not root.right:
            return 1

        depth_dict = {}
        max_width = 1
        stack = [("", root, 0)]
        while stack:
            path, top, depth = stack.pop()
            if not top:
                continue

            if depth not in depth_dict:
                idx = self.calculate_width(path)
                depth_dict[depth] = (idx, idx)
            else:
                idx = self.calculate_width(path)
                left, right = depth_dict[depth]
                if idx < 2 ** (depth - 1) and idx < left:
                    depth_dict[depth] = (idx, right)
                else:
                    # right idx
                    if idx > right:
                        depth_dict[depth] = (left, idx)
                if depth_dict[depth][1] - depth_dict[depth][0] + 1 >= max_width:
                    max_width = depth_dict[depth][1] - depth_dict[depth][0] + 1

            stack.append((path + "1", top.right, depth + 1))
            stack.append((path + "0", top.left, depth + 1))
        return max_width

    def widthOfBinaryTree_dfs(self, root: Optional[TreeNode]) -> int:
        depth_dict = {}

        stack = [(root, 0)]

        while stack:
            top, depth = stack.pop()

            if depth not in depth_dict:
                depth_dict[depth] = 1
            else:
                depth_dict[depth] += 1

            if not top or not top.right and not top.left:
                continue

            stack.append((top.right, depth + 1))
            stack.append((top.left, depth + 1))

        return max(depth_dict.values())

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

    node2 = TreeNode(2, None, None)
    node3.left = node2
    node4 = TreeNode(4, None, None)
    node3.right = node4

    node4 = TreeNode(4, None, None)
    node2.left = node4

    print(solution.widthOfBinaryTree(root))

    #pre_order_traversal(root, "")

    root = TreeNode(1, None, None)
    node3 = TreeNode(3, None, None)
    root.left = node3
    node2 = TreeNode(2, None, None)
    root.right = node2

    node5 = TreeNode(5, None, None)
    node3.left = node5
    node6 = TreeNode(6, None, None)
    node5.left = node6

    node9 = TreeNode(9, None, None)
    node2.right = node9

    node7 = TreeNode(7, None, None)
    node9.right = node7

    pre_order_traversal(root, "")

    print(solution.widthOfBinaryTree(root))

test()
