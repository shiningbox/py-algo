from typing import List
from typing import Optional

class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        # Index for tracking non-equal element
        ni = 0
        i = 0
        while i <= l - 1:
            if nums[i] != val:
                nums[ni] = nums[i]
                ni += 1
                i += 1
            else:
                i += 1
        print(nums[0:ni])
        return ni

def test():
    solution = Solution()
    # test method
    print(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 3))


test()
