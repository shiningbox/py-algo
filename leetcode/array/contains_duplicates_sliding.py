from typing import List
from typing import Optional

class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = nums[i]
            else:
                return True

        return False



def test():
    solution = Solution()
    # test method
    print(solution.containsDuplicate_sort([1, 2, 3, 1]))
    print(solution.containsDuplicate_sort([1, 2, 3, 4]))
    print(solution.containsDuplicate_sort([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


test()
