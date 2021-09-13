from typing import List
from typing import Optional

class Solution:

    def char_int(self, char):
        return ord(char) - 64

    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            res += self.char_int(columnTitle[i]) * (26 ** (len(columnTitle) - i - 1))
        return res


def test():
    solution = Solution()
    # test method
    print(solution.titleToNumber("A"))
    print(solution.titleToNumber("AB"))
    print(solution.titleToNumber("ZY"))
    print(solution.titleToNumber("FXSHRXW"))


test()
