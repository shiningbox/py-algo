from typing import List
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def build_bt(self, low, high, nums):

        if low > high:
            return
        mid = (low + high) // 2
        root = TreeNode(nums[mid])

        # Build left subtree
        left_sub = self.build_bt(low, mid - 1, nums)
        # Build right subtree
        right_sub = self.build_bt(mid + 1, high, nums)
        root.left = left_sub
        root.right = right_sub
        return root

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        return self.build_bt(0, len(nums) - 1, nums)


def print_list(node):
    while node is not None:
        print(node.val, end="->")
        node = node.next
    print()

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
    # test method
    head = ListNode(-10)
    node1 = ListNode(-3)
    head.next = node1
    node2 = ListNode(0)
    node1.next = node2
    node3 = ListNode(5)
    node2.next = node3
    node4 = ListNode(9)
    node3.next = node4
    root = solution.sortedListToBST(head)
    pre_order_traversal(root, "")


test()
