from typing import List
from typing import Optional

class Solution:

    max_size = 0
    grid = []

    def dfs(self, i, j):

        if i < 0 or j < 0 or i >= len(self.grid) \
                or j >= len(self.grid[0]):
            return 0

        if self.grid[i][j] != 1:
            return 0

        size = 1

        # Mark (i, j) as visited
        self.grid[i][j] = -1


        r = self.dfs(i + 1, j)
        down = self.dfs(i - 1, j)
        up = self.dfs(i, j + 1)
        left = self.dfs(i, j - 1)

        size += r + down + up + left
        return size

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        self.max_size = 0
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    size = self.dfs(i, j)
                    if size >= self.max_size:
                        self.max_size = size

        return self.max_size

def test():
    solution = Solution()
    # test method
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(solution.maxAreaOfIsland(grid))


test()
