from typing import List
from typing import Optional

class Solution:

    def canJump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return True
        else:
            if nums[0] == 0:
                return False

        ranges = [0] * len(nums)
        ranges[0] = nums[0]

        i = 1
        while i < len(nums):

            # max range can be extended
            if ranges[i - 1] > i + nums[i]:
                    ranges[i] = ranges[i - 1]
            else:
                    if nums[i] == 0:
                        return False
                    ranges[i] = nums[i] + i

            if ranges[i] >= len(nums) - 1:
                return True

            i += 1

        return False


def test():
    solution = Solution()
    # test method
    print(solution.canJump([2,3,1,1,4]))
    print(solution.canJump([3,2,1,0,4]))
    print(solution.canJump([0, 1]))
    print(solution.canJump([0, 2, 3]))
    print(solution.canJump([0]))
    print(solution.canJump([3,0,8,2,0,0,1]))


test()
