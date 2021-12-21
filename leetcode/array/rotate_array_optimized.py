from typing import List
from typing import Optional

class Solution:

    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def rotate(self, nums: List[int], k: int) -> None:

        len_n = len(nums)

        if not nums or len_n < 2:
            return

        k = k % len_n
        self.reverse(nums, 0, len_n - k - 1)
        self.reverse(nums, len_n - k, len_n - 1)
        self.reverse(nums, 0, len_n - 1)


def test():
    solution = Solution()

    # test method
    solution.rotate([1,2,3,4,5,6,7], 3)
    solution.rotate([1], 3)
    solution.rotate([-1,-100,3,99], 2)
    solution.rotate([1, 2], 0)
    solution.rotate([1, 2], 2)
    solution.rotate([1,2,3,4,5,6], 1)
    solution.rotate([1,2,3], 4)


test()
