from typing import List
from typing import Optional

class Solution:

    def __init__(self):
        self.length = 0

    def dfs(self, nums, per, res):
        if len(per) == self.length:
            res.append(per)
            return
        diff = nums.difference(set(per))
        for item in diff:
            self.dfs(nums, per + [item], res)

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.length = len(nums)
        res = []
        self.dfs(set(nums), [], res)
        return res

def test():
    solution = Solution()
    # test method
    print(solution.permute([1,2,3]))


test()
