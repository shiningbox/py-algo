from typing import List
from typing import Optional

class Solution:

    def get_combinations(self, nums, k, num, res):

        if len(num) == k:
            res.append(num)
            return

        for i in range(len(nums)):
            self.get_combinations(nums[i+1:], k, num + [nums[i]], res)

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        res = []
        self.get_combinations(nums, k, [], res)
        return res


def test():
    solution = Solution()
    # test method
    print(solution.combine(2, 2))
    print(solution.combine(4, 2))


test()
