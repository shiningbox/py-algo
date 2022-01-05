from typing import List
from typing import Optional

class Solution:

    def checkPossibility(self, nums: List[int]) -> bool:
        j = 1
        i = 0
        count = 1
        while j < len(nums):
            if nums[j] < nums[i]:
                if count == 0:
                    return False
                else:
                    if i > 0:
                        if nums[i - 1] > nums[j]:
                            nums[j] = nums[i]
                    count = 0
            i = j
            j += 1
        return True

def test():
    solution = Solution()
    # test method
    print(solution.checkPossibility([4,2,3]))
    print(solution.checkPossibility([4,2,1]))
    print(solution.checkPossibility([3,4,2,3]))


test()
