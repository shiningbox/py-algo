from typing import List
from typing import Optional

class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pass


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

    print(solution.getIntersectionNode(head))

    # print(solution.method(head))


test()

