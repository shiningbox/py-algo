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


def test():
    solution = Solution()
    # test method
    print(solution.sortArrayByParity([0]))
    print(solution.sortArrayByParity([1, 3, 5]))
    print(solution.sortArrayByParity([2, 1, 3, 5]))
    print(solution.sortArrayByParity([3, 1, 2, 4]))
    #print(solution.sortArrayByParity([0, 2]))

test()
