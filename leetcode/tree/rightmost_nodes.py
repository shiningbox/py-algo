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

    def right_views(self, root, path, res):

        if not root:
            return

        if not path or sum(path) == len(path):
            res.append(root.val)

        self.right_views(root.left, path + [0], res)
        self.right_views(root.right, path + [1], res)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.right_views(root, [], res)
        return res

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

    pre_order_traversal(root, "")

    #print(solution.rightSideView(root))

    root = TreeNode(1, None, None)
    node2 = TreeNode(2, None, None)
    root.left = node2
    print(solution.rightSideView(root))


test()
