from typing import List
from typing import Optional


class Solution:

    def threeSum(self, nums):
        res = []
        # sort the array first
        nums.sort()
        for current in range(len(nums) - 2):
            if current > 0 and nums[current] == nums[current - 1]:
                continue
            l, h = current + 1, len(nums) - 1
            while l < h:
                s = nums[current] + nums[l] + nums[h]
                # if sum is less than 0, we need to increase the sum
                if s < 0:
                    l += 1
                # if sum is larger than0, we need to decrease it
                elif s > 0:
                    h -= 1
                else:
                # if sum equals 0
                    res.append((nums[current], nums[l], nums[h]))
                    # if l and h equals to its next, skip them to avoid duplicated element
                    while l < h and nums[l] == nums[l + 1]:
                        l += 1
                    while l < h and nums[h] == nums[h - 1]:
                        h -= 1
                    l += 1
                    h -= 1
        return res

def test():
    solution = Solution()
    # test method
    print(solution.threeSum([-2, 1, 1]))
    print(solution.threeSum([]))
    print(solution.threeSum([0]))
    print(solution.threeSum([-1,0,1,2,-1,-4]))
    print(solution.threeSum([0, 0, 0]))
    print(solution.threeSum([0, 0, 0, 0]))
    print(solution.threeSum([-1,0,1,0]))
    print(solution.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))

test()
