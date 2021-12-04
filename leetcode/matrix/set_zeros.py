from typing import List
from typing import Optional

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # Mark zeros
                    rows.add(i)
                    cols.add(j)

        for r in rows:
            for c in range(n):
                print(r, c)
                matrix[r][c] = 0

        for c in cols:
            for r in range(m):
                print(r, c)
                matrix[r][c] = 0



def test():
    solution = Solution()
    # test method
    print(solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))




test()
