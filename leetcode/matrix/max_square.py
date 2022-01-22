from typing import List
from typing import Optional

class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        max_sq = [[0 for _ in range(n)] for _ in range(m)]
        size = 0

        for i in range(n):
            # initialize first row
            if matrix[0][i] == '1':
                max_sq[0][i] = 1
                size = 1

        for j in range(m):
            # initialize first column
            if matrix[j][0] == '1':
                max_sq[j][0] = 1
                size = 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    max_sq[i][j] = 1
                    # Check if we could expand the max square size by 1
                    pre_max = max_sq[i-1][j-1]
                    for k in range(1, pre_max + 1):
                        if not (i - k >= 0 and matrix[i - k][j] == '1' and \
                                j - k >= 0 and matrix[i][j - k] == '1'):
                            break
                        else:
                            max_sq[i][j] += 1

                    if max_sq[i][j] >= size:
                        size = max_sq[i][j]
        return size * size


def test():
    solution = Solution()
    # test method
    # print(solution.maximalSquare([["1","1","0"],
    #                               ["1","1","1"],
    #                               ["1","0","1"]]))
    # print(solution.maximalSquare([["0","1"],["1","0"]]))
    # print(solution.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    # print(solution.maximalSquare([["0"]]))
    # print(solution.maximalSquare([["0","1"],["0","1"]]))
    # print(solution.maximalSquare([["1","1","1","1","0"],
    #                               ["1","1","1","1","0"],
    #                               ["1","1","1","1","1"],
    #                               ["1","1","1","1","1"],
    #                               ["0","0","1","1","1"]]))
    # print(solution.maximalSquare([["0","0","0","0","0"],
    #                               ["0","0","0","0","0"],
    #                               ["0","0","0","0","1"],
    #                               ["0","0","0","0","0"]]))
    print(solution.maximalSquare([["0","0","0","1"],
                                  ["1","1","0","1"],
                                  ["1","1","1","1"],
                                  ["0","1","1","1"],
                                  ["0","1","1","1"]]))

test()
