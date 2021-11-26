from typing import List
from typing import Optional


class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:

        m_s = nums[0] + nums[1] + nums[2]

        # sort the array first
        nums.sort()

        for current in range(len(nums) - 2):
            l, h = current + 1, len(nums) - 1
            while l < h:
                s = nums[current] + nums[l] + nums[h]
                # if sum is less than 0, we need to increase the sum
                if s < target:
                    if abs(s - target) <= abs(m_s - target):
                        m_s = s
                    l += 1
                elif s > target:
                    if abs(s - target) <= abs(m_s - target):
                        m_s = s
                    h -= 1
                else:
                    return s

        return m_s

def test():
    solution = Solution()
    # test method
    print(solution.threeSumClosest([1 ,1 ,1, 0], -100))
    print(solution.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))
    print(solution.threeSumClosest([-1, 2, 1, -4], 1))
    print(solution.threeSumClosest([0,0,0], 2))


test()
