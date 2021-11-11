from typing import List
from typing import Optional

class Solution:

    def check_rotated_strings(self, a, b, r):
        for i in range(len(a)):
            if b[i] != a[(i + r) % len(a)]:
                return False
        return True

    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True

        if len(s) != len(goal):
            return False

        for i in range(1, len(s)):
            if self.check_rotated_strings(s, goal, i):
                return True

        return False


def test():
    solution = Solution()
    # test method
    print(solution.rotateString("abcde", "cdeab"))
    print(solution.rotateString("aaac", "aaca"))
    print(solution.rotateString("abcde", "abced"))
    print(solution.rotateString("a", "b"))
    print(solution.rotateString("ohbrwzxvxe", "uornhegseo"))


test()
