from typing import List
from typing import Optional

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        else:
            # convert to 1-d array
            results = []
            mat_array = [None] * (m * n)
            for i in range(len(mat_array)):
                mat_array[i] = mat[i // n][i % n]
            for i in range(r):
                row = []
                for j in range(c):
                    row.append(mat_array[j + c * i])
                results.append(row)
            return results

def test():
    solution = Solution()
    # test method
    print(solution.matrixReshape([[1, 2], [3, 4]], 1, 4))
    print(solution.matrixReshape([[1, 2, 3, 4], [5, 6, 7, 8]], 4, 2))
    print(solution.matrixReshape([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]], 3, 4))
    print(solution.matrixReshape([[1, 2, 3, 4], [5, 6, 7, 8]], 4, 3))


test()
