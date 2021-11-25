from typing import List
from typing import Optional

class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:

    def get_len(self, head):
        len = 0
        if not head:
            return len
        else:
            while head:
                head = head.next
                len += 1
        return len

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_a, len_b = self.get_len(headA), self.get_len(headB)
        while len_a > len_b:
            headA = headA.next
            len_a -= 1
        while len_a < len_b:
            headB = headB.next
            len_b -= 1
        # Now the two linked lists have the same lengths
        while headA and headB and headA.val != headB.val:
            headA = headA.next
            headB = headB.next

        return headA

def print_list(node):
    while node is not None:
        print(node.val)
        node = node.next

def test():
    solution = Solution()
    head = ListNode(3)
    node2 = ListNode(2)
    head.next = node2
    node0 = ListNode(0)
    node2.next = node0
    nodem4 = ListNode(-4)
    node0.next = nodem4

    head2 = ListNode(3)
    node0 = ListNode(0)
    head2.next = node0
    nodem4 = ListNode(-4)
    node0.next = nodem4

    print(solution.get_len(head))
    print(solution.get_len(head2))

    print(solution.getIntersectionNode(head, head2))

    #print(solution.method(head))




test()
