from typing import List
from typing import Optional

class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            # If nums appear more than once
            if nums[i] in count_dict:
                if count_dict[nums[i]] >= len(nums) // 2:
                    return nums[i]
                count_dict[nums[i]] += 1
            else:
                count_dict[nums[i]] = 1


def test():
    solution = Solution()
    # test method
    print(solution.majorityElement([3, 2, 3]))
    print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
    print(solution.majorityElement([6, 5, 5]))
    print(solution.majorityElement([6]))


test()
