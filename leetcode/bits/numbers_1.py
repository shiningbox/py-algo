from typing import List
from typing import Optional

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            last_digit = n & 1
            if last_digit == 1:
                count += 1
            n >>= 1
        return count

def test():
    solution = Solution()
    # test method
    print(solution.hammingWeight(11))
    print(solution.hammingWeight(128))


test()
