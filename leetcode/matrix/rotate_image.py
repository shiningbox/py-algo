from typing import List
from typing import Optional

class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)

        if n > 1:
            pass

        mid = (n - 1) // 2
        j = 0

        while j <= mid:

            i = 0
            end = mid
            if n % 2 == 1:
                end = mid - 1

            while i <= end:
                r = 0
                row = i
                col = j
                prev = matrix[row][col]
                while r <= 3:
                    next_row = col
                    next_col = n - 1 - row
                    temp = matrix[next_row][next_col]
                    matrix[next_row][next_col] = prev
                    prev = temp
                    row = next_row
                    col = next_col
                    r += 1
                i += 1
            j += 1

def test():
    solution = Solution()
    # test method
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    #solution.rotate(matrix)
    print(matrix)
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    #solution.rotate(matrix)
    print(matrix)
    matrix = [[1,2],[3,4]]
    #solution.rotate(matrix)
    print(matrix)
    matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    solution.rotate(matrix)
    print(matrix)

test()
