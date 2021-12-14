from typing import List
from typing import Optional

class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return
        # Store the min distance from current i to last row (j)
        # When i becomes 0, then find out the final result from 0 to j
        res = list(triangle[-1])
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]


def test():
    solution = Solution()
    # test method
    print(solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    print(solution.minimumTotal([[-1],[2,3],[1,-1,-3]]))
    print(solution.minimumTotal([[-1],[3,2],[-3, -1, -2]]))
    print(solution.minimumTotal([[1],[-2,-5],[3,6,9],[-1,2,4,-3]]))
    print(solution.minimumTotal([[1],[-5,-2],[3,6,1],[-1,2,4,-3]]))


test()
