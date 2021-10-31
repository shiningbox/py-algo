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

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = {}
        level = 0
        queue = [(level, root)]

        while queue:
            head = queue.pop(0)
            if head[0] not in levels:
                levels[head[0]] = [head[1].val]
            else:
                levels[head[0]].append(head[1].val)

            if head[1].right:
                queue.append((head[0] + 1, head[1].right))
            if head[1].left:
                queue.append((head[0] + 1, head[1].left))

        print(levels)

        return [sum(val_list) / len(val_list) for val_list in levels.values()]


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

    print(solution.averageOfLevels(root))

    root = TreeNode(3, None, None)
    node1 = TreeNode(1, None, None)
    root.left = node1
    node5 = TreeNode(5, None, None)
    root.right = node5

    node0 = TreeNode(0, None, None)
    node1.left = node0
    node2 = TreeNode(2, None, None)
    node1.right = node2

    node4 = TreeNode(4, None, None)
    node5.left = node4
    node6 = TreeNode(6, None, None)
    node5.right = node6

    print(solution.averageOfLevels(root))

test()
