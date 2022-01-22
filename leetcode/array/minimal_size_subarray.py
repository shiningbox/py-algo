from typing import List
from typing import Optional

class Solution:

    def binary_search(self, target, nums, l, h):
        if l > h:
            if 0 <= h <= len(nums) - 1 and nums[h] > target:
                return h
            if 0 <= l <= len(nums) - 1 and nums[l] > target:
                return l
            return

        mid = (l + h) // 2
        if nums[mid] > target:
            return self.binary_search(target, nums, l, mid - 1)
        elif nums[mid] < target:
            return self.binary_search(target, nums, mid + 1, h)
        return mid

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        size = len(nums)
        for i in range(len(nums)):
            pre_sums = [nums[i]]
            for j in range(i + 1, len(nums)):
                pre_sums.append(nums[j] + pre_sums[-1])
            res = self.binary_search(target, pre_sums, 0, len(pre_sums) - 1)
            if res is not None:
                if res + 1 <= size:
                    size = res + 1
        return size

def test():
    solution = Solution()
    # test method
    #print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))
    #print(solution.minSubArrayLen(4, [1,4, 4]))
    #print(solution.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
    #print(solution.minSubArrayLen(11, [1,2,3,4,5]))
    #print(solution.minSubArrayLen(15, [1,2,3,4,5]))
    #print(solution.minSubArrayLen(6, [10, 2, 3]))
    print(solution.minSubArrayLen(15, [5,1,3,5,10,7,4,9,2,8]))

test()
