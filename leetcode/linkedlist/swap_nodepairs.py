from typing import List
from typing import Optional

class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        mock_head = ListNode(-1)
        mock_head.next = head
        p = mock_head
        c = p.next
        if c:
            n = c.next
        else:
            n = None
        # p    c    n
        # p -> 1 -> 2 -> e
        # p -> 2,  1 -> e
        # p -> 2,  1 -> e
        #      n    c
        # p -> 2 -> 1 -> e
        while n:
            p.next = n
            c.next = n.next
            n.next = c
            p = p.next.next
            c = p.next
            if c:
                n = c.next
            else:
                break

        return mock_head.next


def print_list(node):
    while node is not None:
        print(node.val, end="->")
        node = node.next
    print("")

def test():
    solution = Solution()
    head = ListNode(1)
    node2 = ListNode(2)
    head.next = node2
    node0 = ListNode(3)
    node2.next = node0
    nodem4 = ListNode(4)
    node0.next = nodem4

    solution.swapPairs(head)
    print(solution.swapPairs(None))
    print(solution.swapPairs([]))


test()

