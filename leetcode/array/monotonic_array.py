from typing import List
from typing import Optional

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        if len(nums) < 2:
            return True

        increased = False
        decreased = False
        all_equal = True
        i = 0
        j = 1

        while j < len(nums):

            if nums[i] == nums[j]:
                i = j
                j += 1
                continue

            if nums[i] < nums[j]:
                all_equal = False
                if decreased:
                    return False
                else:
                    increased = True
                    decreased = False
            else:
                all_equal = False
                if increased:
                    return False
                else:
                    increased = False
                    decreased = True
            i = j
            j += 1

        return increased or decreased or all_equal

def test():
    solution = Solution()
    # test method
    print(solution.isMonotonic([1,2,2,3]))
    print(solution.isMonotonic([6,5,4,4]))
    print(solution.isMonotonic([1,3,2]))
    print(solution.isMonotonic([1,2,4,5]))
    print(solution.isMonotonic([1, 1, 1]))


test()
