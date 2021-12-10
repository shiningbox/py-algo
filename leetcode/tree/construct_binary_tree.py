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
        self.indices_dict = {}
        self.pre_array = []
        self.in_array = []
        self.current_index = 0

    def get_left_right(self, pre_index):
        left = []
        right = []
        root_index = self.indices_dict[self.pre_array[pre_index]]
        i = root_index - 1
        self.in_array[root_index] = None
        while i >= 0 and self.in_array[i]:
            left.append(self.in_array[i])
            i -= 1
        j = root_index + 1
        while j < len(self.in_array) and self.in_array[j]:
            right.append(self.in_array[j])
            j += 1
        return left, right

    def build_binary_tree(self, index):

        if index >= len(self.pre_array):
            return None, index

        root_val = self.pre_array[index]
        root = TreeNode(root_val)
        left, right = self.get_left_right(index)

        if not left and not right:
            return root, index

        left_root = right_root = None
        if left:
            left_root, index = self.build_binary_tree(index + 1)
        if right:
            right_root, index = self.build_binary_tree(index + 1)
        root.left = left_root
        root.right = right_root
        return root, index

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.indices_dict = {}
        self.pre_array = preorder
        self.in_array = inorder

        for i in range(len(inorder)):
            self.indices_dict[inorder[i]] = i
        root, index = self.build_binary_tree(0)
        return root

def test():
    solution = Solution()
    # test method
    root = solution.buildTree([3,9,20,15,7], [9,3,15,20,7])
    pre_order_traversal(root, "")
    root = solution.buildTree([1, 2], [1, 2])
    pre_order_traversal(root, "")
test()
