from typing import List
from typing import Optional

class Solution:

    def __init__(self):
        self.length = 0

    def dfs(self, subset, path, res, visited):
        if not subset:
            res.append(path)
            return
        for i in range(len(subset)):
            # e.g.,
            # 1 2 3
            # use subset[:i] + subset[i + 1:] to get a subset subtracting item[i]
            if i > 0 and not visited[i-1] and subset[i - 1] == subset[i]:
                    continue
            self.dfs(subset[:i] + subset[i + 1:], path + [subset[i]], res, visited)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.length = len(nums)
        res = []
        nums.sort()
        visited = [False] * len(nums)
        self.dfs(nums, [], res, visited)
        return res

def test():
    solution = Solution()
    # test method
    print(solution.permuteUnique([1,1,2]))
    print(solution.permuteUnique([1,1,1,2]))


test()
