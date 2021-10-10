from typing import List
from typing import Optional

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        while j < len(nums) - 1:
            while i < len(nums) - 1 and nums[i] != 0:
                i += 1
            while j < len(nums) - 1 and nums[j] == 0:
                j += 1
            if i > j:
                j = i
                continue
            # swap i, j
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp


def test():
    solution = Solution()
    # test method
    print(solution.moveZeroes([0, 1, 0, 3, 12]))
    print(solution.moveZeroes([0]))
    print(solution.moveZeroes([0, 0]))
    print(solution.moveZeroes([1, 0, 1]))
    print(solution.moveZeroes([1, 2, 3, 0, 0]))


test()
