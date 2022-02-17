from typing import List
from typing import Optional

class Solution:

    def majorityElement(self, nums: List[int]) -> List[int]:

        can1, count1, can2, count2 = 0, 0, 1, 0

        for num in nums:
            # if num equals can1
            if num == can1:
                count1 += 1
            # if num equals can2
            elif num == can2:
                count2 += 1
            # if can1 are eliminated
            elif count1 == 0:
                can1 = num
                count1 = 1
            # if can2 are eliminated
            elif count2 == 0:
                can2 = num
                count2 = 1
            # if num not equal to can1 and can2
            else:
                count1 -= 1
                count2 -= 1

        return [n for n in (can1, can2)
                if nums.count(n) > len(nums) // 3]


def test():
    solution = Solution()
    # test method
    print(solution.majorityElement([3,2,3]))


test()
