from typing import List
from typing import Optional

class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # End of recursion
        if l1 is None and l2 is None:
            return None

        if l1 is None and l2 is not None:
            return l2

        if l2 is None and l1 is not None:
            return l1

        ## General cases
        # Compare node value and merge
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1.next
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2.next


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
    #print_list(res_node)
    res_node = solution.mergeTwoLists(None, None)
    #print_list(res_node)
    res_node = solution.mergeTwoLists(node24, None)
    #print_list(res_node)


test()
