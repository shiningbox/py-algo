from typing import List
from typing import Optional

class Solution:

    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        if len(nums) < 2:
            return nums

        l = 0
        h = len(nums) - 1
        while l < h:
            while l < h and nums[l] % 2 == 0:
                l += 1
            while l < h and nums[h] % 2 == 1:
                h -= 1
            # swap odd in the first part and even in the latter part
            nums[l], nums[h] = nums[h], nums[l]
            l += 1
            h -= 1

        return nums

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        nums = self.sortArrayByParity(nums)
        i = 0
        j = len(nums) - 1

        while i < j:
            while i < j and i % 2 == 0:
                i += 1
            while i < j and j % 2 == 1:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

            i += 1
            j -= 1

        return nums

def test():
    solution = Solution()
    # test method
    print(solution.sortArrayByParityII([4,2,5,7]))
    print(solution.sortArrayByParityII([2, 3]))


test()
