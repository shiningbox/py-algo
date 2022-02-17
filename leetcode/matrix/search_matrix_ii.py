from typing import List
from typing import Optional

class Solution:

    def binary_search(self, nums, low, high, val):

        if low < 0 or high < 0:
            return False

        if low > high:
            return False

        mid = (low + high) // 2
        if nums[mid] == val:
            return True

        if nums[mid] >= val:
            return self.binary_search(nums, low, mid - 1, val)
        else:
            return self.binary_search(nums, mid + 1, high, val)

    def column(self, matrix, i):
        return [row[i] for row in matrix]

    def binary_search_2d(self, matrix, l_r, l_c, h_r, h_c, target):

        if l_c < 0 or h_c < 0 or h_r < 0 or h_c < 0 or l_r > h_r or l_c > h_c:
            return False

        m_r = (l_r + h_r) // 2
        m_c = (l_c + h_c) // 2

        m_val = matrix[m_r][m_c]

        if m_val == target:
            return True

        row = matrix[m_r]
        row_res = self.binary_search(row, 0, len(matrix[0]) - 1, target)
        if row_res:
            return True

        column = self.column(matrix, m_c)
        col_res = self.binary_search(column, 0, len(matrix) - 1, target)
        if col_res:
            return True

        # Check top_left matrix
        if m_val > target:
            # binary search row and column
            res = self.binary_search_2d(matrix, l_r, l_c, m_r - 1, m_c - 1, target)
            if res:
                return True

        if m_val < target:
            # binary search row and column
            res = self.binary_search_2d(matrix, m_r + 1, m_c + 1, h_r, h_c, target)
            if res:
                return True

        # Check top-right
        res = self.binary_search_2d(matrix, l_r, m_c + 1, m_r - 1, h_c, target)
        if res:
            return True

        # Check bottom-left
        res = self.binary_search_2d(matrix, m_r + 1, l_c, h_r, m_c - 1, target)
        if res:
            return True

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        r = len(matrix)
        c = len(matrix[0])

        return self.binary_search_2d(matrix, 0, 0, r - 1, c - 1, target)


def test():
    solution = Solution()
    # test method
    print(solution.searchMatrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]], 4))
    print(solution.searchMatrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]], 2))
    print(solution.searchMatrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]], 9))
    print(solution.searchMatrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]], 11))



test()
