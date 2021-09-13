from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n2) -> O(2n)
        d_dict = {}
        length = len(nums)
        for i in range(0, length):
            d_dict[nums[i]] = i
        for i in range(0, length):
            differ = target - nums[i]
            if differ in d_dict and i != d_dict[differ]:
                return [i, d_dict[differ]]
        return None


def test():

    nums = [3, 2, 4]
    target = 6

    solution = Solution()
    print(solution.twoSum(nums, target))

test()