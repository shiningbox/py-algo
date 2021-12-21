from typing import List
from typing import Optional

class Solution:
    def __init__(self):
        self.min = 5000

    def find_pivot(self, l, h, nums):
        if l > h or l == len(nums) - 1:
            return -1
        else:
            mid = (h + l) // 2
            if nums[mid] > nums[mid+1]:

                return mid
            res1 = self.find_pivot(l, mid-1, nums)
            if res1 != -1:
                return res1
            else:
                return self.find_pivot(mid+1, h, nums)


    def findMin(self, nums: List[int]) -> int:
        self.min = 5000
        if len(nums) == 1:
            return nums[0]

        pivot = self.find_pivot(0, len(nums)-1, nums)

        return nums[pivot + 1]


def test():
    solution = Solution()
    # test method
    print(solution.findMin([3,4,5,1,2]))


test()
