from typing import List
from typing import Optional

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if 0 < n <= 2:
            return True
        if n > 0 and n % 2 == 0:
            return self.isPowerOfTwo(n / 2)
        return False

def test():
    solution = Solution()
    # test method
    print(solution.isPowerOfTwo(0))
    print(solution.isPowerOfTwo(1))
    print(solution.isPowerOfTwo(16))
    print(solution.isPowerOfTwo(3))
    print(solution.isPowerOfTwo(4))


test()
