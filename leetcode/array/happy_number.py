from typing import List
from typing import Optional

class Solution:

    def convert_int_digits(self, val):
        digits = []
        int_val = val
        while int_val != 0:
            remainder = int_val % 10
            digits.insert(0, remainder)
            int_val = int_val // 10
        return digits

    def isHappy(self, n: int) -> bool:
        res = n
        res_dict = {}
        while res != 1:
            squared_res = 0
            digits = self.convert_int_digits(res)
            for i in range(len(digits)):
                squared_res += digits[i] ** 2
            if squared_res in res_dict:
                return False
            else:
                res_dict[squared_res] = squared_res
            res = squared_res
        if res == 1:
            return True


def test():
    solution = Solution()
    # test method
    print(solution.isHappy(19))
    print(solution.isHappy(2))
    print(solution.isHappy(4))


test()
