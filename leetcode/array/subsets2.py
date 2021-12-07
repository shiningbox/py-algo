from typing import List
from typing import Optional

class Solution:

    def __init__(self):
        self.nums = []

    def get_combinations(self, nums, num, res):

        res.append(num)

        for i in range(len(nums)):
            if 0 < i < len(nums) and nums[i] == nums[i - 1]:
                continue

            self.get_combinations(nums[i+1:], num + [nums[i]], res)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.nums = nums
        self.get_combinations(nums, [], res)
        return res


def test():
    solution = Solution()
    # test method
    print(solution.subsetsWithDup([1,2,2]))
    print(solution.subsetsWithDup([0]))


test()
