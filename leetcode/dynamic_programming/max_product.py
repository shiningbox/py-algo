from typing import List
from typing import Optional

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        # Only need to use n**2 / 2 memory space
        # create a triangular matrix
        d = []
        max_sum = nums[0]

        for i in range(length):
            row = [0] * (i + 1)
            d.append(row)
            for j in range(i+1):
                if j == i:
                    d[i][j] = nums[j]
                else:
                    if j <= i - 1:
                        d[i][j] = nums[i] * d[i - 1][j]
                if d[i][j] >= max_sum:
                    max_sum = d[i][j]

        return max_sum


def test():
    solution = Solution()
    # test method
    #print(solution.maxProduct([2, 3, -2, 4]))
    #print(solution.maxProduct([-2, 0, -1]))
    #print(solution.maxProduct([-2, 3, -4]))
    print(solution.maxProduct([3, -1, 4]))
    #print(solution.maxProduct([2,-5,-2,-4,3]))
    print(solution.maxProduct([0, 2]))


test()
