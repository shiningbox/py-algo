from typing import List
from typing import Optional



# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

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

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        paths = [None, None]
        stack = [(root, [root])]
        while stack:

            if paths[0] and paths[1]:
                break

            top, path = stack.pop()

            if top.val == p.val:
                paths[0] = path

            if top.val == q.val:
                paths[1] = path

            if top.right:
                stack.append((top.right, path + [top.right]))
            if top.left:
                stack.append((top.left, path + [top.left]))

        res = None
        path_p = paths[0]
        path_q = paths[1]
        idx = 0
        while idx < len(path_p) and idx < len(path_q):
            if path_p[idx] == path_q[idx]:
                res = path_p[idx]
            else:
                break
            idx += 1

        return res

def test():
    solution = Solution()
    # test method
    root1 = TreeNode(6, None, None)
    node11 = TreeNode(2, None, None)
    root1.left = node11
    node12 = TreeNode(8, None, None)
    root1.right = node12
    node21 = TreeNode(0, None, None)
    node11.left = node21
    node22 = TreeNode(4, None, None)
    node11.right = node22
    node31 = TreeNode(3, None, None)
    node22.left = node31
    node32 = TreeNode(5, None, None)
    node22.right = node32

    node23 = TreeNode(7, None, None)
    node12.left = node23
    node24 = TreeNode(9, None, None)
    node12.right = node24

    pre_order_traversal(root1, "-")
    print(solution.lowestCommonAncestor(root1, node21, node32))

test()
