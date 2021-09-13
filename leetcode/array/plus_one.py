from typing import List
from typing import Optional

class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        i = l - 1
        if digits[i] != 9:
            digits[i] += 1
        else:
            digits[i] = 0
            i -= 1
            all_nine = True
            while i >= 0:
                if digits[i] != 9:
                    all_nine = False
                    digits[i] += 1
                    return digits
                else:
                    digits[i] = 0
                    i -= 1
            if all_nine:
                digits = [1] + digits

        return digits

    def plusOne_small(self, digits: List[int]) -> List[int]:
        v = 0
        d = 0
        # Digits to value
        for i in range(len(digits) - 1, -1, -1):
            v += digits[i] * 10 ** d
            d += 1
        v += 1
        print(v)
        new_digits = []
        while v > 0:
            i = v % 10
            v = int(v / 10)
            new_digits = [i] + new_digits
        return new_digits

def test():
    solution = Solution()
    # test method
    print(solution.plusOne([1, 2, 3]))
    print(solution.plusOne([4, 3, 2, 1]))
    print(solution.plusOne([0]))
    print(solution.plusOne([9]))
    print(solution.plusOne([9, 9]))
    print(solution.plusOne([9, 9, 9]))
    print(solution.plusOne([9, 8, 9]))
    print(solution.plusOne([6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3]))


test()
