from typing import List
from typing import Optional

class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if not head:
            return False

        chaser = head
        walker = head
        # If there is a cycle, chaser will catch walker eventually
        while walker.next and chaser.next.next:
            walker = walker.next
            chaser = chaser.next.next
            if walker == chaser:
                return True
        return False

def print_list(node):
    while node is not None:
        print(node.val)
        node = node.next

def test():
    solution = Solution()
    head = ListNode(3)
    node2 = ListNode(2)
    head.next = node2
    node3 = ListNode(0)
    node2.next = node3
    node4 = ListNode(-4)
    node3.next = node4
    print(solution.hasCycle(head))

    solution = Solution()
    head = ListNode(3)
    node2 = ListNode(2)
    head.next = node2
    node3 = ListNode(0)
    node2.next = node3
    node4 = ListNode(-4)
    node3.next = node4
    node4.next = node2
    print(solution.hasCycle(head))

    head = ListNode(1)
    node2 = ListNode(2)
    head.next = node2
    node2.next = head
    print(solution.hasCycle(head))




test()
