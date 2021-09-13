from functools import reduce
from typing import List
from typing import Optional

class Solution:

    # xor of same ints will eliminate each other
    # e.g.,
    # 0001 xor 1111 = 1110
    # 1110 xor 1111 = 0001

    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            # Pairs of numbers will be eliminated with xor
            # Then the single number will be remained
            res ^= nums[i]
        return res

def test():
    solution = Solution()
    # test method
    print(solution.singleNumber([2, 2, 1]))
    print(solution.singleNumber([4, 1, 2, 1, 2]))

    nums = [5, 4, 2, 3, 5]
    # Python reduce/aggregation function
    result = reduce(lambda value, element: value + element, nums)

test()
