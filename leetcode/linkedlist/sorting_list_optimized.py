from typing import List
from typing import Optional

class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    def divide(self, h1):
        slow = fast = h1
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        nh = slow.next
        slow.next = None
        return slow, nh

    def merge(self, l1, l2):
        n_h = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return n_h.next

    def merge_sort(self, head):

        if not head:
            return None

        # Single node
        if not head.next:
            return head

        # divide
        mid, nh = self.divide(head)

        # sort first half
        h1 = self.merge_sort(head)
        # sort second half
        h2 = self.merge_sort(nh)

        return self.merge(h1, h2)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.merge_sort(head)


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

