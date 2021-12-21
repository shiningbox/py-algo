from typing import List
from typing import Optional

class Solution:

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

    def binary_search(self, l, h, nums, target):
        if l > h:
            return -1
        mid = (h + l)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary_search(l, mid-1, nums, target)
        else:
            return self.binary_search(mid+1, h, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        pivot = self.find_pivot(0, len(nums)-1, nums)
        if pivot == -1:
            return self.binary_search(0, len(nums)-1, nums, target)
        else:
            res1 = self.binary_search(0, pivot, nums, target)
            if res1 != -1:
                return res1
            else:
                return self.binary_search(pivot + 1, len(nums) - 1, nums, target)


def test():
    solution = Solution()
    # test method
    print(solution.search([4,5,6,7,0,1,2]))


test()
