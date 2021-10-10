from typing import List
from typing import Optional

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):

            # Move j till it matches the s[i]
            while j < len(t) and t[j] != s[i]:
                j += 1

            if j == len(t):
                break
            j += 1
            i += 1

        if i == len(s):
            return True
        else:
            return False


def test():
    solution = Solution()
    # test method
    print(solution.isSubsequence("abc", "ahbgdc"))
    print(solution.isSubsequence("axc", "ahbgdc"))
    print(solution.isSubsequence("", ""))
    print(solution.isSubsequence("", "ahbgdc"))
    print(solution.isSubsequence("b", "c"))
    print(solution.isSubsequence("aaaaa", "bbaaa"))


test()
