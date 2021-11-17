from typing import List
from typing import Optional

class Solution:
    def removeDuplicates(self, s: str) -> str:
        c_stack = [None]
        for char in s:
            top = c_stack[-1]
            if char == top:
                c_stack.pop()
            else:
                c_stack.append(char)
        c_stack.pop(0)
        return "".join(c_stack)


def test():
    solution = Solution()
    # test method
    print(solution.removeDuplicates("abbaca"))


test()
