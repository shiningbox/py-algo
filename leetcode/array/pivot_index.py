from typing import List
from typing import Optional

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_list = [0]
        for i in range(len(nums)):
            sum_list.append(sum_list[-1] + nums[i])
        i = 0
        total_sum = sum_list[-1]
        print(sum_list)
        while i < len(sum_list) - 1:
            if sum_list[i] == total_sum - sum_list[i + 1]:
                return i
            i += 1
        return -1


def test():
    solution = Solution()
    # test method
    print(solution.pivotIndex([1,7,3,6,5,6]))
    print(solution.pivotIndex([1,2,3]))
    print(solution.pivotIndex([0,0,0,1,2]))
    print(solution.pivotIndex([2, 1, -1]))


test()
