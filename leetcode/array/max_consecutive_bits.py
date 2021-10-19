from typing import List
from typing import Optional


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start = 0
        end = 0
        sum = 0
        while end < len(nums):
            if nums[end] == 1:
                start = end
                while end < len(nums) and nums[end] == 1:
                    end += 1
                if end - start >= sum:
                    sum = end-start
            else:
                end += 1
        return sum

def test():
    solution = Solution()
    # test method
    print(solution.findMaxConsecutiveOnes([1, 1, 1, 1, 1]))
    print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))
    #print(solution.findMaxConsecutiveOnes([1,0,1,1,0,1]))
    #print(solution.findMaxConsecutiveOnes([1]))
    #print(solution.findMaxConsecutiveOnes([0]))


test()
