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
    # Reverse list
    def reverse_list(self, head):
        node = head
        rh = None
        while node:
            temp = node.next
            node.next = rh
            rh = node
            node = temp
        return rh


def test():

    solution = Solution()

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

    r_head = solution.reverse_list(node1)
    print_list(r_head)


test()
