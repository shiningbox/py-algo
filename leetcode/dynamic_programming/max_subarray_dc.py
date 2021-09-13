from typing import List
from typing import Optional

class Solution:

    # l  ----m---    h
    # The subarray with max value is crossing m
    # either left_sum, or right_sum, or le
    def max_cross_sum(self, nums, l, h):
        cross_max = 0
        left_sum = -10000
        sum = 0
        mid = int((l + h) / 2)
        # Scan from mid to l
        for i in range(mid, l - 1, -1):
            sum += nums[i]
            if sum >= left_sum:
                left_sum = sum
        sum = 0
        right_sum = -10000
        # Scan from mid + 1 to h
        for j in range(mid + 1, h + 1, 1):
            sum += nums[j]
            if sum >= right_sum:
                right_sum = sum

        return max(left_sum + right_sum, left_sum, right_sum)

    # If array with max sum is within l to m
    # l ----- m     h
    # then max_subarray(l, m-1)
    # If array with the max sum is within m to h
    # l       m  ----   h
    # the max_subarray(nums, m+1, h)
    def max_subarray(self, nums, l, h):

        m = int((l + h) / 2)

        if l == h:
            return nums[l]
        else:
            return max(self.max_subarray(nums, l, m),
                       self.max_subarray(nums, m+1, h),
                       self.max_cross_sum(nums, l, h))

    def maxSubArray(self, nums: List[int]) -> int:
        return self.max_subarray(nums, 0, len(nums) - 1)

def test():
    solution = Solution()
    # test method
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(solution.maxSubArray([1]))
    print(solution.maxSubArray([5, 4, -1, 7, 8]))


test()
