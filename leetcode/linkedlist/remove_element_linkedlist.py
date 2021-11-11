from typing import List
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(node):
    while node is not None:
        print(node.val)
        node = node.next

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
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(6)
    node4 = ListNode(3)
    node5 = ListNode(4)
    node6 = ListNode(5)
    node7 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    node21 = ListNode(6)
    node22 = ListNode(1)
    node21.next = node22

    solution = Solution()
    # test method
    new_head = solution.reverseList(node1)
    print_list(new_head)
    #new_head = solution.reverseList(node2)
    #print_list(new_head)


test()


