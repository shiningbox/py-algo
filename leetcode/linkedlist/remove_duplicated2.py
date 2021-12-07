from typing import List
from typing import Optional

class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake_head = ListNode(-101)
        fake_head.next = head
        prev = fake_head
        current = prev.next
        if current:
            next = current.next
        else:
            return None
        while current:
            found = False
            while next and next.val == current.val:
                    found = True
                    current = next
                    next = current.next

            if found:
                prev.next = next
                found = False
            else:
                prev = current

            current = next
            if current:
                next = current.next

        return fake_head.next


def print_list(node):
    while node is not None:
        print(node.val, end="->")
        node = node.next
    print()

def test():
    solution = Solution()
    head = ListNode(3)
    node2 = ListNode(2)
    head.next = node2
    node0 = ListNode(2)
    node2.next = node0
    nodem4 = ListNode(-4)
    node0.next = nodem4
    node5 = ListNode(5)
    nodem4.next = node5

    print_list(solution.deleteDuplicates(None))


    print_list(solution.deleteDuplicates(head))

    head = ListNode(3)

    print_list(solution.deleteDuplicates(head))

    head = ListNode(3)
    node2 = ListNode(3)
    head.next = node2

    print_list(solution.deleteDuplicates(head))


test()

