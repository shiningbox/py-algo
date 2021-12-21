from typing import List
from typing import Optional

class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    """
        Consider the following linked list, where E is the cycle entry and X the crossing point of fast and slow.
        H: distance from head to cycle entry E
        D: distance from E to X
        L: cycle length
                          _____
                         /     \
        head_____H______E       \
                        \       /
                         X_____/


        If fast and slow both start at head, when fast catches slow, slow has traveled H+D and fast 2(H+D).

        Assume fast has traveled n loops in the cycle, we have:
        2H + 2D = H + D + nL  -->  H = nL - D

        Thus if two pointers start from head and X, respectively, one first reaches E, the other also reaches E.
        In my solution, since fast starts at head.next, we need to move slow one step forward in the beginning of part 2

        """
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        chaser = head
        walker = head
        s = 0
        # If there is a cycle, chaser will catch walker eventually
        res = 0
        while walker.next and chaser.next and chaser.next.next:
            walker = walker.next
            chaser = chaser.next.next
            if chaser == walker:
                res = 1
                break

        if res == 1:
            while head is not walker:
                head = head.next
                walker = walker.next
            return head
        else:
            return None

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
    node4.next = node2
    print(solution.detectCycle(head).val)

    head = ListNode(1)
    node2 = ListNode(2)
    head.next = node2
    node2.next = head
    #print(solution.detectCycle(head))

    solution = Solution()
    head = ListNode(3)
    node2 = ListNode(2)
    head.next = node2
    node3 = ListNode(0)
    node2.next = node3
    node4 = ListNode(-4)
    node3.next = node4
    #print(solution.detectCycle(head))

    #head = ListNode(1)
    #print(solution.detectCycle(head))

test()