from typing import List
from typing import Optional

class Solution:
    def countBits(self, n: int) -> List[int]:
        results = [None] * (n + 1)
        results[0] = 0
        if n == 0:
            return results
        # i & (i - 1) drops the lowest digit
        for i in range(1, n+1):
            results[i] = results[i & (i - 1)] + 1
        return results

def test():
    solution = Solution()

    # test method
    print(solution.countBits(0))
    print(solution.countBits(5))
    print(solution.countBits(2))
    print(solution.countBits(7))
    print(solution.countBits(8))
    print(solution.countBits(16))
    print(solution.countBits(64))


test()
