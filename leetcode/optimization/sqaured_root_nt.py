from typing import List
from typing import Optional

class Solution:

    # newton's method to find the root (f(x) = 0) of a function
    # xk+1 = xk - f(xk) / f'(xk)
    # f(r) = r ** 2 - x
    # thus r = r - (r ** 2 - x) / 2r =
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        r = x / 2
        while abs(r ** 2 - x) > 0.8:
            r = (r ** 2 + x) / (2 * r)
        return int(r)


def test():
    solution = Solution()
    # test method
    print(solution.mySqrt(4))
    print(solution.mySqrt(8))
    print(solution.mySqrt(9))


test()
