from typing import List
from typing import Optional

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        h = len(s) - 1

        while l <= h:
            # swap l and h
            temp = s[l]
            s[l] = s[h]
            s[h] = temp
            l += 1
            h -= 1

        print(s)

def test():
    solution = Solution()
    # test method
    print(solution.reverseString(["h","e","l","l","o"]))
    print(solution.reverseString(["H","a","n","n","a","h"]))
    print(solution.reverseString(["a"]))


test()
