from typing import List
from typing import Optional

class Solution:
    #1
    #100
    #10000
    #1000000
    #100000000
    #10000000000
    #1000000000000
    #100000000000000
    #10000000000000000
    #1000000000000000000
    #100000000000000000000
    #10000000000000000000000
    #1000000000000000000000000
    #100000000000000000000000000
    #10000000000000000000000000000
    #1000000000000000000000000000000
    def isPowerOfFour(self, n: int) -> bool:
        return n != 0 and n & (n - 1) == 0 and n & 1431655765 == n


def test():
    solution = Solution()
    # test method
    print(solution.isPowerOfFour(16))
    print(solution.isPowerOfFour(5))
    print(solution.isPowerOfFour(64))
    print(solution.isPowerOfFour(256))


test()
