from typing import List
from typing import Optional

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        f_nums = [0] * (n + 1)
        f_nums[0] = 0
        f_nums[1] = 1
        for i in range(2, len(f_nums), 1):
            f_nums[i] = f_nums[i - 1] + f_nums[i - 2]
        return f_nums[n]


def test():
    solution = Solution()
    # test method
    print(solution.fib(0))
    print(solution.fib(1))
    print(solution.fib(2))
    print(solution.fib(3))
    print(solution.fib(4))


test()
