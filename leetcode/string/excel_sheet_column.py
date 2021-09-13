from typing import List
from typing import Optional

class Solution:
    # A - Z, 65 to 90
    def map_num_char(self, val):
        return chr(val + 65)

    # 0 to 9, 10 base
    # A to Z, 26 base, A = 0, Z = 25
    # The column number starts with 1, thus needs to decrease by 1
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber > 0:
            remainder = (columnNumber - 1) % 26
            res.insert(0, self.map_num_char(remainder))
            columnNumber = (columnNumber - 1) // 26

        return "".join(res)

def test():
    solution = Solution()
    # test method
    print(solution.convertToTitle(1))
    print(solution.convertToTitle(28))
    print(solution.convertToTitle(701))
    print(solution.convertToTitle(2147483647))


test()
