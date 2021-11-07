from typing import List
from typing import Optional

class Solution:

    def binary_search(self, nums, low, high, val):
        if low > high:
            return -1

        mid = (low + high) // 2
        if nums[mid] == val:
            return mid

        if nums[mid] >= val:
            return self.binary_search(nums, low, mid - 1, val)
        else:
            return self.binary_search(nums, mid + 1, high, val)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)


def test():
    solution = Solution()
    # test method
    print(solution.search([-1,0,3,5,9,12], 9))
    print(solution.search([-1,0,3,5,9,12], 2))
    print(solution.search([-1], -1))


test()
