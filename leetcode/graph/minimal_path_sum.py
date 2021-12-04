from typing import List
from typing import Optional

class Solution:

    def __init__(self):
        self.grid = []
        self.m = 0
        self.n = 0
        self.min_sum = 0

    def get_neighbors(self, u, visited):
        res = []
        if u[0] + 1 <= self.m - 1:
            t = (u[0] + 1, u[1])
            res.append(t)
            visited[t] = False
        if u[1] + 1 <= self.n - 1:
            t = (u[0], u[1] + 1)
            res.append(t)
            visited[t] = False
        return res

    def dfs_path(self, u, visited, path):

        # Mark the current node as visited
        visited[u] = True
        path.append(self.grid[u[0]][u[1]])
        if u == (self.m - 1, self.n - 1):
            sum_p = sum(path)
            if sum_p <= self.min_sum:
                self.min_sum = sum_p
        else:
            # Recur for all the vertices
            # adjacent to this vertex
            for n in self.get_neighbors(u, visited):
                if not visited[n]:
                    self.dfs_path(n, visited, path)

        # Now vertex u has all been visited
        # mark it as unvisited
        path.pop()
        visited[u] = False

    def minPathSum(self, grid: List[List[int]]) -> int:
        visited = {}
        self.min_sum = 2 * 10 ** 5
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.dfs_path((0, 0), visited, [])
        return self.min_sum

def test():
    solution = Solution()
    # test method
    print(solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))



test()
