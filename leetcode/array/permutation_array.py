from typing import List
from typing import Optional

class Solution:

    def __init__(self):
        self.length = 0

    def dfs(self, subset, path, res):
        if not subset:
            res.append(path)
            return
        for i in range(len(subset)):
            # e.g.,
            # 1 2 3
            # use subset[:i] + subset[i + 1:] to get a subset subtracting item[i]
            # [1, 2, 3]
            # i = 0, subset[:0], subset[1:]  subset = [] + [2, 3], path = [1]
                # i = 0, subset[:0], subset[1:] -> subset = [] + [3], path = [1, 2]  ->
                    # [3]
                    # i = 0, subset[:0], subset[1:] -> subset = [], return path = [1, 2, 3]
                # i = 1, subset[:1], subset[2:] -> subset = [2] + [], path = [1, 3]
                    # [2]
                    # i = 0, subset[:0], subset[1:] -> subset = [], return path = [1, 3, 2]

            # i = 1, subset[:2], subset[2:], subset = [1] + [3], path = [2]
                # [1, 3]
                # i = 0, subset[:0], subset[1:] = [] + [3], path = [2, 1]
                    # [3]
                    # i = 0, subset[:0], subset[1:] = [], return path = [2, 1, 3]
                # i = 1, subset[:1], subset[2:]
            # ...
            self.dfs(subset[:i] + subset[i + 1:], path + [subset[i]], res)

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.length = len(nums)
        res = []
        self.dfs(nums, [], res)
        return res

def test():
    solution = Solution()
    # test method
    print(solution.permute([1,2,3]))


test()
