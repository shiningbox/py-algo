from typing import List
from typing import Optional

class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    # Reverse linkedlist
    def reverse_list(self, head):
        node = head
        rh = None
        while node:
            temp = node.next
            node.next = rh
            rh = node
            node = temp
        return rh

    def add_vals(self, val1, val2, carry):
        sum = val1 + val2 + carry
        if sum >= 10:
            carry = 1
            sum -= 10
        else:
            carry = 0
        return sum, carry

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        last = None
        carry = 0
        while l1 and l2:
            last = l1
            sum, carry = self.add_vals(l1.val, l2.val, carry)
            l1.val = sum
            l1 = l1.next
            l2 = l2.next

        if l2:
            last.next = l2
            while l2:
                last = l2
                sum, carry = self.add_vals(l2.val, 0, carry)
                l2.val = sum
                l2 = l2.next
        else:
            last.next = l1
            while l1:
                last = l1
                sum, carry = self.add_vals(l1.val, 0, carry)
                l1.val = sum
                l1 = l1.next

        if not l1 and not l2:
            if carry == 1:
                last.next = ListNode(1)

        return head

def print_list(node):
    while node is not None:
        print(node.val, end="")
        node = node.next
    print(" ")


def test():
    solution = Solution()
    head = ListNode(6)
    node2 = ListNode(1)
    head.next = node2
    node0 = ListNode(3)
    node2.next = node0

    head2 = ListNode(4)
    node0 = ListNode(5)
    head2.next = node0
    nodem4 = ListNode(7)
    node0.next = nodem4
    node8 = ListNode(8)
    nodem4.next = node8

    print_list(solution.addTwoNumbers(head, head2))

    head = ListNode(9)
    node1 = ListNode(9)
    head.next = node1
    node2 = ListNode(9)
    node1.next = node2
    node3 = ListNode(9)
    node2.next = node3

    head2 = ListNode(9)
    node1 = ListNode(9)
    head2.next = node1

    print_list(solution.addTwoNumbers(head, head2))

test()

