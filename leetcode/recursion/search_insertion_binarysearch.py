from typing import List
from typing import Optional

class Solution:

    def binary_search(self, nums, l, h, target):

        if l > h:
            # End of recursion
            # Why return l here?
            # Case 1 target <= nums[0]:
            #        If h keeps reduced by mid - 1 till l = h, mid = l = h = 0
            #        Next time, l = 0, h = -1 then return l

            # Case 2 target >= nums[len - 1]:
            #        If l keeps increased by mid + 1 till l = h, mid = l = h = len - 1
            #        Next time, l = len, h = len - 1, return l = len

            # Case 3 target in (0, len - 1):
            #
            #        The position is either in mid, (l, mid - 1), or (mid + 1, l)
            return l
            # Continue searching
        else:
            mid = int((l + h) / 2)
            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                # go to left half
                return self.binary_search(nums, l, mid - 1, target)
            else:
                # go to the right half
                return self.binary_search(nums, mid + 1, h, target)

    # Find the target element
    # Or the smallest element that larger than target
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)


def test():
    solution = Solution()
    # test method
    print(solution.searchInsert([1, 3, 5, 6], 5))
    print(solution.searchInsert([1, 3, 5, 6], 3))
    print(solution.searchInsert([1, 3, 5, 6], 2))
    print(solution.searchInsert([1, 3, 5, 6], 7))
    print(solution.searchInsert([1, 3, 5, 6], 0))
    print(solution.searchInsert([1], 0))


test()
