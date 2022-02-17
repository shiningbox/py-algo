from typing import List
from typing import Optional

class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:

        idx = mid = 0

        fast = slow = head
        stack = []
        while slow.next and fast.next and fast.next.next:
            mid += 1
            slow = slow.next
            fast = fast.next.next
        node = tail = head
        while idx < mid:
            node = node.next
            tail = node
            idx += 1
        while node.next:
            stack.append(node.next)
            node = node.next
        tail.next = None

        # Start reordring
        node = head
        while stack:
            top = stack.pop()
            print_list(head)

            top.next = node.next
            node.next = top
            node = top.next
        return head

def print_list(node):
    while node is not None:
        print(node.val, end="->")
        node = node.next
    print()


def test():
    solution = Solution()
    head = ListNode(1)
    node2 = ListNode(2)
    head.next = node2
    node0 = ListNode(3)
    node2.next = node0
    nodem4 = ListNode(4)
    node0.next = nodem4
    node5 = ListNode(5)
    nodem4.next = node5

    head = solution.reorderList(head)
    print_list(head)



test()

