from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def dfs_stack(self, root: TreeNode):

        if root is None:
            print(" ")

        stack = []
        stack.append(root)
        # dfs stack contains unprocessed nodes
        while stack is not None and len(stack) > 0:
            # pop and process the top
            top = stack.pop()

            if top.val is not None:
                print(top.val)

            # Push its next level nodes to stack
            # Push the right child of top to stack
            if top.right is not None:
                stack.append(top.right)
            # Push the left child to stack as the current top
            if top.left is not None:
                stack.append(top.left)

    def bfs_queue(self, root: TreeNode):

        if root is None:
            print(" ")

        queue = []
        queue.append(root)
        while queue is not None and len(queue) > 0:
            header = queue.pop(0)
            print(header.val)
            if header.left is not None:
                queue.append(header.left)
            if header.right is not None:
                queue.append(header.right)

    # DFS with stack
    # BFS with queue
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        # DFS p and q together
        while stack and len(stack) > 0:

            # Pop and process top
            node0, node1 = stack.pop()

            # If all nodes are None, i.e., empty roots or empty children
            # Continue with next pop
            if node0 is None and node1 is None:
                continue
            # Python check if any of the element is None
            elif None in [node0, node1]:
                return False
            else:
                if node0.val != node1.val:
                    return False
                else:
                    # Push next level nodes for pop and processing
                    stack.append((node0.right, node1.right))
                    stack.append((node0.left, node1.left))

        return True

def test():
    solution = Solution()
    # test method
    root1 = TreeNode(1, None, None)
    node2 = TreeNode(2, None, None)
    root1.right = node2
    node3 = TreeNode(3, None, None)
    node2.left = node3
    node4 = TreeNode(4, None, None)
    node2.right = node4
    node5 = TreeNode(5, None, None)
    node4.left = node5

    root2 = TreeNode(1, None, None)
    node2 = TreeNode(2, None, None)
    root2.right = node2
    node3 = TreeNode(3, None, None)
    node2.left = node3
    node4 = TreeNode(4, None, None)
    node2.right = node4
    node5 = TreeNode(5, None, None)
    node4.left = node5

    root3 = TreeNode(1, None, None)
    node2 = TreeNode(2, None, None)
    root3.right = node2

    print(solution.isSameTree(root1, root2))
    print(solution.isSameTree(root1, root3))
    print(solution.isSameTree(root2, root3))
    print(solution.isSameTree(None, None))

    #solution.dfs_stack(node1)
    #solution.bfs_queue(node1)


test()
