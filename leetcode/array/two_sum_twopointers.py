from typing import List
from typing import Optional

class Solution:
    # numbers that is already sorted in non-decreasing order
    # sorted, then consider binary tree
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        return [i + 1, j + 1]

def test():
    solution = Solution()
    # test method
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([2, 3, 4], 6))
    print(solution.twoSum([-1, 0], -1))


test()
