from typing import List
from typing import Optional

class Solution:

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        s = p = 0
        length = 1
        while s < len(nums):
            p = s

            while p + 1 < len(nums) and nums[p] < nums[p + 1]:
                p += 1

            new_len = p - s + 1

            if new_len >= length:
                length = new_len

            s = p + 1

        return length


def test():
    solution = Solution()
    # test method
    print(solution.findLengthOfLCIS([1,3,5,4,7]))
    print(solution.findLengthOfLCIS([2,2,2,2,2]))
    print(solution.findLengthOfLCIS([2]))


test()
