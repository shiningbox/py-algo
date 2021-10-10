from typing import List
from typing import Optional

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        for num in nums:
            sum += num
        expected_sum = int((n * (n + 1)) / 2)
        return expected_sum - sum

def test():
    solution = Solution()
    # test method
    print(solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(solution.missingNumber([3, 0, 1]))
    print(solution.missingNumber([0]))


test()
