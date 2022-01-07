from typing import List
from typing import Optional

class Solution:
    """The basic idea is to track the index of the left bracket and star position.
    Push all the indices of the star and left bracket to their stack respectively.

    STEP 1
    Once a right bracket comes, pop left bracket stack first if it is not empty.
    If the left bracket stack is empty, pop the star stack if it is not empty.


    STEP 2
    Note that the left bracket CANNOT appear after the star as there is NO way to balance the bracket.
    In other words, whenever there is a left bracket index appears after the Last star,
    a false statement can be made. Otherwise, pop out each from the left bracket and star stack.

    e.g., *(

    STEP 3
    A correct sequence should have an empty left bracket stack. You don't need to take care of the star stack.

    Greedy algorithm is used here. We always want to use left brackets to balance the right one first as the * symbol is a wild card. """

    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []

        for i in range(len(s)):
            c = s[i]
            if c == '(':
                left_stack.append(i)
            elif c == '*':
                star_stack.append(i)
            else:
                if not left_stack and not star_stack:
                    return False
                if left_stack:
                    left_stack.pop()
                else:
                    star_stack.pop()

        while left_stack and star_stack:
            if left_stack.pop() > star_stack.pop():
                return False

        return not left_stack



def test():
    solution = Solution()
    # test method

    # True
    print(solution.checkValidString("*"))
    print(solution.checkValidString("(*)"))
    print(solution.checkValidString("()"))
    print(solution.checkValidString("(())"))
    print(solution.checkValidString("(())()"))
    print(solution.checkValidString("*)"))
    print(solution.checkValidString("(*"))
    print(solution.checkValidString("(*))"))
    print(solution.checkValidString("(((**))"))

    # False
    print(solution.checkValidString("(*)))"))


test()
