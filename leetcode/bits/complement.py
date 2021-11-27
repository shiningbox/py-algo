from typing import List
from typing import Optional

class Solution(object):

    def findComplement(self, num):
        i = 1
        # left_stack shift 1 till it is larger than num
        # e.g., 101
        # 001 -> 010 -> 100 -> 1000
        # then 1000 - 1 = 8 - 1 = 7 = 111
        # 111 ^ 101 = 010 = 2
        while i <= num:
            i = i << 1
        return (i - 1) ^ num

def test():
    solution = Solution()
    # test method
    print(solution.findComplement(5))
    print(solution.findComplement(1))


test()
