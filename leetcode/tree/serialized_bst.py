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


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""

        stack = [root]
        res = ""
        while stack:
            top = stack.pop(0)

            if not top:
                res += "n"
                continue
            else:
                res += str(top.val)
            if top.left or top.right:
                stack.append(top.left)
                stack.append(top.right)

        return res

    def deserialize(self, data: str) -> Optional[TreeNode]:

        """Decodes your encoded data to tree.
        """
        if not data:
            return None

        def build_bst(i):

            if i >= len(char_array):
                return None

            if char_array[i] == 'n':
                return None

            root = TreeNode(char_array[i])
            root.left = build_bst(2 * i + 1)
            root.right = build_bst(2 * i + 2)
            return root

        char_array = list(data)

        return build_bst(0)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans


def test():
    # test method
    root = TreeNode(3, None, None)
    node2 = TreeNode(2, None, None)
    root.left = node2
    node5 = TreeNode(5, None, None)
    root.right = node5

    node1 = TreeNode(1, None, None)
    node2.left = node1

    node4 = TreeNode(4, None, None)
    node5.left = node4

    node6 = TreeNode(6, None, None)
    node5.right = node6

    ser = Codec()
    deser = Codec()
    tree = ser.serialize(root)
    print(tree)
    pre_order_traversal(deser.deserialize(tree), "")

test()
