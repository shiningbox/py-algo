from typing import List
from typing import Optional


class Solution:

    def quick_sort(self, l, r, array: list):
        # Find three sequences, L, P, R, bounded by 0, to Pivot -1, Pivot, Pivot + 1 to right_bound
        # Note that, L or R could be none, if less than 3
        # IF sequence size is 0 or 1
        if len(array) < 2:
            return

        if l >= r:
            return

        p = array[r]
        l_i = l
        r_i = r - 1
        # scan until left_stack index meets right_stack index
        # Find smaller elements (less than pivot) that needs to be moved to left_stack sequence
        # Find larger elements (larger than pivot) that needs to be moved to right_stack sequence
        while l_i <= r_i:
            # Find the left_stack index that are larger than pivot, which needs to be swapped
            while l_i <= r_i and array[l_i] <= p:
                l_i += 1
            # Find the right_stack index that are smaller than pivot, which needs to be swapped
            while l_i <= r_i and array[r_i] >= p:
                r_i -= 1
            if l_i < r_i:
                # Swap left_stack index and right_stack index
                temp = array[l_i]
                array[l_i] = array[r_i]
                array[r_i] = temp
        # Swap the r_
        temp = array[l_i]
        array[l_i] = array[r]
        array[r] = temp
        # Sort left_stack sequence
        self.quick_sort(l, l_i - 1, array)
        self.quick_sort(l_i + 1, r, array)

    """Given an integer array nums and an integer k, modify the array in the following way:

    choose an index i and replace nums[i] with -nums[i].
    You should apply this process exactly k times. You may choose the same index i multiple times.

    Return the largest possible sum of the array after modifying it in this way."""
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        self.quick_sort(0, len(nums) - 1, nums)
        # find first positve
        i = 0
        while i < len(nums) and nums[i] < 0:
            i += 1
        if i >= k:
            j = 0
            while j < k:
                nums[j] *= -1
                j += 1
        else:
            j = 0
            while j < i:
                nums[j] *= -1
                j += 1
            k = k - i
            if k % 2 != 0:
                # flip the min val
                if i < len(nums):
                    if nums[i - 1] <= nums[i]:
                        nums[i - 1] *= -1
                    else:
                        nums[i] *= -1
                else:
                    nums[i - 1] *= -1



        return sum(nums)


def test():
    solution = Solution()
    # test method
    print(solution.largestSumAfterKNegations([4, 2, 3], 1))
    print(solution.largestSumAfterKNegations([3, -1, 0, 2], 3))
    print(solution.largestSumAfterKNegations([2,-3,-1,5,-4], 2))
    print(solution.largestSumAfterKNegations([-8,3,-5,-3,-5,-2], 6))
    print(solution.largestSumAfterKNegations([-2,5,0,2,-2], 5))
    print(solution.largestSumAfterKNegations([-2,9,9,8,4], 5))


test()
