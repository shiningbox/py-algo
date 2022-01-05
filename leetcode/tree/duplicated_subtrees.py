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

    res = []
    visited = set()

    def check_tree(self, root1, root2):
        if not root1 and not root2:
            return True
        elif root1 and not root2 or root2 and not root1:
            return False
        if root1.val != root2.val:
            return False
        return self.check_tree(root1.left, root2.left) and self.check_tree(root1.right, root2.right)

    def is_same_subtree(self, t, s):

        roots = []
        stack = [t]

        while stack:
            node = stack.pop()

            if not node:
                continue

            if node != s and node.val == s.val and self.check_tree(node, s):
                if node not in self.visited and s not in self.visited:
                    self.res.append(s)
                    self.visited.add(node)
                    self.visited.add(s)

            stack.append(node.right)
            stack.append(node.left)


    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.res = []

        # DFS from the root
        stack = [root]
        while stack:
            top = stack.pop()
            if not top:
                continue
            # If this sub root has already been visited
            if top not in self.visited and self.is_same_subtree(root, top):
                self.res.append(top.val)
            stack.append(top.right)
            stack.append(top.left)

        return self.res


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
