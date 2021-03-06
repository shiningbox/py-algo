from typing import List
from typing import Optional


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

def test():
    solution = Solution()
    res = solution.generateTrees(1)
    print(len(res))
    for root in res:
        pre_order_traversal(root, "")
    # test method
    res = solution.generateTrees(3)
    print(len(res))
    for root in res:
        pre_order_traversal(root, "")

    res = solution.generateTrees(4)
    print(len(res))
    for root in res:
        pre_order_traversal(root, "")

test()
