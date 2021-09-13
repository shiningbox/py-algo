from typing import List
from typing import Optional

class Solution:

    def getRow(self, rowIndex: int) -> List[int]:

        vals = [[0 for i in range(rowIndex + 1)] for j in range(rowIndex + 1)]

        # Set first row to be all 1
        for j in range(0, rowIndex + 1):
            vals[0][j] = 1

        for j in range(1, rowIndex + 1):
            i = 1
            while i <= j:
                vals[i][j] = vals[i - 1][j - 1] + vals[i][j - 1]
                i += 1

        return [row[rowIndex] for row in vals]

    def generate(self, numRows: int) -> List[List[int]]:
        results = []
        vals = [[0 for i in range(numRows)] for j in range(numRows)]
        # Set first row to be all 1

        for j in range(0, numRows):
            vals[0][j] = 1
        results = [[1]]
        for j in range(1, numRows):
            i = 1
            col = [1]
            while i <= j:
                vals[i][j] = vals[i-1][j - 1] + vals[i][j - 1]
                col.append(vals[i][j])
                i += 1
            results.append(col)
        return results


def test():
    solution = Solution()
    # test method
    print(solution.getRow(0))
    print(solution.getRow(1))
    print(solution.getRow(3))
    print(solution.getRow(4))

test()
