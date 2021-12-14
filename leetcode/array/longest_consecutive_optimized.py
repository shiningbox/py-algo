from typing import List
from typing import Optional

class Solution:

    def union_adj(self, num, n_dict):
        left = right = 0

        if num not in n_dict:
            return 0
        del n_dict[num]

        if (num - 1) in n_dict:
            left = self.union_adj(num - 1,  n_dict)

        if (num + 1) in n_dict:
            right = self.union_adj(num + 1, n_dict)


        return left + right + 1

    def longestConsecutive(self, nums: List[int]) -> int:
        max_cont = 0
        n_dict = {}
        for i in range(len(nums)):
            n_dict[nums[i]] = i
        for num in nums:
            if num not in n_dict:
                continue
            else:
                res = self.union_adj(num, n_dict)
                if res >= max_cont:
                    max_cont = res

        return max_cont

def test():
    solution = Solution()
    # test method
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(solution.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))


test()
