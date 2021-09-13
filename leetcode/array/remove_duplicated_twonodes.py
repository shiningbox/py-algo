from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        if head.next is None:
            return head

        u_node = head
        node = u_node.next
        while node is not None:
            if node.val != u_node.val:
                u_node = node
                node = node.next
            else:
                while node is not None and node.val == u_node.val:
                    node = node.next
                u_node.next = node
        return head


    def print_list(self, node: ListNode):
        while node is not None:
            print(node.val)
            node = node.next

def test():
    solution = Solution()

    node0 = ListNode(1, None)

    # test method
    node1 = ListNode(1, None)
    node2 = ListNode(1, None)
    node1.next = node2
    node3 = ListNode(2, None)
    node2.next = node3
    node4 = ListNode(2, None)
    node3.next = node4

    node21 = ListNode(1, None)
    node22 = ListNode(1, None)
    node21.next = node22

    node31 = ListNode(1, None)
    node32 = ListNode(2, None)
    node31.next = node32
    node33 = ListNode(3, None)
    node32.next = node33

    solution.print_list(solution.deleteDuplicates(None))
    solution.print_list(solution.deleteDuplicates(node0))
    solution.print_list(solution.deleteDuplicates(node1))
    solution.print_list(solution.deleteDuplicates(node21))
    solution.print_list(solution.deleteDuplicates(node31))


test()
