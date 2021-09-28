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

    def check_equal(self, head1, head2):
        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        return True

    # O(n) time and O(1) space
    # Use the chase pattern
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find middle point using chase pattern
        fast = slow = head
        # When fast reaches the end
        # slow should only reaches to the half
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # Then reverse the second half, from rev to head
        r_head = self.reverse_list(slow)
        return self.check_equal(head, r_head)

def test():
    solution = Solution()
    head = ListNode(1)
    print(solution.isPalindrome(head))

    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(1)
    head.next = node2
    node2.next = node3
    node3.next = node4
    print(solution.isPalindrome(head))

    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node5 = ListNode(1)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(solution.isPalindrome(head))

    head = ListNode(1)
    node2 = ListNode(2)
    head.next = node2
    print(solution.isPalindrome(head))


    # test method


test()
