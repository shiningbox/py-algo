from typing import List
from typing import Optional

class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return
        # Compute a min distance from (i0, j0) to (i1, j1)
        dis = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))]
        dis[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            dis[i][0] += dis[i - 1][0] + triangle[i][0]

        for i in range(1, len(triangle)):
            for j in range(1, len(triangle[i])):
                if j == len(triangle[i]) - 1:
                    dis[i][j] = triangle[i][j] + dis[i - 1][j - 1]
                else:
                    dis[i][j] = triangle[i][j] + min(dis[i-1][j], dis[i-1][j-1])
        return min(dis[-1])


def test():
    solution = Solution()
    # test method
    print(solution.minimumTotal([[-10]]))
    print(solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    print(solution.minimumTotal([[-1],[2,3],[1,-1,-3]]))
    print(solution.minimumTotal([[-1],[3,2],[-3, -1, -2]]))
    print(solution.minimumTotal([[1],[-2,-5],[3,6,9],[-1,2,4,-3]]))
    print(solution.minimumTotal([[1],[-5,-2],[3,6,1],[-1,2,4,-3]]))


test()
