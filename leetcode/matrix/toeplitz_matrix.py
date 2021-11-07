from typing import List
from typing import Optional

class Solution:

    def check_equal(self, nums):
        return nums.count(nums[0]) == len(nums)

    def get_diagonals(self, matrix, r_i, c_i):
        diagonals = []
        while c_i >= 0 and r_i >= 0:
            diagonals.append(matrix[r_i][c_i])
            c_i -= 1
            r_i -= 1
        return diagonals

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # Get lower diagonals
        for i in range(n):
            if not self.check_equal(self.get_diagonals(matrix, m - 1, i)):
                return False
        # Get upper diagonals
        for i in range(m-2, -1, -1):
            if not self.check_equal(self.get_diagonals(matrix, i, n-1)):
                return False

        return True
def test():
    solution = Solution()
    # test method
    print(solution.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
    print(solution.isToeplitzMatrix([[1,2],[2,2]]))


test()
