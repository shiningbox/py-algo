from typing import List

class Solution:
    # O(n)
    def reverse(self, x: int) -> int:

        if x <= -2 ** 31 or x >= 2 ** 31 - 1:
            return 0

        digits = []
        value = 0

        if x > 0:
            sign = 1
        else:
            sign = -1
            x = x * -1

        while x != 0:
            d = x % 10
            x = int(x / 10)
            digits.append(d)

        for i in range(len(digits)-1, -1, -1):
            value += digits[i] * (10 ** (len(digits) - i - 1))
        result = value * sign
        if -1 * 2 ** 31 <= result <= 2 ** 31 - 1:
            return result
        else:
            return 0


def test():
    solution = Solution()
    # test method
    print(solution.reverse(321))
    print(solution.reverse(-123))
    print(solution.reverse(120))
    print(solution.reverse(0))
    print(solution.reverse(1534236469))

test()
