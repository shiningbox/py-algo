from typing import List
from typing import Optional

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_dict = {}
        for num in nums:
            num_dict[num] = num

        for i in range(len(nums) + 1):
            if i not in num_dict.keys():
                return i

def test():
    solution = Solution()
    # test method
    print(solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(solution.missingNumber([3, 0, 1]))
    print(solution.missingNumber([0]))


test()
