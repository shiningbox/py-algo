from typing import List
from typing import Optional

class Solution:

    # newton's method to find the root (f(x) = 0) of a function
    # xk+1 = xk - f(xk) / f'(xk)
    # f(r) = r ** 2 - x
    # thus r = r - (r ** 2 - x) / 2r
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        r = num // 2
        while r ** 2 > num:
            r = (r ** 2 + num) // (2 * r)
        return num == r ** 2


def test():
    solution = Solution()
    # test method
    print(solution.isPerfectSquare(4))
    print(solution.isPerfectSquare(8))
    print(solution.isPerfectSquare(9))
    print(solution.isPerfectSquare(16))
    print(solution.isPerfectSquare(14))


test()
