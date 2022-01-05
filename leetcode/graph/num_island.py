from typing import List
from typing import Optional

class Solution:

    grid = []
    island = {}
    m = 0
    n = 0

    def get_neighbors(self, u, visited):

        res = []
        next = (u[0] + 1, u[1])
        if next[0] <= self.m - 1 and self.grid[next[0]][next[1]] == "1":
            if next not in visited:
                visited[next] = False
            if not visited[next]:
                res.append(next)

        next = (u[0], u[1] + 1)
        if next[1] <= self.n - 1 and self.grid[next[0]][next[1]] == "1":
            if next not in visited:
                visited[next] = False
            if not visited[next]:
                res.append(next)

        next = (u[0] - 1, u[1])
        if next[0] >= 0 and self.grid[next[0]][next[1]] == "1":
            if next not in visited:
                visited[next] = False
            if not visited[next]:
                res.append(next)

        next = (u[0], u[1] - 1)
        if next[1] >= 0 and self.grid[next[0]][next[1]] == "1":
            if next not in visited:
                visited[next] = False
            if not visited[next]:
                res.append(next)

        return res

    def dfs(self, u, visited, path):

        # Mark the current node as visited
        visited[u] = True
        self.island[u] = True

        path.append(u)

        for n in self.get_neighbors(u, visited):
            if not visited[n]:
                # Visit vertex
                self.dfs(n, visited, path)

        # Now vertex u has all been visited
        # mark it as unvisited
        path.pop()
        visited[u] = False

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        self.island = {}
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1" and (i, j) not in self.island:
                    self.dfs((i, j), {}, [])
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
    print(solution.numIslands(grid))
    grid = [["1", "1", "1"],
            ["0", "1", "1"],
            ["1", "1", "1"]]
    print(solution.numIslands(grid))

test()
