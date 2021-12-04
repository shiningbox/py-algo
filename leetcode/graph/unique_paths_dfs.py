from typing import List
from typing import Optional

class Solution:

    def __init__(self):
        self.m = 0
        self.n = 0
        self.sum = 0

    def get_neighbors(self, u, visited):
        res = []
        if u[0] + 1 <= self.m - 1:
            res.append((u[0] + 1, u[1]))
            visited[(u[0] + 1, u[1])] = False
        if u[1] + 1 <= self.n - 1:
            res.append((u[0], u[1] + 1))
            visited[(u[0], u[1] + 1)] = False
        return res

    def dfs_path(self, u, visited, path):

        # Mark the current node as visited
        visited[u] = True
        path.append(u)
        if u == (self.m - 1, self.n - 1):
            self.sum += 1
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

    def uniquePaths(self, m: int, n: int) -> int:
        visited = {}
        self.m = m
        self.n = n
        self.sum = 0
        self.dfs_path((0, 0), visited, [])
        return self.sum

def test():
    solution = Solution()
    # test method
    print(solution.uniquePaths(3, 2))
    print(solution.uniquePaths(3, 4))
    print(solution.uniquePaths(3, 5))



test()
