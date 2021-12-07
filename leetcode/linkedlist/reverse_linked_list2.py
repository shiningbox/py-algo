from typing import List
from typing import Optional

class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:


    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        dh = ListNode(-1)
        dh.next = head
        dt = head
        while dt and i <= right:
            if i < left:
                dh = dh.next
            dt = dt.next
            i += 1
        n_head = dh.next
        prev = None
        while n_head != dt:
            curr = n_head
            n_head = n_head.next
            curr.next = prev
            prev = curr

        dh.next.next = dt
        dh.next = prev
        if left <= 1:
            return dh.next
        else:
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


    print_list(solution.reverseBetween(head, 2, 4))

    # print(solution.method(node))
    head = ListNode(3)
    node = ListNode(5)
    head.next = node
    print_list(solution.reverseBetween(head, 1, 2))

    head = ListNode(1)
    node1 = ListNode(2)
    head.next = node1
    node2 = ListNode(3)
    node1.next = node2
    print_list(solution.reverseBetween(head, 1, 2))

test()

