from typing import List
from typing import Optional

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        i = 2
        steps = [0] * (n + 1)
        steps[0] = 1
        steps[1] = 1
        while i <= n:
            steps[i] = steps[i - 1] + steps[i - 2]
            i += 1
        return steps[n]


def test():
    solution = Solution()
    # test method
    print(solution.climbStairs(1))
    print(solution.climbStairs(2))
    print(solution.climbStairs(3))
    print(solution.climbStairs(4))
    print(solution.climbStairs(5))
    print(solution.climbStairs(11))


test()
