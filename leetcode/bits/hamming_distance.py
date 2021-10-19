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

    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        # count how many 1s
        return self.hammingWeight(xor)


def test():
    solution = Solution()
    # test method
    print(solution.hammingDistance(1, 4))
    print(solution.hammingDistance(3, 1))


test()
