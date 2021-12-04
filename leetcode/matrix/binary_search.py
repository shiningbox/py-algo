from typing import List
from typing import Optional

class Solution:

    def two_to_one_index(self, matrix, coord):
        m = len(matrix)
        n = len(matrix[0])
        return coord[0] * n + coord[1]

    def one_index_to_two(self, matrix, index):
        m = len(matrix)
        n = len(matrix[0])
        return index // n, index %n

    def binary_search(self, matrix, low, high, val):

        low_index = self.two_to_one_index(matrix, low)
        high_index = self.two_to_one_index(matrix, high)

        if low_index > high_index:
            return -1

        mid_index = (low_index + high_index) // 2

        mid_row, mid_col = self.one_index_to_two(matrix, mid_index)
        print(mid_row, mid_col)

        if matrix[mid_row][mid_col] == val:
            return val

        if matrix[mid_row][mid_col] >= val:
            return self.binary_search(matrix, low, self.one_index_to_two(matrix, mid_index - 1), val)
        else:
            return self.binary_search(matrix, self.one_index_to_two(matrix, mid_index + 1), high, val)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        result = self.binary_search(matrix, (0, 0), (m-1, n-1), target)
        return result != -1


def test():
    solution = Solution()
    # test method
    print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
    print(solution.searchMatrix([[1,1]], 2))



test()
