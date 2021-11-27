from typing import List
from typing import Optional

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def generate_parentesis_tree(self, level):
        root = TreeNode("(")
        i = 1
        parents = [root]
        while i < level * 2:
            new_parents = []
            for parent in parents:
                parent.left = TreeNode("(")
                parent.right = TreeNode(")")
                new_parents.append(parent.left)
                new_parents.append(parent.right)
            parents = new_parents
            i += 1
        return root

    def find_path(self, node, left, right, res, ls):

        # if left < right:
        # ()), can never be a valid result
        if right < left:
            return

        if not left and not right:
            s = ls + node.val
            res.append(s)
            return

        if node.left:
            self.find_path(node.left, left - 1, right, res, ls + node.val)
        if node.right:
            self.find_path(node.right, left, right - 1, res, ls + node.val)

    def generateParenthesis(self, n: int) -> List[str]:
        root = self.generate_parentesis_tree(n)
        res = []
        self.find_path(root, n - 1, n, res, "")
        return res

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
    print(solution.generateParenthesis(3))

test()
