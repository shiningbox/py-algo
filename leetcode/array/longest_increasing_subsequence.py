from typing import List
from typing import Optional

class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:

        l = [1]*len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    l[i] = max(l[i], l[j] + 1)

        return max(l)

def test():
    solution = Solution()
    # test method
    print(solution.lengthOfLIS([0,1,0,3,2,3]))


test()
