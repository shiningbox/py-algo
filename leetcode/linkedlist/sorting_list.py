from typing import List
from typing import Optional

class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    def divide(self, h1):
        slow = fast = h1
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        nh = slow.next
        slow.next = None
        node = nh
        while node:
            node = node.next
        return slow, nh, node

    def merge(self, l1, l2):
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        h = ListNode()
        n_node = h

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                new_node = ListNode(val=l1.val, next=None)
                n_node.next = new_node
                n_node = new_node
                l1 = l1.next
            else:
                new_node = ListNode(val=l2.val, next=None)
                n_node.next = new_node
                n_node = new_node
                l2 = l2.next

        while l1 is not None:
            new_node = ListNode(val=l1.val, next=None)
            n_node.next = new_node
            n_node = new_node
            l1 = l1.next

        while l2 is not None:
            new_node = ListNode(val=l2.val, next=None)
            n_node.next = new_node
            n_node = new_node
            l2 = l2.next

        return h.next

    def merge_sort(self, head, tail):

        if not head:
            return None

        # Single node
        if head == tail:
            return head

        # divide
        mid, nh, tail = self.divide(head)
        print_list_h(head)
        print_list_h(nh)

        # sort first half
        h1 = self.merge_sort(head, mid)
        # sort second half
        h2 = self.merge_sort(nh, tail)

        return self.merge(h1, h2)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.merge_sort(head, None)


def print_list(h, t):
    node = h.next
    while node != t:
        print(node.val, end="->")
        node = node.next
    print()

def print_list_h(h):
    node = h
    while node:
        print(node.val, end="->")
        node = node.next
    print()

def test():
    solution = Solution()
    head = ListNode(5)
    node2 = ListNode(3)
    head.next = node2
    node0 = ListNode(2)
    node2.next = node0
    nodem4 = ListNode(1)
    node0.next = nodem4
    node5 = ListNode(4)
    nodem4.next = node5

    #head = solution.sortList(head)
    #print_list_h(head)

    solution = Solution()
    head = ListNode(4)
    node1 = ListNode(3)
    head.next = node1
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(1)
    node2.next = node3
    head = solution.sortList(head)
    print_list_h(head)

test()

