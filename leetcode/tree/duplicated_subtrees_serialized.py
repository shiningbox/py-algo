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

    def findDuplicateSubtrees(self, root):

        # Serialize a tree to a string
        # and save each serialized sub-tree into a dictionary, with value to be a list
        # if value is larger than
        def serialize_tree(root):
            if not root:
                return "NA"
            struct = f"{str(root.val)}, {serialize_tree(root.left)}, {serialize_tree(root.right)}"
            if struct in nodes:
                nodes[struct].append(root)
            else:
                nodes[struct] = [root]
            return struct

        nodes = {}
        serialize_tree(root)

        return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]


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

    pre_order_traversal(root, "")

    print(solution.findDuplicateSubtrees(root))

test()
