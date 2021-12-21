from typing import List
from typing import Optional


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # also need to maintain the min value
        # because min value could be negative turned into max value
        # if multiplied by an negative value
        cur_max, cur_min = 1, 1
        res = nums[0]

        for n in nums:
            vals = (n, n * cur_max, n * cur_min)
            cur_max, cur_min = max(vals), min(vals)
            res = max(res, cur_max)

        return res


def test():
    solution = Solution()
    # test method
    #print(solution.maxProduct([2, 3, -2, 4]))
    #print(solution.maxProduct([-2, 0, -1]))
    #print(solution.maxProduct([-2, 3, -4]))
    print(solution.maxProduct([3, -1, 4]))
    print(solution.maxProduct([2,-5,-2,-4,3]))
    print(solution.maxProduct([0, 2]))


test()
