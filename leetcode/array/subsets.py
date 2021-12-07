from typing import List
from typing import Optional

class Solution:

    def get_combinations(self, nums, num, res):

        res.append(num)

        for i in range(len(nums)):
            self.get_combinations(nums[i+1:], num + [nums[i]], res)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.get_combinations(nums, [], res)
        return res


def test():
    solution = Solution()
    # test method
    print(solution.subsets([1,2,3]))


test()
