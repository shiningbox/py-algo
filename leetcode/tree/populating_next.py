from typing import List
from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# Print the tree
def pre_order_traversal(node: Node, indent):
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

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return root

        stack = [(root, 0)]
        p_h = Node(-1)
        prev = (p_h, 0)
        while stack:
            head, depth = stack.pop(0)

            if head.left:
                stack.append((head.left, depth + 1))

            if head.right:
                stack.append((head.right, depth + 1))
            pre_node, pre_depth = prev[0], prev[1]
            if depth == pre_depth + 1:
                # add a None node
                n_node = Node(val="#")
                pre_node.next = n_node
                n_node.next = head
            else:
                pre_node.next = head

            prev = (head, depth)
        n_node = Node(val="#")
        head.next = n_node
        n_node.next = None
        return p_h.next


def print_linked_list(node):
    while node:
        print(node.val, end=",")
        node = node.next
    print()

def test():
    solution = Solution()
    # test method
    root = Node(1, None, None)
    node2 = Node(2, None, None)
    root.left = node2
    node3 = Node(3, None, None)
    root.right = node3

    node4 = Node(4, None, None)
    node2.left = node4
    node5 = Node(5, None, None)
    node2.right = node5

    node6 = Node(6, None, None)
    node3.left = node6
    node7 = Node(7, None, None)
    node3.right = node7

    pre_order_traversal(root, "")
    node = solution.connect(root)
    print_linked_list(node)



test()
