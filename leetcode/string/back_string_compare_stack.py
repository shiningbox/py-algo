from typing import List
from typing import Optional

class Solution:

    def pop_top(self, s, stack):
        for char in s:
            if char != "#":
                stack.append(char)
            else:
                if stack:
                    stack.pop(-1)

    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_a = []
        stack_b = []
        self.pop_top(s, stack_a)
        self.pop_top(t, stack_b)
        return "".join(stack_a) == "".join(stack_b)


def test():
    solution = Solution()
    # test method
    print(solution.backspaceCompare("a##j", "#a#j"))
    print(solution.backspaceCompare("a#j", "b"))


test()
