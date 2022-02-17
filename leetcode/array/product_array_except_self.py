from typing import List
from typing import Optional

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = [None] * len(nums)
        pre_prod[0] = nums[0]
        suf_prod = [None] * len(nums)
        suf_prod[-1] = nums[-1]

        for i in range(1, len(nums)):
            pre_prod[i] = pre_prod[i - 1] * nums[i]

        for i in range(len(nums) - 2, -1, -1):
            suf_prod[i] = suf_prod[i + 1] * nums[i]

        res = [None] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[i] = suf_prod[i + 1]
            elif i == len(nums) - 1:
                res[i] = pre_prod[i - 1]
            else:
                res[i] = pre_prod[i - 1] * suf_prod[i + 1]

        return res


def test():
    solution = Solution()
    # test method
    print(solution.productExceptSelf([1,2,3,4]))
    print(solution.productExceptSelf([5,6]))
    print(solution.productExceptSelf([5,6,7]))


test()
