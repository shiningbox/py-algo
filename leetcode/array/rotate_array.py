from typing import List
from typing import Optional

class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        s = k % l
        if l <= 1 or s == 0:
            return

        e = (l - k) % l
        j = e

        for i in range(s):
            nums[j], nums[i] = nums[i], nums[j]
            j = (j + 1) % l

        for _ in range(s):
            for j in range(l - 1, s, -1):
                nums[j], nums[j - 1] = nums[j-1], nums[j]

        print(nums)

def test():
    solution = Solution()
    # test method
    nums = [1,2,3,4,5,6,7]
    solution.rotate(nums, 3)
    solution.rotate([1], 3)
    solution.rotate([-1,-100,3,99], 2)
    solution.rotate([1, 2], 0)
    solution.rotate([1, 2], 2)
    solution.rotate([1,2,3,4,5,6], 1)
    solution.rotate([1,2,3], 4)


test()
