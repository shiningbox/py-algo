from typing import List
from typing import Optional

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the linkedlist, get all the indexes
        # who points to a positive number
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


def test():
    solution = Solution()
    # test method
    print(solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
    #print(solution.findDisappearedNumbers([1, 1]))
    #print(solution.findDisappearedNumbers([4, 1, 3, 1, 3]))


test()
