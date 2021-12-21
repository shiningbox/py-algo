from typing import List
from typing import Optional

class Solution:

    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        d = [0] * length
        global_max = d[0]
        for i in range(length):
            local_max = 0
            for j in range(i+1):
                if j == i - 1:
                    continue
                elif j == i:
                    if nums[j] >= local_max:
                        local_max = nums[j]
                else:
                    if nums[i] + d[j] >= local_max:
                        local_max = nums[i] + d[j]
            if local_max >= global_max:
                global_max = local_max
            d[i] = local_max
        return global_max


def test():
    solution = Solution()
    # test method
    print(solution.rob([1]))
    print(solution.rob([1,2,3,1]))
    print(solution.rob([2,7,9,3,1]))
    print(solution.rob([1, 2, 1, 2]))


test()
