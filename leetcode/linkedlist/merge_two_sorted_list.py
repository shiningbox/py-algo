from typing import List
from typing import Optional

class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

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


def print_list(node):
    while node is not None:
        print(node.val)
        node = node.next

def test():
    solution = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node4 = ListNode(4)
    node2.next = node4
    node22 = ListNode(2)
    node23 = ListNode(3)
    node22.next = node23
    node24 = ListNode(4)
    node23.next = node24
    # test method
    res_node = solution.mergeTwoLists(node1, node22)
    print_list(res_node)
    res_node = solution.mergeTwoLists(None, node22)
    print_list(res_node)
    res_node = solution.mergeTwoLists(None, None)
    print_list(res_node)
    res_node = solution.mergeTwoLists(node24, None)
    print_list(res_node)


test()
