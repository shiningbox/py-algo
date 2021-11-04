from typing import List
from typing import Optional


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        total = 0

        if len(s) < 2:
            return total

        p = i = 0
        bp = 0
        while p < len(s):
            f_count = 0
            s_count = 0
            i = p
            while i < len(s) and s[p] == s[i]:
                f_count += 1
                i += 1
            bp = i
            while i < len(s) and s[p] != s[i] and s_count < f_count:
                s_count += 1
                i += 1
            p = bp

            if f_count == s_count:
                total += (f_count + s_count) // 2
            elif s_count < f_count:
                total += s_count

        return total
def test():
    solution = Solution()
    # test method
    print(solution.countBinarySubstrings("0011"))
    print(solution.countBinarySubstrings("01"))
    print(solution.countBinarySubstrings("000111"))
    print(solution.countBinarySubstrings("00011101"))
    print(solution.countBinarySubstrings("00110011"))
    print(solution.countBinarySubstrings("10101"))
    print(solution.countBinarySubstrings("00110"))


test()
