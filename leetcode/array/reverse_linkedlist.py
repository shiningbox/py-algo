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
    pass


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
    new_head = solution.removeElements(node1, 6)
    print_list(new_head)
    new_head = solution.removeElements(node21, 6)
    print_list(new_head)


test()
