from typing import List
from typing import Optional

class Solution:

    # Start with empty
    def majorityElement(self, nums: List[int]) -> int:
        # Count is the current winner
        candidate, count = nums[0], 0
        for i in range(len(nums)):
            # No winner
            if count == 0:
                # Current one becomes candidate
                candidate = nums[i]
                count += 1
            else:
                # If the candidate has some count
                # But if the next one is not candiate
                # reduce count
                if nums[i] != candidate:
                    count -= 1
                else:
                # else, add one
                    count += 1
        return candidate

def test():
    solution = Solution()
    # test method
    print(solution.majorityElement([3, 2, 3]))
    print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
    print(solution.majorityElement([6, 5, 5]))
    print(solution.majorityElement([6]))


test()
