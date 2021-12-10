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

    def __init__(self):
        self.depth_dict = {}

    def pre_order_traversal(self, node: TreeNode, depth):
        # Root
        if node:
            if depth not in self.depth_dict:
                self.depth_dict[depth] = [node.val]
            else:
                if depth % 2 == 0:
                    self.depth_dict[depth].append(node.val)
                else:
                    self.depth_dict[depth].insert(0, node.val)
        else:
            return

        self.pre_order_traversal(node.left, depth + 1)
        self.pre_order_traversal(node.right, depth + 1)


    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.depth_dict = {}
        self.pre_order_traversal(root, 0)
        return list(self.depth_dict.values())

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

    #pre_order_traversal(root, "")

    print(solution.zigzagLevelOrder(root))

test()
