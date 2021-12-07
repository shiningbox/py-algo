from typing import List
from typing import Optional

class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverse(self, node, d_head, d_tail):

        if not node.next:
            d_tail.next = node
            return node

        last_node = self.reverse(node.next, d_head, d_tail)
        last_node.next = node
        if d_head.next == last_node:
            last_node.next = None

        return node

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d_tail = ListNode(-1)
        d_head = ListNode(-1)
        d_head.next = head
        self.reverse(d_head, d_head, d_tail)
        if d_tail.next != d_head:
            return d_tail.next
        else:
            return None


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

    print(solution.getIntersectionNode(head))

    # print(solution.method(node))


test()

