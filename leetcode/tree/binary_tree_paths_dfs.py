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


def dfs(node):
    res = []
    if not node:
        return res

    stack = [node]

    while stack:
        top = stack.pop()

        if not top:
            continue
        res.append(top)
        stack.append(top.right)
        stack.append(top.left)

    return res


def bfs(node):
    res = []
    if not node:
        return res

    stack = [node]

    while stack:
        top = stack.pop(0)

        if not top:
            continue
        res.append(top)
        stack.append(top.left)
        stack.append(top.right)

    return res

def dfs_recursion(node, res):
    if not node:
        return

    res.append(node)
    dfs_recursion(node.left, res)
    dfs_recursion(node.right, res)


def bfs_recursion(node, res):
    if not node:
        return

    res.append(node)
    dfs_recursion(node.left, res)
    dfs_recursion(node.right, res)


class Solution:

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.right:
                stack.append((node.right, ls + str(node.val) + "->"))
            if node.left:
                stack.append((node.left, ls + str(node.val) + "->"))
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

    root2 = TreeNode(0, None, None)

    #print(solution.binaryTreePaths(root1))
    #print(solution.binaryTreePaths(root2))
    pre_order_traversal(root1, "")
    res = dfs(root1)
    for node in res:
        print(node.val, end="-")
    res = []
    print(" ")
    dfs_recursion(root1, res)
    for node in res:
        print(node.val, end="-")
    print(" ")
    res = bfs(root1)
    for node in res:
        print(node.val, end="-")
    print(" ")




test()
