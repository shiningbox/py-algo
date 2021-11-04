from typing import List
from typing import Optional

class Solution:

    def hasAlternatingBits(self, n: int) -> bool:
        if n < 2:
            return True

        prev = n & 1
        n = n >> 1
        while n > 0:
            e = n & 1
            if e == prev:
                return False
            prev = e
            n = n >> 1

        return True

def test():
    solution = Solution()
    # test method
    print(solution.hasAlternatingBits(5))
    print(solution.hasAlternatingBits(7))
    print(solution.hasAlternatingBits(1))


test()
