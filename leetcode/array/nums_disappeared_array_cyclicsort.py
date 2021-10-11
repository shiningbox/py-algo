from typing import List
from typing import Optional

class Solution(object):
    def findDisappearedNumbers(self, nums):
        results = []
        # cyclic sort
        for i in range(len(nums)):
            c_index = nums[i] - 1
            while c_index < len(nums) and nums[i] != nums[c_index]:
                temp = nums[c_index]
                nums[c_index] = nums[i]
                nums[i] = temp
                c_index = nums[i] - 1
        print(nums)

def test():
    solution = Solution()
    # test method
    print(solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
    #print(solution.findDisappearedNumbers([1, 1]))
    #print(solution.findDisappearedNumbers([4, 1, 3, 1, 3]))


test()
