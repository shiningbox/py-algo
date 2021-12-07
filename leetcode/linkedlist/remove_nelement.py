from typing import List
from typing import Optional

class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    def list_length(self, node):
        length = 0
        while node:
            node = node.next
            length += 1
        return length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fake_head = ListNode(-1)
        fake_head.next = head
        length = self.list_length(fake_head)
        target_index = length - n
        i = 0
        node = fake_head
        while node and i < length - n - 1:
            node = node.next
            i += 1

        # Remove its next node
        node.next = node.next.next
        return fake_head.next


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

    print_list(solution.removeNthFromEnd(head, 4))

    # print(solution.method(node))


test()

