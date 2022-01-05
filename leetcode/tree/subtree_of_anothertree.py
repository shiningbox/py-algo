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

    def check_tree(self, root1, root2):
        if not root1 and not root2:
            return True
        elif root1 and not root2 or root2 and not root1:
            return False

        if root1.val != root2.val:
            return False

        return self.check_tree(root1.left, root2.left) and self.check_tree(root1.right, root2.right)

    def dfs(self, t, s):

        if not t:
            return False

        stack = [t]
        while stack:

            top = stack.pop()

            if not top:
                continue

            if top.val == s.val and self.check_tree(top, s):
                return True

            stack.append(top.right)
            stack.append(top.left)

        return False

    def isSubtree(self, t, s):
        if not s:
            return True

        return self.dfs(t, s)

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

    sub_root = node4

    print(solution.isSubtree(root, sub_root))

    sub_root2 = TreeNode(3, None, None)
    node6 = TreeNode(6, None, None)
    sub_root2.left = node6

    node5 = TreeNode(5, None, None)
    sub_root2.right = node5

    node9 = TreeNode(9, None, None)
    node5.right = node9

    print(solution.isSubtree(root, sub_root2))

    root = TreeNode(1, None, None)
    node1 = TreeNode(1, None, None)
    root.left = node1

    sub_root3 = TreeNode(1, None, None)

    print(solution.isSubtree(root, sub_root3))

    root3 = TreeNode(4, None, None)
    node1 = TreeNode(1, None, None)
    root3.left = node1
    node11 = TreeNode(1, None, None)
    node1.left = node11

    node6 = TreeNode(6, None, None)
    node7 = TreeNode(7, None, None)

    node11.left = node6
    node11.right = node7

    sub_root4 = TreeNode(4, None, None)
    node1 = TreeNode(1, None, None)
    sub_root4.left = node1
    node6 = TreeNode(6, None, None)
    node7 = TreeNode(7, None, None)
    node1.left = node6
    node1.right = node7

    print(solution.isSubtree(root3, sub_root4))


test()
