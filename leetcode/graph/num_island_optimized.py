from typing import List
from typing import Optional

class Solution:

    grid = []
    m = 0
    n = 0

    def dfs(self, i, j):

        if i < 0 or j < 0 or i >= len(self.grid) \
                or j >= len(self.grid[0]):
            return

        if self.grid[i][j] != "1":
            return

        # Mark (i, j) as visited
        self.grid[i][j] = "#"

        self.dfs(i + 1, j)
        self.dfs(i - 1, j)
        self.dfs(i, j + 1)
        self.dfs(i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                        self.dfs(i, j)
                        count += 1

        return count


def test():
    solution = Solution()
    # test method
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(solution.numIslands(grid))
    grid = [["1","1","1"],
            ["0","1","0"],
            ["1","1","1"]]
    print(solution.numIslands(grid))
    grid = [["1", "1", "1"],
            ["0", "1", "1"],
            ["1", "1", "1"]]
    print(solution.numIslands(grid))
    grid = [["1","1","1","1","1","0","1","1","1","1"],
            ["0","1","1","0","1","1","1","0","1","1"],
            ["1","0","1","0","1","1","0","1","0","1"],
            ["1","0","1","1","0","1","1","1","1","1"],
            ["1","1","0","0","1","1","1","1","1","1"],
            ["1","1","0","1","1","1","1","1","1","1"],
            ["1","1","1","1","1","1","1","1","0","1"],
            ["0","1","1","0","1","1","1","1","1","0"],
            ["1","1","0","1","1","0","1","1","1","1"],
            ["0","1","1","1","1","1","0","1","1","1"]]
    print(solution.numIslands(grid))

test()
