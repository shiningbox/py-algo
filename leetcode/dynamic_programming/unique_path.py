from typing import List
from typing import Optional

class Solution:





    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[0 for j in range(n)] for i in range(m)]
        mat[0][0] = 1
        i = j = 0
        while j <= n - 1:
            i = 0
            while i <= m - 1:
                path_sum = 0
                if j - 1 >= 0:
                    path_sum += mat[i][j - 1]
                if i - 1 >= 0:
                    path_sum += mat[i - 1][j]
                mat[i][j] += path_sum
                i += 1
            j += 1
        return mat[m-1][n-1]


def test():
    solution = Solution()
    # test method
    print(solution.uniquePaths(2, 2))
    print(solution.uniquePaths(3, 2))
    #print(solution.uniquePaths(3, 4))
    #print(solution.uniquePaths(3, 5))


test()
